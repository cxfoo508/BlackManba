# coding = utf-8
import json

import pytest

from base_case import *
from data.creat_skills import *
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

        # 创建技能faq
        skill_parms = create_skills_parm()
        data = skill_parms.parm_001
        data[0]["agent_id"] = int(os.environ.get("agent_id"))
        data[0]["intent_id"] = int(os.environ.get("intent_id"))
        print(data)
        res = create_skills(data[0])
        print(res.content.decode())
        con = res.content.decode()
        con_dict = json.loads(con)
        assert (con_dict["data"]["agent_id"] == int(os.environ.get("agent_id"))) and (
                con_dict["data"]["skill_id"] != "") and (
                       con_dict["data"]["skill_one_id"] != None) and (con_dict["data"]["skill_name"] != None), con
        os.environ["skill_id"] = str(con_dict["data"]["skill_id"])
        os.environ["skill_one_id"] = str(con_dict["data"]["skill_one_id"])
        os.environ["skill_name"] = con_dict["data"]["skill_name"]

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
        assert '{"code":0,"msg":"词槽创建成功","data":{"slot_id":' in res, res

    def test002_slot_update(self):
        """
        更新slot为意图词槽
        """
        print("---slot update---")
        os.environ['slot_name'] = get_str(3)
        data = {
            "slot_id": str(os.environ.get("slot_id")),
            "agent_id": str(os.environ.get("agent_id")),
            "slot_name": os.environ.get('slot_name'),
            "intent_value_list": [
                {
                    "intent_id": str(os.environ.get("intent_id")),
                    "value": "string"
                }
            ],

            "is_from_text": 0,
            "is_list": 0,
            "is_compound": 0
        }
        res = SlotCaseBase.slot_update(data)
        assert '{"code":0,"msg":" 词槽更新成功","data":{"rowcount"' in res, res

    def test003_slot_get(self):
        """
        获取词槽
        """
        print('---slot list---')
        data = {
            "agent_id": os.environ.get("agent_id"),
            "page_no": 1,
            "number_per_page": 20
        }

        res = SlotCaseBase.slot_list(data)
        con = json.loads(res)
        rowl = len(con['data']['rows'])
        assert (rowl == 1) and (os.environ.get('slot_id') in res) and (
                os.environ.get('slot_name') == con['data']['rows'][0]['slot_name']), res

    def test004_slot_ref_skills(self):
        """
        获取引用词槽的技能
        """
        data = {
            "agent_id": os.environ.get('agent_id'),
            "slot_id_list": [
                os.environ.get('slot_id')
            ]
        }
        res = SlotCaseBase.slot_ref_skills(data)

    def test005_slot_del(self):
        """
        删除词槽
        """
        print('---slot del---')
        data = {
            "agent_id": os.environ.get('agent_id'),
            "slot_id_list": [os.environ.get('slot_id')]
        }
        res = SlotCaseBase.slot_del(data)
        assert '{"code":0,"msg":"词槽删除成功","data":{"rowcount":1}}' in res, res

    def teardown_class(self):
        """
        删除agent
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
    pytest.main("-s -v test_slot_case.py::TestCass")