# coding = utf-8
import json

import pytest

from base_case import *
from data_method import *


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

    def setup_class(self):
        """
        创建app ，创建意图
        """
        print("---setup_class---")
        os.environ["token"] = self.auth_login(None)

        data = {
            "agent_name": get_str(4),
            "agent_detail": "测试",
            "agent_logo": "string",
            "lang": "zh-CN"
        }
        res = creat_app(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        assert '{"code":0,"msg":"机器人创建成功","data":{"agent_id"' in con, con
        os.environ["agent_id"] = con_dict["data"]["agent_id"]
        print(f"Agent_id:{os.environ.get('agent_id')}")
        # 创建意图
        data = {
            "agent_id": os.environ.get('agent_id'),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 0,
                    "name": "相似问"
                }
            ],
            "keywords_eq": [
                {
                    "id": 0,
                    "name": "严格"
                }
            ],
            "keywords_include": [
                {
                    "id": 0,
                    "name": "包含"
                }
            ]
        }
        res = create_intent(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        print(con_dict)
        os.environ["intent_id"] = str(con_dict["data"]["intent_id"])

    def teardown_class(self):
        """
        删除app
        """
        print("---teardown_class---")
        data = {
            "agent_id": os.environ.get("agent_id")
        }
        res = del_app(data)
        con = res.content.decode()
        print(con)
        assert '"code":0' in con, con


if __name__ == '__main__':
    pytest.main("-s -v test_case_skills.py::TestCass")
