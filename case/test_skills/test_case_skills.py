# coding = utf-8
import json

import pytest

from base_case import *
from data.creat_skills import create_skills_parm
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

    def get_data001(self):
        data_list = create_skills_parm.get_parms_list("parm_001")
        return data_list

    @pytest.fixture(params=get_data001(None))
    def get_data_list001(self, request):
        return request.param

    def test001_create_skill(self, get_data_list001):
        """
        创建技能faq
        """
        data = get_data_list001
        print(data)
        data[0]["agent_id"] = int(os.environ.get("agent_id"))
        data[0]["intent_id"] = int(os.environ.get("intent_id"))
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

    # @pytest.mark.skip
    def test002_set_skill(self):
        """
        技能设置
        """
        print("\n-查询 set skill-")
        data1 = {
            "agent_id": int(os.environ.get("agent_id")),
            "skill_one_id": int(os.environ.get("skill_one_id"))
            # "skill_one_id": 11112
        }
        con = get_skills_set_detail(data1)
        print("-设置技能-")
        data = {
            "agent_id": int(os.environ.get("agent_id")),
            "skill_one_id": int(os.environ.get('skill_one_id')),
            # "skill_one_id":111111,
            "max_interval": 5,
            "node_history": 2
        }
        res = set_skill(data)
        print('-查询 set skill-')
        get_skills_set_detail(data1)

    def test003_get_skill_list(self):
        """
        获取技能列表
        """
        data = {
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "skill_name": ''
            },
            "filters": {
                "skill_type": [
                    0
                ],
                "skill_status": [
                    2
                ]
            },
            "sort": {
                "update_time": "string"
            },
            "page_size": 20,
            "page_num": 1
        }
        res = get_skills_list(data)
        print(res.content.decode())

    def test004_get_skill_detail(self):
        """
        获取单个技能信息
        """
        data = {
            "agent_id": int(os.environ.get("agent_id")),
            "skill_one_id": int(os.environ.get("skill_one_id"))
        }
        res = get_skills_detail(data)

    def test005_edit_skills(self):
        """
        编辑技能
        """
        data = {
            "agent_id": int(os.environ.get("agent_id")),
            "skill_one_id": int(os.environ.get("skill_one_id")),
            "skill_name": get_str(5),
            "intent_id": int(os.environ.get("intent_id")),
            "description": "string"
        }
        res = edit_skills(data)

    def test005_del_kills(self):
        """
        删除技能
        """
        data = {
            "agent_id": int(os.environ.get("agent_id")),
            "skill_id": int(os.environ.get("skill_id")),
            "skill_one_id": int(os.environ.get("skill_one_id"))
        }
        con = del_skill(data)

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
    pytest.main("-s -v test_case_skills.py::TestCass")
