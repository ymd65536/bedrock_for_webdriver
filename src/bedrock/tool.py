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
    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime", region_name=const.region_name["apne1"])

    def simple_invoke_model(self, model_id: str, payload: dict):
        response = self.client.invoke_model(
            ModelId=model_id,
            Payload=payload
        )
        return response

    def open_window(self):
        return "Opening a window."

    def close_window(self):
        return "Closing a window."
