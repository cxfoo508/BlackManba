import requests

URL = "http://172.17.202.22:5015"


def request_data(url, data=None, check_data=None):
    """
    request
    """
    send_url = url
    header = {
        "Content-Type": "application/json"
    }
    print(f"{URL}{send_url}")
    request = requests.post(url=f"{URL}{send_url}", json=data, headers=header)
    return request


def query(data):
    """

    """
    body = {
        "msg_body": {
            "text": {
                "content": data
            }
        },
        "metadata": [],
        "agent_id": 0,
        "skill_ids": [
            0
        ],
        "debug": False
    }
    url = "/core/engine/dm/bot-response"
    res = request_data(url, data=body)
    return res
