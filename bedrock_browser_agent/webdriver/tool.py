import webdriver.core.base as base
import webdriver.core.const as const


def help() -> str:
    return "This is a help message from webdriver.tool module."


def open_window(url, browser) -> str:
    if browser == "Microsoft Edge":
        url = f"microsoft-edge:{url}"
    elif browser.upper() == "Chrome".upper() or browser.upper() == "Google Chrome".upper():
        res = base.post(
            const.WEB_DRIVER_URL,
            '{"capabilities":{}}'
        ).json()

        # セッションIDを取得
        sessionId = res.get("value").get("sessionId")
        res = base.post(
            f"{const.WEB_DRIVER_URL}/{sessionId}/url",
            '{"url": "' + url + '"}'
        ).json()

        return sessionId
    elif browser == "Firefox":
        url = f"firefox:{url}"
    else:
        url = f"{url}"
    return None
