# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : case_botresponse.py
# DATE : 2021/6/17 15:27

import json

import pytest

from base_case import *
from data.data_method import *


class Testcase:
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

    def create_responses(self):
        """
        新建回复集
        """
        agent_id = os.environ.get("agent_id")
        data = {
            "id": None,
            "name": get_str(5),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": 1,
            "status": 1,
            "agent_id": agent_id,
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(5),
                    "response_once": 0,
                    "resp_content": get_str(5),
                    "resp_order": 0,
                    "resp_type_id": 1,  # 对话机器人回复类型列表，1为自定义默认回复，会读取自定义动作回复 custom_action_id
                    "sug_intents": 1,
                    "custom_action_id": 1,  # 自定义动作回复
                    "event_id": None
                },
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(5),
                    "response_once": 0,
                    "resp_content": get_str(5),
                    "resp_order": 0,
                    "resp_type_id": 2,
                    "sug_intents": 1,
                    "custom_action_id": 1,
                    "event_id": None
                }
            ]
        }
        res = update_responses(data)
        con = res.content.decode()
        print(con)
        con_dict = json.loads(con)
        responses_id = con_dict["data"]["lastrowid"]
        return responses_id

    def update_responses(self, responses_id):
        """
        更新回复集
        """
        agent_id = os.environ.get("agent_id")
        data_update = {
            "id": responses_id,
            "name": get_str(5),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": 1,
            "status": 1,
            "agent_id": agent_id,
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(5),
                    "response_once": 0,
                    "resp_content": get_str(5),
                    "resp_order": 0,
                    "resp_type_id": 1,  # 对话机器人回复类型列表，1为自定义默认回复，会读取自定义动作回复 custom_action_id
                    "sug_intents": 1,
                    "custom_action_id": 1,  # 自定义动作回复
                    "event_id": None
                },
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(5),
                    "response_once": 0,
                    "resp_content": get_str(5),
                    "resp_order": 0,
                    "resp_type_id": 2,
                    "sug_intents": 1,
                    "custom_action_id": 1,
                    "event_id": None
                }
            ]
        }
        res_update = update_responses(data_update)
        con_update = res_update.content.decode()
        con_dict_update = json.loads(con_update)
        print(con_dict_update)
        return con_dict_update

    def delete_responses(self, responses_id):
        """
        删除回复集
        """
        data = {
            "responses_id": responses_id
        }
        res = delete_responses(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        print(con_dict)
        return con_dict

    def get_responses(self, responses_id):
        """
        获取回复集
        """
        data = {
            "responses_id": responses_id
        }
        res = get_responses(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        print(con_dict)
        return con_dict

    def setup_class(self):
        """
        开始步骤创建机器人
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

    def test_001_get_response_type(self):
        """
        获取对话机器人回复类型列表
        """
        data = {}
        res = response_type(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        description_list = list()
        for dict in con_dict["data"]:
            description_list.append(dict["description"])
        print(description_list)
        assert ['文本', '图片', '语音'] == description_list

    def test_002_get_responses_type(self):
        """
        获取对话机器人回复集类型列表
        """
        data = {}
        res = responses_type(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        description_list = list()
        for dict in con_dict["data"]:
            description_list.append(dict["description"])
        print(description_list)
        assert ['默认回复', '流程回复', '更新回复', '预置提示', '延时追问'] == description_list

    def test_003_get_responses_mode(self):
        """
        获取对话机器人回复集模式列表
        """
        data = {}
        res = responses_mode(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        description_list = list()
        for dict in con_dict["data"]:
            description_list.append(dict["description"])
        print(description_list)
        assert ['全部', '随机', '依次'] == description_list

    def test_004_get_custom_action(self):
        """
        获取系统内置自定义动作回复
        """
        data = {}
        res = custom_action(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        resp_content_list = list()
        for dict in con_dict["data"]:
            resp_content_list.append(dict["resp_content"])
        print(resp_content_list)
        assert ['action:default_aciton1', 'action:default_aciton2', 'action:default_aciton3'] == resp_content_list

    def test_005_create_responses(self):
        """
        新增回复集
        """
        response_id = self.create_responses()
        print(response_id)
        res = self.get_responses(response_id)
        assert res["result"]["id"]
        self.delete_responses(response_id)

    def test_006_update_responses(self):
        """
        根据ID更新回复集
        """
        response_id = self.create_responses()
        print(response_id)
        res = self.get_responses(response_id)
        print(res["result"]["name"])
        self.update_responses(response_id)
        res1 = self.get_responses(response_id)
        print(res1["result"]["name"])
        assert res["result"]["name"] != res1["result"]["name"]
        self.delete_responses(response_id)

    def test_007_get_responses(self):
        """
        根据id获取回复集
        """
        response_id = self.create_responses()
        print(response_id)
        res = self.get_responses(response_id)
        print(res["result"]["name"])
        assert res["result"]["id"] == response_id
        self.delete_responses(response_id)

    def test_007_delete_responses(self):
        """
        删除回复集
        """
        response_id = self.create_responses()
        print(response_id)
        self.delete_responses(response_id)
        res = self.get_responses(response_id)
        print(res)
        assert res["result"] == None

    def teardown(self):
        """
        收尾工作
        """
        print("---tear down---")
        data = {
            "agent_id": os.environ.get("agent_id")
        }
        res = del_app(data)
        con = res.content.decode()
        assert '"code":0' in con, con


if __name__ == "__main__":
    pytest.main("-s -v case_botresponse.py::Testcase")
