# Description: Constants for the bedrock module.
import os
PORT = os.getenv('WEBDRIVER_PORT', None)
WEB_DRIVER_URL = 'http://localhost:{0}/session'.format(PORT)

region_name = {
    "apne1": "ap-northeast-1"
}
claude_model_ids = {
    "claude-3-haiku": "anthropic.claude-3-haiku-20240307-v1:0"
}

inferenceConfig = ({"maxTokens": 1000, "temperature": 0})
