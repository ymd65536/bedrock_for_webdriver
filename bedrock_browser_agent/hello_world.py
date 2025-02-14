import webdriver.tool as wd_tool
import bedrock.core.const as const
import bedrock.tool as bdr_tool

if __name__ == "__main__":
    print(wd_tool.help())
    print(bdr_tool.boto3_version())
    print(const.region_name["apne1"])

    agent = bdr_tool.agent_action()
    agent.set_query("https://www.google.com/ をGoogle Chromeのウィンドウで開く")
    res = agent.execute(const.claude_model_ids["claude-3-haiku"])
    session_id = None

    if res:
        if res[0] == "open_window":
            session_id = wd_tool.open_window(
                res[1].get("url"), res[1].get("browser"))
    
        agent.set_query(f"WebDriverのセッションID:{session_id},Google検索ボックスに「Amazon Bedrock」と入力する")
        res = agent.execute(const.claude_model_ids["claude-3-haiku"])
        print(res)

        if res:
            if res[0] == "input_search_text":
                wd_tool.input_search_text(res[1].get("session_id"), res[1].get("search_text"))