import os

import requests

from modules.logger import log


def rear_post(url, data):
    """
    后端请求
    """
    send_url = url
    URL = os.environ.get('url')
    token = os.environ.get("token")
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    log.info(f'send url: {URL}{send_url}')
    res = requests.post(url=f"{URL}{send_url}", json=data, headers=header)
    log.info(f'res time: {res.elapsed.total_seconds()}')
    return res


