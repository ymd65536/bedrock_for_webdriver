# Amazon Bedrockでブラウザを操作する

## 概要

Amazon Bedrockを使ってブラウザを操作するサンプルプログラムです。

## Setup

```bash
export WEBDRIVER_PORT=54088
chromedriver --port=$WEBDRIVER_PORT
```

## Run

```bash
export WEBDRIVER_PORT=54088
python bedrock_browser_agent/hello_world.py
```

## Set AWS_PROFILE

```bash
export AWS_PROFILE=your-profile
```

## Model List

```bash
aws bedrock get-foundation-model --model-identifier anthropic.claude-v2:1 --query 'modelDetails.modelArn' --output text
```
