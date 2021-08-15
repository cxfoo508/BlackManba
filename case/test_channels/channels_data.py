# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : channels_data.py
# DATE : 2021/7/27 13:58
import os
from data.data_method import *





class channels_data_class:

    def __init__(self):

        """
        渠道参数
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
        os.environ["user_id"] = "19910928"
        """
        获取渠道信息参数
        """
        self.param_get_detail_001 = [{
                              "agent_id": None,
                              "channel_type": None
                            }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_get_detail_002 = [{
            "agent_id": 1,
            "channel_type": None
        }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_get_detail_003 = [{
            "agent_id": 1,
            "channel_type": 1
        }, ['res["code"]==0', 'res["data"]==None'], {}]
        self.param_get_detail_004 = [{
            "agent_id": get_int(10),
            "channel_type": 1
        }, ['res["code"]==0', 'res["data"]==None'], {}]
        self.param_get_detail_005 = [{
            "agent_id": get_str(10),
            "channel_type": 1
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_detail_006 = [{
            "agent_id": "shjglahkdjlaklk!@#$$%%^&**(()__13144asd",
            "channel_type": 1
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_detail_007 = [{
            "agent_id": "",
            "channel_type": 1
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_detail_008 = [{
            "agent_id": " ",
            "channel_type": 1
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_detail_009 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": 0
        }, ['res["code"]==10007', 'res["msg"]=="获取渠道信息失败"'], {}]
        self.param_get_detail_010 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": get_int(10)
        }, ['res["code"]==0', 'res["data"]==None'], {}]
        self.param_get_detail_011 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": get_str(4)
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_detail_012 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": "ssshjh!@#$%^&*()_+}{></"
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_detail_013 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": ""
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_detail_014 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": " "
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_detail_015 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": 1
        }, ['res["code"]==0', 'res["data"]["channel_type"]==1'], {}]
        self.param_get_detail_016 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": 2
        }, ['res["code"]==0', 'res["data"]["channel_type"]==2'], {}]
        self.param_get_detail_017 = [{
            "agent_id": os.environ.get("agent_id"),
            "channel_type": 3
        }, ['res["code"]==0', 'res["data"]["channel_type"]==3'],
            {"account_key": 'res["data"]["account_key"]', "account_secret": 'res["data"]["account_secret"]'}]

        """
        获取渠道全鉴token参数
        """
        self.param_get_auth_001 = [{
                      "auth_account_key": None,
                      "auth_nonce": None,
                      "auth_sign": None,
                      "auth_timestamp": None
                    }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_get_auth_002 = [{
            "auth_account_key": get_int(12),
            "auth_nonce": None,
            "auth_sign": None,
            "auth_timestamp": None
        }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_get_auth_003 = [{
            "auth_account_key": get_int(12),
            "auth_nonce": get_int(12),
            "auth_sign": None,
            "auth_timestamp": None
        }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_get_auth_004 = [{
            "auth_account_key": get_int(12),
            "auth_nonce": get_int(12),
            "auth_sign": get_int(12),
            "auth_timestamp": None
        }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_get_auth_005 = [{
            "auth_account_key": get_str(4),
            "auth_nonce": get_int(12),
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_006 = [{
            "auth_account_key": "12345hjsdgkgha~!@#$$%%^&**(())_+",
            "auth_nonce": get_int(12),
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_007 = [{
            "auth_account_key": "",
            "auth_nonce": get_int(12),
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_008 = [{
            "auth_account_key": " ",
            "auth_nonce": get_int(12),
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_009 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce": get_int(12),
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_010 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce": get_str(12),
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_011 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce": "123wgdajkglasjld!@#$%^&*(((!>><?",
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_012 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce": "",
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_013 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce": " ",
            "auth_sign": get_int(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_014 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce":  os.environ.get("auth_nonce"),
            "auth_sign": get_str(12),
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_015 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce":  os.environ.get("auth_nonce"),
            "auth_sign": "asdfghalsghhakh!@#~$%^&*()_+?>:",
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_016 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce":  os.environ.get("auth_nonce"),
            "auth_sign": "",
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_017 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce":  os.environ.get("auth_nonce"),
            "auth_sign": " ",
            "auth_timestamp": get_int(12)
        }, ['res["code"]==10007', 'res["msg"]=="渠道token生成失败"'], {}]
        self.param_get_auth_018 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce":  os.environ.get("auth_nonce"),
            "auth_sign":  os.environ.get("auth_sign"),
            "auth_timestamp": get_str(12)
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_auth_019 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce":  os.environ.get("auth_nonce"),
            "auth_sign":  os.environ.get("auth_sign"),
            "auth_timestamp": "asdfghalsghhakh!@#~$%^&*()_+?>:",
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_auth_020 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce":  os.environ.get("auth_nonce"),
            "auth_sign":  os.environ.get("auth_sign"),
            "auth_timestamp": "",
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_auth_021 = [{
            "auth_account_key":  os.environ.get("auth_account_key"),
            "auth_nonce":  os.environ.get("auth_nonce"),
            "auth_sign":  os.environ.get("auth_sign"),
            "auth_timestamp": " ",
        }, ['res["detail"][0]["msg"]=="value is not a valid integer"'], {}]
        self.param_get_auth_022 = [{
            "auth_account_key": os.environ.get("auth_account_key"),
            "auth_nonce": os.environ.get("auth_nonce"),
            "auth_sign": os.environ.get("auth_sign"),
            "auth_timestamp": os.environ.get("auth_timestamp"),
        }, ['res["code"]==0', 'res["msg"]=="渠道token生成成功"'], {'access_token': 'res["data"]["access_token"]'}]

        """
        创建渠道用户参数
        """
        self.param_create_user_001 = [{
              "user_id": None,
              "avatar_url": None,
              "nickname": None
            }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_create_user_002 = [{
            "user_id": get_int(3),
            "avatar_url": None,
            "nickname": None
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_003 = [{
            "user_id": get_int(3),
            "avatar_url": get_int(3),
            "nickname": None
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_004 = [{
            "user_id": get_int(3),
            "avatar_url": get_int(3),
            "nickname": get_int(3)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_005 = [{
            "user_id": get_str(4),
            "avatar_url": get_int(3),
            "nickname": get_int(3)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_006 = [{
            "user_id": "asdfghalsghhakh!@#~$%^&*()_+?>:",
            "avatar_url": get_int(3),
            "nickname": get_int(3)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_007 = [{
            "user_id": "",
            "avatar_url": get_int(3),
            "nickname": get_int(3)
        }, ['res["code"]==10004', 'res["msg"]=="创建用户失败"'], {}]
        self.param_create_user_008 = [{
            "user_id": " ",
            "avatar_url": get_int(3),
            "nickname": get_int(3)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_009 = [{
            "user_id": get_int(10),
            "avatar_url": get_str(3),
            "nickname": get_int(3)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_010 = [{
            "user_id": os.environ.get("user_id"),
            "avatar_url": "asdfghalsghhakh!@#~$%^&*()_+?>:",
            "nickname": get_int(3)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_011 = [{
            "user_id": get_int(10),
            "avatar_url": "",
            "nickname": get_int(3)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_012 = [{
            "user_id": get_int(10),
            "avatar_url": " ",
            "nickname": get_int(3)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_013 = [{
            "user_id": get_int(10),
            "avatar_url": get_str(5),
            "nickname": get_str(4)
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_014 = [{
            "user_id": get_int(10),
            "avatar_url": get_str(5),
            "nickname": "asdfghalsghhakh!@#~$%^&*()_+?>:"
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_015 = [{
            "user_id": get_int(10),
            "avatar_url": get_str(5),
            "nickname": ""
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_016 = [{
            "user_id": get_int(10),
            "avatar_url": get_str(5),
            "nickname": " "
        }, ['res["code"]==0', 'res["msg"]=="创建用户成功"'], {}]
        self.param_create_user_017 = [{
            "user_id": None,
            "avatar_url": "https://laiye.com/",
            "nickname": get_str(6)
        }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_create_user_018 = [{
            "user_id": get_int(2048),
            "avatar_url": get_int(2048),
            "nickname": get_int(2048)
        }, ['res["code"]==200', 'res["msg"]=="Argument False expected to be of bytearray, bytes, float, int, or str type"'], {}]

        """
        查询渠道用户信息参数
        """
        self.param_get_user_001 = [{
              "user_id": None
            }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_get_user_002 = [{
            "user_id": get_int(10)
        }, ['res["code"]==10007', 'res["msg"]=="获取用户信息失败"'], {}]
        self.param_get_user_003 = [{
            "user_id": get_str(4)
        }, ['res["code"]==10007', 'res["msg"]=="获取用户信息失败"'], {}]
        self.param_get_user_004 = [{
            "user_id": "~!!@#$$%^^&**()__+:>?>>string"
        }, ['res["code"]==10007', 'res["msg"]=="获取用户信息失败"'], {}]
        self.param_get_user_005 = [{
            "user_id": ""
        }, ['res["code"]==10007', 'res["msg"]=="获取用户信息失败"'], {}]
        self.param_get_user_006 = [{
            "user_id": " "
        }, ['res["code"]==0', 'res["msg"]=="获取用户信息成功"'], {}]
        self.param_get_user_007 = [{
            "user_id": os.environ.get("user_id")
        }, ['res["code"]==0', 'res["msg"]=="获取用户信息成功"'], {}]

        """
        机器人对话回复参数
        """
        self.param_get_response_001 = [{
              "user_id": None,
              "msg_body": {
                "text": {
                  "content": None
                }
              }
            }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]
        self.param_get_response_002 = [{
            "user_id": get_int(10),
            "msg_body": {
                "text": {
                    "content": None
                }
            }
        }, ['res["code"]==200', '"object is not subscriptable" in res["msg"]'], {}]
        self.param_get_response_003 = [{
            "user_id": get_int(10),
            "msg_body": {
                "text": {
                    "content": get_int(10)
                }
            }
        }, ['res["code"]==0', 'res["msg"]=="获取机器人回复成功"'], {}]
        self.param_get_response_004 = [{
            "user_id": get_str(10),
            "msg_body": {
                "text": {
                    "content": get_int(10)
                }
            }
        }, ['res["code"]==0', 'res["msg"]=="获取机器人回复成功"'], {}]
        self.param_get_response_005 = [{
            "user_id": "~!!@#$$%^^&**()__+:>?>>string",
            "msg_body": {
                "text": {
                    "content": get_int(10)
                }
            }
        }, ['res["code"]==0', 'res["msg"]=="获取机器人回复成功"'], {}]
        self.param_get_response_006 = [{
            "user_id": "",
            "msg_body": {
                "text": {
                    "content": get_int(10)
                }
            }
        }, ['res["code"]==10007', 'res["msg"]=="获取机器人回复失败"'], {}]
        self.param_get_response_007 = [{
            "user_id": " ",
            "msg_body": {
                "text": {
                    "content": get_int(10)
                }
            }
        }, ['res["code"]==200', 'res["data"]==None'], {}]
        self.param_get_response_008 = [{
            "user_id": os.environ.get("user_id"),
            "msg_body": {
                "text": {
                    "content": get_str(4)
                }
            }
        }, ['res["code"]==0', 'res["msg"]=="获取机器人回复成功"'], {}]
        self.param_get_response_009 = [{
            "user_id": os.environ.get("user_id"),
            "msg_body": {
                "text": {
                    "content": "~!!@#$$%^^&**()__+:>?>>string"
                }
            }
        }, ['res["code"]==0', 'res["msg"]=="获取机器人回复成功"'], {}]
        self.param_get_response_010 = [{
            "user_id": os.environ.get("user_id"),
            "msg_body": {
                "text": {
                    "content": ""
                }
            }
        }, ['res["code"]==0', 'res["msg"]=="获取机器人回复成功"'], {}]
        self.param_get_response_011 = [{
            "user_id": os.environ.get("user_id"),
            "msg_body": {
                "text": {
                    "content": " "
                }
            }
        }, ['res["code"]==0', 'res["msg"]=="获取机器人回复成功"'], {}]
        self.param_get_response_012 = [{
            "user_id": os.environ.get("user_id"),
            "msg_body": {
                "text": {
                    "content": get_str(4)
                }
            }
        }, ['res["code"]==0', 'res["msg"]=="获取机器人回复成功"'], {}]
        self.param_get_response_013 = [{
            "user_id": None,
            "msg_body": {
                "text": {
                    "content": get_str(4)
                }
            }
        }, ['res["detail"][0]["msg"]=="none is not an allowed value"'], {}]