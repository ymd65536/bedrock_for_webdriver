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


def input_search_text(session_id: str, search_text: str) -> None:
    """
    Google検索ボックスにテキストを入力するメソッド
    
    Args:
        session_id (str): WebDriverのセッションID
        search_text (str): 検索したいテキスト
    """    
    # 要素を特定
    res = base.post(
        f"{const.WEB_DRIVER_URL}/{session_id}/element",
        "{\"using\": \"css selector\",\"value\": \"[name=\'q\']\"}"
    ).json()
    
    # 要素のIDを取得
    element_id = res.get("value").get("element-6066-11e4-a52e-4f735466cecf")
    
    res = base.post(
        f"{const.WEB_DRIVER_URL}/{session_id}/element/{element_id}/value",
        "{\"text\":\"" + search_text + "\"}"
    ).json()
    
    return None
