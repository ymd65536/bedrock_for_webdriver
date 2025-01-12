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

    print(res)
    if res:
        session_id = wd_tool.open_window(
            res[1].get("url"), res[1].get("browser"))
        print(session_id)
