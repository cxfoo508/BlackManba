# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : channels_data.py
# DATE : 2021/8/6 18:29
import os
from data.data_method import *


class channels_data_new_class:

    def __init__(self):
        # <editor-fold desc="初始化及收尾参数列表">

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

        # </editor-fold>
        # <editor-fold desc="">
        # </editor-fold>
        # <editor-fold desc="新增渠道">
        self.param_create_channels_001 = [{"agent_id":None,
                                        "data":{
                                        "operations": [
                                                    {
                                                    "create": {
                                                        "id": None,
                                                        "channel_name": None,
                                                        "channel_description": None,
                                                        "channel_type": None,
                                                        "open_api": {
                                                            "send_webhook": None,
                                                            "pre_webhook": None,
                                                            "post_webhook": None
                                                        }
                                                      }
                                                    }
                                                  ]
                                                }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_002 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 10', 'res["message"] == "缺少渠道名称"'
], {}]
        self.param_create_channels_003 = [{"agent_id": None,
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": 1,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_004 = [{"agent_id": None,
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_005 = [{"agent_id": None,
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": get_str(123),
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_006 = [{"agent_id": None,
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_007 = [{"agent_id": None,
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_008 = [{"agent_id": None,
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_009 = [{"agent_id": None,
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_010 = [{"agent_id": "",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": "",
                                                           "channel_name": "",
                                                           "channel_description": "",
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_011 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": "",
                                                           "channel_name": "",
                                                           "channel_description": "",
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_012 = [{"agent_id": "",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": 1,
                                                           "channel_name": "",
                                                           "channel_description": "",
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_013 = [{"agent_id": "",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": "",
                                                           "channel_name": get_str(4),
                                                           "channel_description": "",
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_014 = [{"agent_id": "",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": "",
                                                           "channel_name": "",
                                                           "channel_description": get_str(123),
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_015 = [{"agent_id": "",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": "",
                                                           "channel_name": "",
                                                           "channel_description": "",
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_016 = [{"agent_id": "",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": "",
                                                           "channel_name": "",
                                                           "channel_description": "",
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_017 = [{"agent_id": "",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": "",
                                                           "channel_name": "",
                                                           "channel_description": "",
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_018 = [{"agent_id": "",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": "",
                                                           "channel_name": "",
                                                           "channel_description": "",
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_019 = [{"agent_id": " ",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": " ",
                                                           "channel_description": " ",
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": " ",
                                                               "pre_webhook": " ",
                                                               "post_webhook": " "
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_020 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": " ",
                                                           "channel_description": " ",
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": " ",
                                                               "pre_webhook": " ",
                                                               "post_webhook": " "
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_021 = [{"agent_id": " ",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": 1,
                                                           "channel_name": " ",
                                                           "channel_description": " ",
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": " ",
                                                               "pre_webhook": " ",
                                                               "post_webhook": " "
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for enum type" in res["message"]'], {}]
        self.param_create_channels_022 = [{"agent_id": " ",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": get_str(4),
                                                           "channel_description": " ",
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": " ",
                                                               "pre_webhook": " ",
                                                               "post_webhook": " "
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_023 = [{"agent_id": " ",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": " ",
                                                           "channel_description": get_str(123),
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": " ",
                                                               "pre_webhook": " ",
                                                               "post_webhook": " "
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_024 = [{"agent_id": " ",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": " ",
                                                           "channel_description": " ",
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": " ",
                                                               "pre_webhook": " ",
                                                               "post_webhook": " "
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_025 = [{"agent_id": " ",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": " ",
                                                           "channel_description": " ",
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": " ",
                                                               "post_webhook": " "
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_026 = [{"agent_id": " ",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": " ",
                                                           "channel_description": " ",
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": " ",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": " "
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_027 = [{"agent_id": " ",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": " ",
                                                           "channel_description": " ",
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": " ",
                                                               "pre_webhook": " ",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_028 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["channel"]["id"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'],
                                          {'id':'res["channel"]["id"]'}]
        self.param_create_channels_029 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "UNSPECIFIED",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "UNSPECIFIED"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com"'],
                                          {'id':'res["channel"]["id"]'}]
        self.param_create_channels_030 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "OPENAPI",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["channel"]["id"] is not None', 'res["channel"]["channelType"] == "OPENAPI"'],
                                          {'id':'res["channel"]["id"]'}]
        self.param_create_channels_031 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": get_str(4),
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for enum type" in res["message"]'], {}]
        self.param_create_channels_032 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": get_int(5),
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, [], {}]
        self.param_create_channels_033 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for enum type" in res["message"]'], {}]
        self.param_create_channels_034 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for enum type" in res["message"]'], {}]
        self.param_create_channels_035 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": " ",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for enum type" in res["message"]'], {}]
        self.param_create_channels_036 = [{"agent_id": get_str(4),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_037 = [{"agent_id": get_int(10),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["channel"]["id"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_038 = [{"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_039 = [{"agent_id": "",
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_create_channels_040 = [{"agent_id": " ",
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_create_channels_041 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": get_str(4),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_042 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": get_int(10),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"]["id"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_043 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_044 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": "",
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_045 = [{"agent_id": os.environ.get("agent_id"),
                                           "data":{
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": " ",
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_create_channels_046 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(64),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"]["id"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_047 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(121),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 10', 'res["message"] == "渠道名称超过64字符！"'
], {}]
        self.param_create_channels_048 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"]["id"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_049 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": "",
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 10', 'res["message"] == "缺少渠道名称"'], {}]
        self.param_create_channels_050 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": " ",
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 10', 'res["message"] == "缺少渠道名称"'], {}]
        self.param_create_channels_051 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(256),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_052 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": str(get_int(257)),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 10', 'res["message"] == "渠道描述内容超过256字符！"'], {}]
        self.param_create_channels_053 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelDescription"] == "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"'], {}]
        self.param_create_channels_054 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": "",
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelDescription"] == ""'], {}]
        self.param_create_channels_055 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": " ",
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelDescription"] == ""'], {}]
        self.param_create_channels_056 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": get_str(4),
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_057 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_int(10),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'], {}]
        self.param_create_channels_058 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == ""'], {}]
        self.param_create_channels_059 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == ""'], {}]
        self.param_create_channels_060 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": get_str(256),
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_061 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": get_str(4),
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_062 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": get_int(10),
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'], {}]
        self.param_create_channels_063 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_064 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["preWebhook"] == ""'], {}]
        self.param_create_channels_065 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": " ",
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["preWebhook"] == ""'], {}]
        self.param_create_channels_066 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": get_str(256),
                                                             "post_webhook": "www.baidu.com"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_067 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": get_str(4)
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_068 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": get_int(10)
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'], {}]
        self.param_create_channels_069 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": get_str(256)
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_070 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"'], {}]
        self.param_create_channels_071 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["postWebhook"] == ""'], {}]
        self.param_create_channels_072 = [{"agent_id": os.environ.get("agent_id"),
                                         "data":{
                                             "operations": [
                                                 {
                                                     "create": {
                                                         "id": None,
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com",
                                                             "pre_webhook": "www.baidu.com",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["postWebhook"] == ""'], {}]
        self.param_create_channels_073 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {
                                               "operations": [
                                                   {
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   },{
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "OPENAPI",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   },{
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "UNSPECIFIED",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   },{
                                                       "create": {
                                                           "id": get_int(10),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   },{
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(588),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   },{
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": get_int(10),
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   },{
                                                       "create": {
                                                           "id": get_int(2),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   },{
                                                       "create": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com",
                                                               "pre_webhook": "www.baidu.com",
                                                               "post_webhook": "www.baidu.com"
                                                           }
                                                       }
                                                   }

                                               ]
                                           }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com"'], {}]



        # </editor-fold>

        # <editor-fold desc="更新渠道">
        self.param_update_channels_001 = [{"agent_id": None,
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'
], {}]
        self.param_update_channels_002 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["channel"] == None'], {}]
        self.param_update_channels_003 = [{"agent_id": None,
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": os.environ.get("id"),
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'
], {}]
        self.param_update_channels_004 = [{"agent_id": None,
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'
], {}]
        self.param_update_channels_005 = [{"agent_id": None,
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": get_str(123),
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'
], {}]
        self.param_update_channels_006 = [{"agent_id": None,
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'
], {}]
        self.param_update_channels_007 = [{"agent_id": None,
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": None,
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'
], {}]
        self.param_update_channels_008 = [{"agent_id": None,
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": None
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'
], {}]
        self.param_update_channels_009 = [{"agent_id": None,
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": None,
                                                           "channel_description": None,
                                                           "channel_type": None,
                                                           "open_api": {
                                                               "send_webhook": None,
                                                               "pre_webhook": None,
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'
], {}]
        self.param_update_channels_010 = [{"agent_id": "",
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": "",
                                                           "channel_name": "",
                                                           "channel_description": "",
                                                           "channel_type": "",
                                                           "open_api": {
                                                               "send_webhook": "",
                                                               "pre_webhook": "",
                                                               "post_webhook": ""
                                                           }
                                                       }
                                                   }
                                               ]
                                           }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_update_channels_011 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "",
                                                         "channel_name": "",
                                                         "channel_description": "",
                                                         "channel_type": "",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_012 = [{"agent_id": "",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": "",
                                                         "channel_description": "",
                                                         "channel_type": "",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_update_channels_013 = [{"agent_id": "",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "",
                                                         "channel_name": get_str(4),
                                                         "channel_description": "",
                                                         "channel_type": "",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_update_channels_014 = [{"agent_id": "",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "",
                                                         "channel_name": "",
                                                         "channel_description": get_str(123),
                                                         "channel_type": "",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_update_channels_015 = [{"agent_id": "",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "",
                                                         "channel_name": "",
                                                         "channel_description": "",
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_update_channels_016 = [{"agent_id": "",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "",
                                                         "channel_name": "",
                                                         "channel_description": "",
                                                         "channel_type": "",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_update_channels_017 = [{"agent_id": "",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "",
                                                         "channel_name": "",
                                                         "channel_description": "",
                                                         "channel_type": "",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_update_channels_018 = [{"agent_id": "",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "",
                                                         "channel_name": "",
                                                         "channel_description": "",
                                                         "channel_type": "",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_update_channels_019 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": " ",
                                                         "channel_description": " ",
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": " ",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_020 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": " ",
                                                         "channel_description": " ",
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": " ",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_021 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": " ",
                                                         "channel_description": " ",
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": " ",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for enum type" in res["message"]'], {}]
        self.param_update_channels_022 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": get_str(4),
                                                         "channel_description": " ",
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": " ",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_023 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": " ",
                                                         "channel_description": get_str(123),
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": " ",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_024 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": " ",
                                                         "channel_description": " ",
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": " ",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_025 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": " ",
                                                         "channel_description": " ",
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": " ",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_026 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": " ",
                                                         "channel_description": " ",
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_027 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": " ",
                                                         "channel_description": " ",
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": " ",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_028 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_029 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "UNSPECIFIED",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "UNSPECIFIED"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_030 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "OPENAPI",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "OPENAPI"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_031 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": get_str(4),
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for enum type" in res["message"]'], {}]
        self.param_update_channels_032 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": get_int(5),
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, [], {}]
        self.param_update_channels_033 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for enum type" in res["message"]'
], {}]
        self.param_update_channels_034 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for enum type" in res["message"]'
], {}]
        self.param_update_channels_035 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": " ",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"invalid value for enum type" in res["message"]'
], {}]
        self.param_update_channels_036 = [{"agent_id": get_str(4),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_update_channels_037 = [{"agent_id": get_int(10),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is None'], {}]
        self.param_update_channels_038 = [{"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'
], {}]
        self.param_update_channels_039 = [{"agent_id": "",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 5', 'res["message"] == "Not Found"'
], {}]
        self.param_update_channels_040 = [{"agent_id": " ",
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_update_channels_041 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": get_str(4),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_042 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": get_int(10),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] == None'], {}]
        self.param_update_channels_043 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_044 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": "",
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_045 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": " ",
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for int64 type" in res["message"]'], {}]
        self.param_update_channels_046 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": str(get_int(64)),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_047 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": str(get_int(66)),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 10 ', 'res["message"] == "渠道名称超过64字符！"'], {}]
        self.param_update_channels_048 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 10', 'res["message"] == "渠道名称重复！"'], {}]
        self.param_update_channels_049 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": "",
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, [], {}]
        self.param_update_channels_050 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": " ",
                                                         "channel_description": get_str(256),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, [], {}]
        self.param_update_channels_051 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(256),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_052 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": str(get_int(257)),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 10', 'res["message"] == "渠道描述内容超过256字符！"'], {}]
        self.param_update_channels_053 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["channelDescription"] == "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"'], {}]
        self.param_update_channels_054 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": "",
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_055 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": " ",
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_056 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": get_str(4),
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["preWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_057 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_int(10),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'
], {}]
        self.param_update_channels_058 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == ""'], {}]
        self.param_update_channels_059 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": " ",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == ""'], {}]
        self.param_update_channels_060 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": get_int(256),
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'
], {}]
        self.param_update_channels_061 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": get_str(4),
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_062 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": get_int(10),
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'
], {}]
        self.param_update_channels_063 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["preWebhook"] == "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"'], {}]
        self.param_update_channels_064 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["preWebhook"] == ""'], {}]
        self.param_update_channels_065 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": " ",
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["preWebhook"] == ""'], {}]
        self.param_update_channels_066 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": get_int(256),
                                                             "post_webhook": "www.baidu.com_new"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'], {}]
        self.param_update_channels_067 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": get_str(4)
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["sendWebhook"] == "www.baidu.com_new"'], {}]
        self.param_update_channels_068 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": get_int(10)
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'], {}]
        self.param_update_channels_069 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": get_int(256)
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for string type" in res["message"]'], {}]
        self.param_update_channels_070 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["postWebhook"] == "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"'], {}]
        self.param_update_channels_071 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["postWebhook"] == ""'], {}]
        self.param_update_channels_072 = [{"agent_id": os.environ.get("agent_id"),
                                         "data": {
                                             "operations": [
                                                 {
                                                     "update": {
                                                         "id": os.environ.get("id"),
                                                         "channel_name": get_str(4),
                                                         "channel_description": get_str(121),
                                                         "channel_type": "CUSTOM",
                                                         "open_api": {
                                                             "send_webhook": "www.baidu.com_new",
                                                             "pre_webhook": "www.baidu.com_new",
                                                             "post_webhook": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }}, ['res["channel"] is not None', 'res["channel"]["channelType"] == "CUSTOM"', 'res["channel"]["openApi"]["postWebhook"] == ""'], {}]
        self.param_update_channels_073 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {
                                               "operations": [
                                                   {
                                                       "update": {
                                                           "id": os.environ.get("id"),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": None,
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "OPENAPI",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": os.environ.get("id"),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "UNSPECIFIED",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": get_int(10),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": os.environ.get("id"),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(588),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": os.environ.get("id"),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": get_int(10),
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": get_int(2),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": os.environ.get("id"),
                                                           "channel_name": get_str(78),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": os.environ.get("id"),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }, {
                                                       "update": {
                                                           "id": os.environ.get("id"),
                                                           "channel_name": get_str(4),
                                                           "channel_description": get_str(121),
                                                           "channel_type": "CUSTOM",
                                                           "open_api": {
                                                               "send_webhook": "www.baidu.com_new",
                                                               "pre_webhook": "www.baidu.com_new",
                                                               "post_webhook": "www.baidu.com_new"
                                                           }
                                                       }
                                                   }

                                               ]
                                           }}, ['res["code"] == 3', '"proto:" in res["message"]',  '"invalid value for enum type" in res["message"]'], {}]
        # </editor-fold>

        # <editor-fold desc="删除渠道">
        self.param_delete_channels_001 = [{"agent_id": None,
                                           "data":{"operations": [
                                                {
                                                    "delete": None
                                                }]}}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_delete_channels_002 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {"operations": [
                                               {
                                                   "delete": None
                                               }]}}, ['res["channel"] == None'], {}]
        self.param_delete_channels_003 = [{"agent_id": None,
                                           "data": {"operations": [
                                               {
                                                   "delete": os.environ.get("id")
                                               }]}}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_delete_channels_004 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {"operations": [
                                               {
                                                   "delete": os.environ.get("id")
                                               }]}}, ['res["channel"]["id"] == "1"'], {}]
        self.param_delete_channels_005 = [{"agent_id": "",
                                           "data": {"operations": [
                                               {
                                                   "delete": ""
                                               }]}}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_delete_channels_006 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {"operations": [
                                               {
                                                   "delete": ""
                                               }]}}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_delete_channels_007 = [{"agent_id": "",
                                           "data": {"operations": [
                                               {
                                                   "delete": os.environ.get("id")
                                               }]}}, ['res["code"] == 5', 'res["message"] == "Not Found"'
], {}]
        self.param_delete_channels_008 = [{"agent_id": " ",
                                           "data": {"operations": [
                                               {
                                                   "delete": " "
                                               }]}}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_delete_channels_009 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {"operations": [
                                               {
                                                   "delete": " "
                                               }]}}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_delete_channels_010 = [{"agent_id": " ",
                                           "data": {"operations": [
                                               {
                                                   "delete": os.environ.get("id")
                                               }]}}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_delete_channels_011 = [{"agent_id": get_str(4),
                                           "data": {"operations": [
                                               {
                                                   "delete": os.environ.get("id")
                                               }]}}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_delete_channels_012 = [{"agent_id": get_int(10),
                                           "data": {"operations": [
                                               {
                                                   "delete": os.environ.get("id")
                                               }]}}, ['res["channel"] == None'], {}]
        self.param_delete_channels_013 = [{"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                           "data": {"operations": [
                                               {
                                                   "delete": os.environ.get("id")
                                               }]}}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_delete_channels_014 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {"operations": [
                                               {
                                                   "delete": get_str(4)
                                               }]}}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]
        self.param_delete_channels_015 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {"operations": [
                                               {
                                                   "delete": get_int(10)
                                               }]}}, ['res["channel"] == None'], {}]
        self.param_delete_channels_016 = [{"agent_id": os.environ.get("agent_id"),
                                           "data": {"operations": [
                                               {
                                                   "delete": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                               }]}}, ['res["code"] == 3', '"invalid value for int64 type" in res["message"]'], {}]



        # </editor-fold>

        # <editor-fold desc="获取渠道">
        self.param_get_channels_001 = [{"agent_id":None,
                                        "id":None}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_get_channels_002 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": None}, ['res["code"] == 3', '"type mismatch, parameter: id, error:" in res["message"]'], {}]
        self.param_get_channels_003 = [{"agent_id": None,
                                        "id": os.environ.get("id")}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_get_channels_004 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": os.environ.get("id")}, ['res["channel"]["id"] == os.environ.get("id")'], {}]
        self.param_get_channels_005 = [{"agent_id": "",
                                         "id": ""}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_get_channels_006 = [{"agent_id": "",
                                        "id": os.environ.get("id")}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_get_channels_007 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": ""}, ['res["code"] == 3', '"type mismatch, parameter: id, error:" in res["message"]'], {}]
        self.param_get_channels_008 = [{"agent_id": " ",
                                       "id": os.environ.get("id")}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_get_channels_009 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": " "}, ['res["code"] == 3', '"type mismatch, parameter: id, error:" in res["message"]'], {}]
        self.param_get_channels_010 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"}, ['res["code"] == 3', '"type mismatch, parameter: id, error:" in res["message"]'], {}]
        self.param_get_channels_011 = [{"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                        "id": os.environ.get("id")}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_get_channels_012 = [{"agent_id": get_str(4),
                                        "id": os.environ.get("id")}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_get_channels_013 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": get_str(4)}, ['res["code"] == 3', '"type mismatch, parameter: id, error:" in res["message"]'], {}]
        self.param_get_channels_014 = [{"agent_id": get_int(10),
                                        "id": os.environ.get("id")}, ['res["channel"] == None'], {}]
        self.param_get_channels_015 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": get_int(10)}, ['res["channel"] == None'], {}]
        self.param_get_channels_016 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": os.environ.get("id")}, ['res["channel"]["id"] == os.environ.get("id")'], {}]
        self.param_get_channels_017 = [{"agent_id": os.environ.get("agent_id"),
                                        "id": os.environ.get("id")}, ['res["channel"] is None'], {}]
        # </editor-fold>

        # <editor-fold desc="获取渠道列表">
        self.param_get_channelslist_001 = [{"agent_id":None,
                                             "page":None,
                                            "pageSize":None}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_get_channelslist_002 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": None,
                                             "pageSize": None}, ['res["code"] == 3', '"page" in res["message"]',  '"parsing field" in res["message"]'], {}]
        self.param_get_channelslist_003 = [{"agent_id": None,
                                             "page": 1,
                                             "pageSize": None}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_get_channelslist_004 = [{"agent_id": None,
                                             "page": None,
                                             "pageSize": 14}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_get_channelslist_005 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": 1,
                                             "pageSize": None}, ['res["code"] == 3', '"page_size" in res["message"]',  '"parsing field" in res["message"]'], {}]
        self.param_get_channelslist_006 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": 1,
                                             "pageSize": 20}, ['res["channels"] is not None', 'len(res["channels"]) >= 1'], {}]
        self.param_get_channelslist_007 = [{"agent_id": "",
                                             "page": "",
                                             "pageSize": ""}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_get_channelslist_008 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": "",
                                             "pageSize": ""}, ['res["code"] == 3', '"page" in res["message"]',  '"parsing field" in res["message"]'], {}]
        self.param_get_channelslist_009 = [{"agent_id": "",
                                             "page": 1,
                                             "pageSize": ""}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_get_channelslist_010 = [{"agent_id": "",
                                             "page": "",
                                             "pageSize": 20}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_get_channelslist_011 = [{"agent_id": " ",
                                            "page": 1,
                                             "pageSize": 20}, ['res["code"] == 3', '"type mismatch, parameter: agent_id, error:" in res["message"]'], {}]
        self.param_get_channelslist_012 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": " ",
                                             "pageSize": 20}, ['res["code"] == 3', '"page" in res["message"]',  '"parsing field" in res["message"]'], {}]
        self.param_get_channelslist_013 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": 1,
                                             "pageSize": " "}, ['res["code"] == 3', '"page_size" in res["message"]',  '"parsing field" in res["message"]'], {}]
        self.param_get_channelslist_014 = [{"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                             "page": 1,
                                             "pageSize": 20}, ['res["code"] == 5', 'res["message"] == "Not Found"'], {}]
        self.param_get_channelslist_015 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                             "pageSize": 20}, ['res["code"] == 3', '"page" in res["message"]',  '"parsing field" in res["message"]'], {}]
        self.param_get_channelslist_016 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": 1,
                                             "pageSize": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"}, ['res["code"] == 3', '"page_size" in res["message"]',  '"parsing field" in res["message"]'], {}]
        self.param_get_channelslist_017 = [{"agent_id": get_int(10),
                                             "page": 1,
                                             "pageSize": 20}, ['res["channels"] == []'], {}]
        self.param_get_channelslist_018 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": get_int(10),
                                             "pageSize": 20}, ['res["channels"] == []'], {}]
        self.param_get_channelslist_019 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": 1,
                                             "pageSize": get_int(10)}, ['res["channels"] is not None', 'len(res["channels"]) >= 1'], {}]
        self.param_get_channelslist_020 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": 1,
                                             "pageSize": 20}, ['res["channels"] is not None', 'len(res["channels"]) >= 1'], {}]
        self.param_get_channelslist_021 = [{"agent_id": os.environ.get("agent_id"),
                                             "page": 1,
                                             "pageSize": 20}, ['res["channels"] is not None', 'len(res["channels"]) >= 1'], {}]
        # </editor-fold>