import hashlib
import json
import os
import random
import string
import time
import zlib
from urllib.parse import urlencode

import requests

from modules.logger import log

CHAR_LIST = []

[[CHAR_LIST.append(e) for e in string.digits] for i in range(0, 2)]
[[CHAR_LIST.append(e) for e in string.digits] for i in range(0, 2)]
[[CHAR_LIST.append(e) for e in string.digits] for i in range(0, 2)]


def GetChars(length):
    random.shuffle(CHAR_LIST)
    return "".join(CHAR_LIST[0:length])


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


def get_headers():
    """
    获取渠道header
    """
    # 开放平台的基础信息
    secret = "W8AF78C8A9AEEDF774062AC7E600513E"
    pubkey = "M937AB21C263110E"
    # 秒级别时间戳
    timestamp = str(int(time.time()))
    nonce = GetChars(32)
    sign = hashlib.sha1((nonce + timestamp + secret).encode()).hexdigest()
    data = {
        "account_key": pubkey,
        "nonce": nonce,
        "sign": sign,
        "timestamp": timestamp
    }
    headers = {}
    for k, v in data.items():
        headers["auth_" + k] = v
    return headers


def channel_auth(data=None):
    """
    获取渠道权鉴Token
    """
    print(f'data:{data}')
    url = '/v1/channels/auth'
    res = rear_post(url, data)
    con = res.content.decode()
    print(f'res:{con}')
    return con


def get_channel_auth():
    headers = get_headers()
    res = channel_auth(data=headers)
    con_data = json.loads(res)
    return con_data["data"]["access_token"]


def request_data_channel(url, data=None):
    """
    渠道post
    """
    send_url = url
    URL = os.environ.get("url")
    token = os.environ.get("access_token")
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    print(f"Bearer {token}")
    print(f"{URL}{send_url}")
    request_channel = requests.post(url=f"{URL}{send_url}", json=data, headers=header)
    return request_channel






