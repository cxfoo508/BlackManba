# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : test_case_botfallbackconfig.py
# DATE : 2021/6/17 14:19
import json
import pytest
from base_case import *
from data_method import *

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

    def test_001_get_fallback_config(self):
        """
        获取默认机器人的回复策略
        """
        agent_id = os.environ.get("agent_id")
        data = {
                  "agent_id": agent_id
                }
        res = get_config(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        print(con_dict)
        threshold_value = con_dict["data"]["threshold_value"]
        resp_content = con_dict["data"]["fallback_responses"]["responses"]
        print(threshold_value)
        print(resp_content)
        resp_content_value = list()
        for dict in resp_content:
            resp_content_value.append(dict["resp_content"])
            print(resp_content_value)
        assert threshold_value == 0.6
        assert '抱歉 我没明白你的意思！' in resp_content_value, resp_content_value

    def test_002_create_fallback_config(self):
        """
        编辑机器人的回复策略
        """
        agent_id = os.environ.get("agent_id")
        data = {
              "agent_id": agent_id,
              "threshold_value": 0.9,
              "status": 1,
              "fallback_responses": {
                "id": 0,
                "mode_id": 1,
                "responses": [
                  {
                    "name": get_str(7),
                    "resp_content": "string",
                    "resp_type_id": 2,
                    "custom_action_id": 0
                  }
                ]

              }
            }
        res = update_config(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        print(con_dict)
        get_data = {
                  "agent_id": agent_id
                }
        res_get = get_config(get_data)
        con_get = res_get.content.decode()
        con_dict_get = json.loads(con_get)
        print(con_dict_get)
        threshold_value = con_dict_get["data"]["threshold_value"]
        resp_content = con_dict_get["data"]["fallback_responses"]["responses"]
        resp_content_value = list()
        for dict in resp_content:
            resp_content_value.append(dict["resp_content"])
        assert threshold_value == 0.9
        assert '抱歉 我没明白你的意思！' not in resp_content_value, resp_content_value



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
        print(con)
        assert '"code":0' in con, con

if __name__ == "__main__":
    pytest.main("-s -v test_case_botfallbackconfig.py::Testcase")