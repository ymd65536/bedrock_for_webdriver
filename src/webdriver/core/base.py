import requests


def post(url: str, payload: str) -> dict:
    res = requests.post(
        url,
        headers={'Content-Type': 'application/json'},
        data=payload
    )

    return res
