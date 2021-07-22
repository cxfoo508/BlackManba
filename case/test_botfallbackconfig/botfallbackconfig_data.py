# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : botfallbackconfig_data.py
# DATE : 2021/7/20 15:01
import os

from data_method import *

class botfallbackconfig_data_class:

    def __init__(self):
        """
        回复策略参数
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
        查看兜底策略的参数
        """
        self.param_get_config_001 = [{
                  "agent_id": None
                }, [], {}]
        self.param_get_config_002 = [{
            "agent_id": get_str(4)
        }, ['res["code"]==200', 'res["data"]==None'], {}]
        self.param_get_config_003 = [{
            "agent_id": get_int(10)
        }, ['res["code"]==0', 'res["data"]["threshold_value"]==0.6'], {}]
        self.param_get_config_004 = [{
            "agent_id": "Nonessadj231874523482747!@#$^%&*%($($"
        }, ['res["code"]==200', 'res["data"]==None'], {}]
        self.param_get_config_005 = [{
            "agent_id": os.environ.get("agent_id")
        }, ['res["code"]==0', 'res["data"]["threshold_value"]==0.6'], {}]
        self.param_get_config_006 = [{
            "agent_id": ""
        }, ['res["code"]==200', 'res["data"]==None'], {}]
        self.param_get_config_007 = [{
            "agent_id": " "
        }, ['res["code"]==200', 'res["data"]==None'], {}]
        self.param_get_config_008 = [{
            "agent_id": os.environ.get("agent_id")
        }, ['res["code"]==0', 'res["data"]["fallback_responses"]["responses"][0]["resp_content"]=="test"'], {}]
        """
        更新兜底策略
        """
        # 所有参数依次为None
        self.update_config_001 = [{
                                "agent_id": None,
                                "threshold_value": None,
                                "status": None,
                                "fallback_responses": {
                                    "id": None,
                                    "mode_id": None,
                                    "responses": [
                                        {
                                            "name": None,
                                            "resp_content": None,
                                            "resp_type_id": None,
                                            "custom_action_id": None
                                        }
                                    ]
                                }
                            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_002 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "threshold_value": None,
                                  "status": None,
                                  "fallback_responses": {
                                    "id": None,
                                    "mode_id": None,
                                    "responses": [
                                      {
                                        "name": None,
                                        "resp_content": None,
                                        "resp_type_id": None,
                                        "custom_action_id": None
                                      }
                                    ]
                                  }
                                }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_003 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "threshold_value": 0.6,
                                  "status": None,
                                  "fallback_responses": {
                                    "id": None,
                                    "mode_id": None,
                                    "responses": [
                                      {
                                        "name": None,
                                        "resp_content": None,
                                        "resp_type_id": None,
                                        "custom_action_id": None}
                                    ]
                                  }
                                }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_004 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "threshold_value": 0.6,
                                  "status": 1,
                                  "fallback_responses": {
                                    "id": None,
                                    "mode_id": None,
                                    "responses": [
                                      {
                                        "name": None,
                                        "resp_content": None,
                                        "resp_type_id": None,
                                        "custom_action_id": None}
                                    ]
                                  }
                                }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_005 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "threshold_value": 0.6,
                                  "status": 0,
                                  "fallback_responses": {
                                    "id": None,
                                    "mode_id": None,
                                    "responses": [
                                      {
                                        "name": None,
                                        "resp_content": None,
                                        "resp_type_id": None,
                                        "custom_action_id": None}
                                    ]
                                  }
                                }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_006 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "threshold_value": 0.6,
                                  "status": 1,
                                  "fallback_responses": {
                                    "id": get_int(2),
                                    "mode_id": None,
                                    "responses": [
                                      {
                                        "name": None,
                                        "resp_content": None,
                                        "resp_type_id": None,
                                        "custom_action_id": None}
                                    ]
                                  }
                                }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_007 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": None,
                        "resp_content": None,
                        "resp_type_id": None,
                        "custom_action_id": None}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_008 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": None,
                        "resp_type_id": None,
                        "custom_action_id": None}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_009 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": None,
                        "custom_action_id": None}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_010 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": None}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_011 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_012 = [{
            "agent_id": get_int(10),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_013 = [{
            "agent_id": "123dhjkashdkhkauw222)(*&^%$#@!",
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_014 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 1.22,
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_015 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": get_str(4),
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_016 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": get_int(4),
            "status": 1,
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_017 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": get_int(4),
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==200', '"(pymysql.err.DataError) (1406," in res["msg"]'], {}]
        self.update_config_018 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": get_str(4),
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_019 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": "ashdjkhajkqi12345!@#$%%^^())",
            "fallback_responses": {
                "id": get_int(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_020 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": get_str(2),
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_021 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": "123123FFqasgdashdghadj!@#$%^&**()",
                "mode_id": 1,
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_022 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": get_int(4),
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_023 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": get_str(4),
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_024 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": "12313weqweqweqwad!@#$%^&*",
                "responses": [
                    {
                        "name": "test",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_025 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_026 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_int(4),
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_027 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": "123123qweqweasdhghsjkfh!@#$%^&*()",
                        "resp_content": "test",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==200', '"(pymysql.err.DataError) (1406," in res["msg"]'], {}]
        self.update_config_028 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_029 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_int(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, [], {}]
        self.update_config_030 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": "1231dadasdad!@#$^%&**()!@#!@",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_031 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_032 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": get_str(4),
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_033 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": get_int(4),
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_034 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": "2312312djadhkahgfashdakh!@#^$&*%((#",
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_035 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": get_int(4)}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_036 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": get_str(4)}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_037 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": "123123asdjgjfkalshdlahl!@#$%&^((("}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_038 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1},{
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1},{
                        "name": get_int(1024),
                        "resp_content": get_int(1024),
                        "resp_type_id": 1,
                        "custom_action_id": 1},{
                        "name": get_int(2048),
                        "resp_content": get_int(2048),
                        "resp_type_id": 1,
                        "custom_action_id": 1},{
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1},{
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1},{
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1},{
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==200', '"(pymysql.err.DataError) (1406," in res["msg"]'], {}]
        self.update_config_039 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(1024),
                        "resp_content": get_int(1024),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(2048),
                        "resp_content": get_int(2048),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(128),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==200', '"(pymysql.err.DataError) (1406," in res["msg"]'], {}]
        self.update_config_040 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(1024),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(2048),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}, {
                        "name": get_int(64),
                        "resp_content": get_int(128),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==200', '"(pymysql.err.DataError) (1406," in res["msg"]'], {}]
        self.update_config_041 = [{
            "agent_id": "",
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_042 = [{
            "agent_id": " ",
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_043 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": "",
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_044 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": " ",
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_045 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": "",
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_046 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": " ",
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_047 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": "",
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_048 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": " ",
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_049 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": "",
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_050 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": " ",
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_051 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": "",
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_052 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": " ",
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_053 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": "",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_054 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": " ",
                        "resp_type_id": 1,
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==0', 'res["msg"]=="兜底策略更新成功"'], {}]
        self.update_config_055 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": "",
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_056 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": " ",
                        "custom_action_id": 1}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_057 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": ""}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.update_config_058 = [{
            "agent_id": os.environ.get("agent_id"),
            "threshold_value": 0.6,
            "status": 1,
            "fallback_responses": {
                "id": 1,
                "mode_id": 1,
                "responses": [
                    {
                        "name": get_str(4),
                        "resp_content": get_str(4),
                        "resp_type_id": 1,
                        "custom_action_id": " "}
                ]
            }
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]