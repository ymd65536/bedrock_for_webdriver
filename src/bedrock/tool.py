# This is a simple function that prints the version of boto3 that is installed.
import boto3
import core.const as const


def boto3_version():
    """
    This function returns the version of boto3 that is installed.
    Returns:
        str: The version of boto3 that is installed.
    """
    return boto3.__version__


def help() -> str:
    """
    This is a help message from bedrock.tool module.
    Returns:
        str: _description_
    """
    return "This is a help message from bedrock.tool module."


class agent_action:
    """
    This class is used to interact with the agent.
    """

    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime", region_name=const.region_name["apne1"])

    def simple_invoke_model(self, model_id: str, payload: dict):
        return "Invoking model."

    def set_query(self, user_query: str):
        self.prompt = f"<text>{user_query}</text>"
        self.messages = [
            {
                "role": "user",
                "content": [{"text": self.prompt}]
            }
        ]

    def _define_tools(self):
        open_window = {
            "toolSpec": {
                "name": "open_window",
                "description": "指定されたURLを指定されたブラウザのウィンドウで開く",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string",
                                "description": "URL"
                            },
                            "browser": {
                                "type": "string",
                                "description": "ブラウザで開く"
                            }
                        },
                        "required": ["url", "browser"]
                    }
                }
            }
        }
        tools = [open_window]
        return tools

    def execute(self, model_id: str):
        self.tool_list = self._define_tools()
        response = self.client.converse(
            modelId=model_id,
            messages=self.messages,
            toolConfig={
                "tools": self.tool_list,
                "toolChoice": {"any": {}}
            },
            inferenceConfig=const.inferenceConfig
        )
        tool_params = response.get("output", {}).get(
            "message", {}).get("content", [{}])[0].get("toolUse", {})

        function_name = tool_params.get("name", "")
        input_params = tool_params.get("input", {})

        return function_name, input_params
