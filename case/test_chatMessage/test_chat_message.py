import json

import pytest

from base_case import *
from case.test_chatMessage.message_base import ChatMessageCase


class TestCase:

    def auth_login(self):
        """
        登陆
        """

        print("---test login---")
        data = {
            "username": "laiye",
            "password": "123123",
            "is_keep_login": True
        }
        res = auth_login(data)
        con = res.content.decode()
        con_data = json.loads(con)
        return con_data["data"]["jwt_token"]

    def test001_message(self):
        """
        对话
        """
        os.environ["token"] = self.auth_login()

        text = '员工级别'
        data = {
            "msg_body": {
                "text": {"content": text}
            },
            "agent_id": '0'
        }
        con = ChatMessageCase.chat_get_response(data)

    def test002_get_history(self):
        """
        获取测试历史数据
        """
        data = {
            "agent_id": '0'
        }
        con = ChatMessageCase.chat_get_hestory(data)

    def test003_reset(self):
        """
        晴空会话
        """
        con = ChatMessageCase.chat_reset()
        assert '{"code":0,"msg":"","data":{}}' in con, con


if __name__ == '__main__':
    pytest.main("-s -v test_chat_message.py::TestCass")
