# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : botreponse_data.py
# DATE : 2021/7/22 20:04

import os
from data.data_method import *


class botreponse_data_class:

    def __init__(self):
        """
        回复集参数
        """
        self.setup_login = [{
            "username": "laiye",
            "password": "123123",
            "is_keep_login": True
        }, [], {'token': 'res["data"]["jwt_token"]'}]
        self.setup_create_app = [{
            "agent_name": get_str(4),
            "agent_detail": "测试",
            "agent_logo": "string",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["msg"]=="机器人创建成功"'], {'agent_id': 'res["data"]["agent_id"]'}]
        self.teardown_class = [{
            "agent_id": os.environ.get("agent_id")
        }, ['res["code"]==0'], {}]
        """
        获取对话机器人回复类型列表参数
        """
        self.response_type_001 = [{}, ['res["code"]==0', 'res["data"][0]["name"]=="text"'], {'type_id': 'res["data"][0]["id"]', 'type_text_id':'res["data"][0]["id"]', 'type_image_id': 'res["data"][1]["id"]', 'type_voice_id': 'res["data"][2]["id"]'}]
        """
        获取对话机器人回复集模式列表
        """
        self.responses_mode_001 = [{}, ['res["code"]==0', 'res["data"][0]["name"]=="all"'], {'mode_id':'res["data"][0]["id"]', 'mode_all_id': 'res["data"][0]["id"]', 'mode_random_id': 'res["data"][1]["id"]', 'mode_one_id': 'res["data"][2]["id"]'}]
        """
        获取系统内置自定义动作回复
        """
        self.custom_action_001 = [{}, ['res["code"]==0', 'res["data"][0]["name"]=="默认回复1"'], {'action_id': 'res["data"][0]["id"]', 'action_id_001': 'res["data"][0]["id"]', 'action_id_002': 'res["data"][1]["id"]', 'action_id_003': 'res["data"][2]["id"]'}]
        """
        根据ID获取回复集
        """
        self.get_responses_001 = [
            {
                "responses_id": None
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.get_responses_002 = [
            {
                "responses_id": ""
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.get_responses_003 = [
            {
                "responses_id": " "
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.get_responses_004 = [
            {
                "responses_id": get_str(4)
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.get_responses_005 = [
            {
                "responses_id": get_int(10)
            }
            , ['res["code"]==0', 'res["msg"]=="回复集获取失败"'], {}]
        self.get_responses_006 = [
            {
                "responses_id": os.environ.get("responses_id")
            }
            , [], {}]
        """
        新增或者修改回复集
        """
        self.update_responses_001 = [{
                                      "id": None,
                                      "name": None,
                                      "mode_id": None,
                                      "type_id": None,
                                      "skill_id": None,
                                      "status": None,
                                      "agent_id": None,
                                      "responses": [
                                        {
                                          "id": None,
                                          "resps_id": None,
                                          "name": None,
                                          "response_once": None,
                                          "resp_content": None,
                                          "resp_order": None,
                                          "resp_type_id": None,
                                          "sug_intents": None,
                                          "custom_action_id": None,
                                          "event_id": None
                                        }
                                      ]
                                    }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_002 = [{
            "id": get_int(10),
            "name": None,
            "mode_id": None,
            "type_id": None,
            "skill_id": None,
            "status": None,
            "agent_id": None,
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": None,
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_003 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": None,
            "type_id": None,
            "skill_id": None,
            "status": None,
            "agent_id": None,
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": None,
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_004 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": None,
            "skill_id": None,
            "status": None,
            "agent_id": None,
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": None,
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_005 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": None,
            "status": None,
            "agent_id": None,
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": None,
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_006 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": None,
            "agent_id": None,
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": None,
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_007 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": None,
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": None,
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_008 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": None,
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_009 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": None,
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_010 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": None,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_011 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": None,
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_012 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": None,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_013 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": None,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_014 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": None,
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_015 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": None,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_016 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]

        self.update_responses_017 = [{
            "id": get_int(10),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_018 = [{
            "id": get_str(4),
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_019 = [{
            "id": "asdghjkjk~!@#$#$%%^^^&&**(11123",
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        #
        self.update_responses_020 = [{
            "id": "",
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_021 = [{
            "id": " ",
            "name": get_str(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        # 成功更新回复集
        self.update_responses_022 = [{
            "id": None,
            "name": get_int(4),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_023 = [{
            "id": None,
            "name": "sshdlkghlkajsl~!@!@#$$%%^^&&**((())_+qwe`132121",
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_024 = [{
            "id": None,
            "name": "",
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_025 = [{
            "id": None,
            "name": " ",
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_026 = [{
            "id": None,
            "name": get_str(128),
            "mode_id": 1,
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_027 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": get_int(4),
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]

        self.update_responses_028 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": get_str(4),
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_029 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": get_int(4),
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_030 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": "sdsd1234578!@#$%^&*()_+~",
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_031 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": "",
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_032 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": " ",
            "type_id": 1,
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_033 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": get_str(4),
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_034 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": get_int(4),
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_035 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": "1234577asdglgfhla~!@#$%^&**(()_+",
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_036 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": "",
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_037 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": " ",
            "skill_id": get_int(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_038 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": get_str(4),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_039 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": "1234637593490QWSfgfgasdhjd~!!@#%^&*()_+[]:",
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_040 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": "",
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_041 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": " ",
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_042 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_043 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 0,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_044 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": get_str(4),
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_045 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": get_int(4),
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_046 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": "1234!@~#$%^^&&**())__{;'./}",
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_047 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": "",
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_048 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": " ",
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_049 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": get_int(20),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_050 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": get_str(4),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_051 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": "123436ashgklhadhj~!@#$%^&*()_+|}{",
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_052 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": "",
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_053 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": " ",
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_054 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_str(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_055 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": get_int(4),
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_056 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": "123546~!@#$%^&&*()){}:",
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_057 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": "",
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_058 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": " ",
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_059 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": 0,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_060 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": get_int(4),
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_061 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": get_str(4),
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_062 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": "123~@!#$%^&*()_+';",
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_063 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": "",
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_064 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": " ",
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_065 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(128),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_066 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_int(128),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_067 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": "sgkjhjkguqwei~!@$%^&*()_+[]';",
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_068 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": "",
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_069 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": " ",
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_070 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 1,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_071 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": get_str(4),
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_072 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": get_int(4),
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_073 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": "123689sghhhga;wie~!@#$%^&*()_+",
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_074 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": "",
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_075 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": " ",
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_076 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_077 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(1024),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_078 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(1025),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_079 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_int(2048),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_080 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_int(2049),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==200', '"pymysql.err.DataError" in res["msg"]'], {}]
        self.update_responses_081 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": "12368~!@#$%^&*()_+{}:?><",
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_082 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": "",
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_083 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": " ",
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_084 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_085 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": get_str(4),
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_086 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": get_int(4),
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_087 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": "`2145569960!@#$%^&*()_+:L><dhajskh",
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_088 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": "",
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_089 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": " ",
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_090 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": 1,
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_091 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": get_int(4),
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_092 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": get_str(4),
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_093 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": get_int(4),
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_094 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": "123455~!@#$%^&**()_P:><?wdfghjg",
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_095 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": "",
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_096 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": " ",
                    "sug_intents": get_int(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_097 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": get_str(3),
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_098 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": "shihg`1234!@#$%^&*()<>?",
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_099 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": "",
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_100 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": " ",
                    "custom_action_id": 1,
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_101 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": get_str(4),
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_102 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": get_int(4),
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_103 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": "123~!@#$%^&*()_+:?>>",
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_104 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": "",
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_105 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": " ",
                    "event_id": 1
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_106 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": get_str(4)
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_107 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": get_str(4)
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_108 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": get_int(4)
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_109 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": "1234~!@#$%^&*()_PL:>?{}1serafdadf"
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_110 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": ""
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_111 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": " "
                }
            ]
        }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_responses_112 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }
            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_113 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }


            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        self.update_responses_114 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                },{
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }

            ]
        }
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {}]
        # 场景case参数
        self.update_responses_115 = [{
            "id": os.environ.get("responses_id"),
            "name": get_str(4),
            "mode_id": os.environ.get("mode_id"),
            "type_id": os.environ.get("type_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_116 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_all_id"),
            "type_id": os.environ.get("type_text_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_text_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_001"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_117 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_all_id"),
            "type_id": os.environ.get("type_image_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_text_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_001"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_118 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_all_id"),
            "type_id": os.environ.get("type_voice_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_text_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_001"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_119 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_random_id"),
            "type_id": os.environ.get("type_voice_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_text_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_001"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_120 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_one_id"),
            "type_id": os.environ.get("type_voice_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_text_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_001"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_121 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_one_id"),
            "type_id": os.environ.get("type_voice_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_text_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_002"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_122 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_one_id"),
            "type_id": os.environ.get("type_voice_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_text_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_003"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        self.update_responses_123 = [{
            "id": None,
            "name": get_str(4),
            "mode_id": os.environ.get("mode_one_id"),
            "type_id": os.environ.get("type_voice_id"),
            "skill_id": os.environ.get("skill_id"),
            "status": 1,
            "agent_id": os.environ.get("agent_id"),
            "responses": [
                {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_text_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_001"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_image_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_002"),
                    "event_id": None
                }, {
                    "id": None,
                    "resps_id": None,
                    "name": get_str(4),
                    "response_once": 0,
                    "resp_content": get_str(4),
                    "resp_order": 1,
                    "resp_type_id": os.environ.get("type_voice_id"),
                    "sug_intents": os.environ.get("intents_id"),
                    "custom_action_id": os.environ.get("action_id_003"),
                    "event_id": None
                }]}
            , ['res["code"]==0', 'res["msg"]=="回复集更新成功"'], {'responses_id': 'res["data"]["lastrowid"]'}]
        """
        删除回复集
        """
        self.delete_responses_001 = [
            {
                "responses_id": None
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.delete_responses_002 = [
            {
                "responses_id": ""
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.delete_responses_003 = [
            {
                "responses_id": " "
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.delete_responses_004 = [
            {
                "responses_id": get_str(4)
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.delete_responses_005 = [
            {
                "responses_id": get_int(10)
            }
            , ['res["code"]==0', 'res["msg"]=="回复集删除成功"'], {}]
        self.delete_responses_006 = [
            {
                "responses_id": os.environ.get("responses_id")
            }
            , ['res["code"]==0', 'res["msg"]=="回复集删除成功"'], {}]