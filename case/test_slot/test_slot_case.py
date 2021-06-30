# coding = utf-8
import json

import pytest

from base_case import *
from data_method import *
from slot_base import SlotCaseBase


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

    def test001_slot_create(self):
        """
        创建词槽
        """
        data = {
            "agent_id": os.environ.get("agent_id"),
            "slot_name": "string",
            "is_from_text": 0,
            "is_list": 0,
            "is_compound": 0
        }
        res = SlotCaseBase.slot_create(data)
        res_dict = json.loads(res)
        os.environ["slot_id"] = res_dict["data"]["slot_id"]
        assert '{"code":0,"msg":"slot.create.success.0","data":{"slot_id":' in res, res

    def test002_slot_update(self):
        """
        更新slot
        """
        print("---slot update---")
        data = {
            "slot_id": str(os.environ.get("slot_id")),
            "agent_id": str(os.environ.get("agent_id")),
            "slot_name": get_str(3),
            "intent_value_list": [
                {
                    "intent_id": str(os.environ.get("intent_id")),
                    "value": "string"
                }
            ],
            "entity_intent_list": [
                {
                    "entity_id": "string",
                    "intent_id_list": [
                        "string"
                    ]
                }
            ],
            "is_from_text": 0,
            "is_list": 0,
            "is_compound": 0
        }
        res = SlotCaseBase.slot_update(data)
        # assert

    def teardown_class(self):
        print("---teardown_class---")
        data = {
            "agent_id": os.environ.get("agent_id")
        }
        res = del_app(data)
        con = res.content.decode()
        print(con)
        assert '"code":0' in con, con


if __name__ == '__main__':
    pytest.main("-s -v test_slot_case.py::TestCass")
