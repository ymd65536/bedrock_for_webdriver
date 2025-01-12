import webdriver.tool as wd_tool
import bedrock.core.const as const
import bedrock.tool as bdr_tool

if __name__ == "__main__":
    print(wd_tool.help())
    print(bdr_tool.boto3_version())
    print(const.region_name["apne1"])
