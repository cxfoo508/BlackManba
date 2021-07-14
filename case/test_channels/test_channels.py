# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : test_channels.py
# DATE : 2021/7/9 16:33

from base_case import *


class Testcase:

    def setup_class(self):
        os.environ["access_token"] = get_channel_auth()
        self.userid = GetChars(8)
        self.nickname = GetChars(4)

    def test_001_create_channel_user(self):
        data = {
              "user_id": self.userid,
              "avatar_url": "http://www.baidu.com",
              "nickname": self.nickname
            }
        res = channel_create_user(data=data)

    def test_002_get_channel_user(self):
        data = {
              "user_id": self.userid
            }
        res = channel_get_user(data=data)

    def test_003_channel_response(self):
        # content = ["员工级别", "101", "719667588@qq.com"]
        content = ["sadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasda",
                   "sadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasda",
                   "sadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasda",
                   "sadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasda@qq.com",
                   "sadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasdasadadadasdasdasdasda"]
        for i in content:
            data = {
                "user_id": self.userid,
                "msg_body": {
                    "text": {
                        "content": i
                    }
                }
            }
            res = channel_get_response(data=data)
