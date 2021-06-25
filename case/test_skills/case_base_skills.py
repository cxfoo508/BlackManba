# coding = utf-8
import os

import requests

# URL =  "http://172.17.202.22:5015"
URL = "http://39.105.24.211:8080"


# URL = "http://59.110.157.33:5697"


def request_data(url, data=None, check_data=None):
    """
    request
    """
    send_url = url
    token = os.environ.get("token")
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    print(f"{URL}{send_url}")
    request = requests.post(url=f"{URL}{send_url}", json=data, headers=header)
    return request


def creat_app(data):
    """
    创建机器人
    """
    url = "/v1/agent/create"
    res = request_data(url, data)
    return res
