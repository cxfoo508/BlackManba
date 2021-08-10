# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : intents_data.py
# DATE : 2021/7/19 15:17
import os

from data_method import *

class intents_data_class:

    def __init__(self):
        """
        意图参数
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
        意图列表
        """
        self.param_list_001 = [{
                              "agent_id": None,
                              "search": {
                                "examples": None,
                                "intent_name":None
                              },
                              "filters": {
                                "intent_type": None,
                                "trigger_type": None,
                                "skill_type": None
                              },
                              "sort": {
                                "examples_count": None,
                                "update_time": None
                              },
                              "page_size": None,
                              "page_num": None
                            },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_002 = [{
                              "agent_id": os.environ.get("agent_id"),
                              "search": {
                                "examples": None,
                                "intent_name":None
                              },
                              "filters": {
                                "intent_type": None,
                                "trigger_type": None,
                                "skill_type": None
                              },
                              "sort": {
                                "examples_count": None,
                                "update_time": None
                              },
                              "page_size": None,
                              "page_num": None
                            },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_003 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": None
                                  },
                                  "filters": {
                                    "intent_type": None,
                                    "trigger_type": None,
                                    "skill_type": None
                                  },
                                  "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                  },
                                  "page_size": None,
                                  "page_num": None
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_004 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": None,
                                    "trigger_type": None,
                                    "skill_type": None
                                  },
                                  "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_005 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": None,
                                    "skill_type": None
                                  },
                                  "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_006 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": None
                                  },
                                  "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_007 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                  },
                                  "page_size": None,
                                  "page_num": None
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_008 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": None
                                  },
                                  "page_size": None,
                                  "page_num": None
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_009 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": None,
                                  "page_num": None
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_010 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": None
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_011 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'],{}]
        self.param_list_012 = [{
                                  "agent_id": get_str(4),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_013 = [{
                                  "agent_id": get_int(10),
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["total_num"]==0'],{}]
        self.param_list_014 = [{
                                  "agent_id": "",
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_015 = [{
                                  "agent_id": " ",
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_016 = [{
                                  "agent_id": "!@#$%^&**&^^*^%*((^%^*Dfhgsdhhkjahdjk123123",
                                  "search": {
                                    "examples": get_str(4),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'],{}]
        self.param_list_017 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": get_int(128),
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'],{}]
        self.param_list_018 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": "quwehjkhsdjk!@#$%^&*()_+12344561321",
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'],{}]
        self.param_list_019 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": "",
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'],{}]
        self.param_list_020 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": " ",
                                    "intent_name": get_str(4)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'],{}]
        self.param_list_021 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": "",
                                    "intent_name": get_int(128)
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'],{}]
        self.param_list_022 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": "",
                                    "intent_name": "1213123!@@##$$%^&&**(()(qesadhaashjk"
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'],{}]
        self.param_list_023 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": "",
                                    "intent_name": ""
                                  },
                                  "filters": {
                                    "intent_type": [],
                                    "trigger_type": [],
                                    "skill_type": []
                                  },
                                  "sort": {
                                    "examples_count": "ascend",
                                    "update_time": "ascend"
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'],{}]
        self.param_list_024 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": " "
            },
            "filters": {
                "intent_type": [],
                "trigger_type": [],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_025 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [get_str(4)],
                "trigger_type": [],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_026 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [get_int(4)],
                "trigger_type": [],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["total_num"]==0'], {}]
        self.param_list_027 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": ["1231231sghdhajkdhsajkkdh!@#$$%%^^&&&!%%"],
                "trigger_type": [],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_028 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [""],
                "trigger_type": [],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_029 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [" "],
                "trigger_type": [],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_030 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0,1,2],
                "trigger_type": [],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_031 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [get_int(10)],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["total_num"]==0'], {}]
        self.param_list_032 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [get_str(10)],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_033 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": ["12312asdjghajkk!@#$%^^&**(()))__"],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_034 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [""],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_035 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [" "],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_036 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": []
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_037 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [get_str(4)]
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_038 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [get_int(4)]
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_039 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": ["asadas123455689!@#$%^&*()"]
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_040 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [""]
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_041 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [" "]
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_042 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "ascend",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_043 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "asdhjlasdhjhkhj123123!@#&*#*(9",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_044 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": get_str(4),
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_045 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": get_int(4),
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_046 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_047 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": " ",
                "update_time": "ascend"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_048 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "asdhajghkaj12314!!@##$%^&&*"
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_049 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": get_str(4)
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_050 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": get_int(4)
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_051 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": ""
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_052 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": " "
            },
            "page_size": 20,
            "page_num": 1
        }, ['res["code"]==0', 'res["data"]["intents_list"][0]["intent_name"]=="无意图"'], {}]
        self.param_list_053 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": get_str(4),
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_054 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": get_int(4),
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_055 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": "",
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_056 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": " ",
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_057 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": 0,
            "page_num": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_058 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": 20,
            "page_num": 0
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_059 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": 20,
            "page_num": get_str(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_060 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": 20,
            "page_num": get_int(4)
        }, ['res["code"]==0', 'res["data"]["total_num"]==1'], {}]
        self.param_list_061 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": 20,
            "page_num": "123123452!@#$!%^&@**929)))"
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_062 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": 20,
            "page_num": ""
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_063 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "descend",
                "update_time": "descend"
            },
            "page_size": 20,
            "page_num": " "
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_list_064 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": "",
                "intent_name": ""
            },
            "filters": {
                "intent_type": [0, 1, 2],
                "trigger_type": [0, 1, 2, 3, 4],
                "skill_type": [1, 3]
            },
            "sort": {
                "examples_count": "",
                "update_time": ""
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        """
        新增意图
        """
        self.param_create_001 = [{
                      "agent_id": None,
                      "intent_name": None,
                      "examples": [
                        {
                          "id": None,
                          "name": None
                        }
                      ],
                      "keywords_eq": [
                        {
                          "id": None,
                          "name": None
                        }
                      ],
                      "keywords_include": [
                        {
                          "id": None,
                          "name": None
                        }
                      ]
                    }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_003 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_create_004 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_create_005 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_create_006 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_create_007 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_create_008 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_create_009 = [{
            "agent_id": get_int(5),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {'intent_id': 'res["data"]["intent_id"]'}]
        self.param_create_010 = [{
            "agent_id": get_str(5),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_011 = [{
            "agent_id": "",
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_012 = [{
            "agent_id": " ",
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_013 = [{
            "agent_id": "1213128!@#$%^^&*()_)_+)_++",
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_014 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_int(128),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_015 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": "",
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10004', 'res["msg"]=="创建意图失败"'], {}]
        self.param_create_016 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": " ",
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10004', 'res["msg"]=="创建意图失败"'], {}]
        self.param_create_017 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": "123567234789!@#$%^&*()_`1",
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_018 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_int(129),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_019 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_020 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": get_int(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_021 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": "123112!@#$%^^&**(())Fgjasd",
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_022 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": "",
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_023 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": " ",
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_024 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_int(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_025 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": "1231214!@#$%^&*()~sd"
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_026 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": ""
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_027 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": " "
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_028 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(128)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_029 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(129)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_030 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": get_str(4),
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_031 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_032 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": "1231453657ASDF!@#$%^&*(((",
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_033 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": "",
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_034 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": " ",
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_035 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(64)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_036 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(65)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_037 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": "12131!@#$%^&&**(())___"
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_038 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": ""
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_039 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": " "
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_040 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_041 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": get_str(4),
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_042 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": "123gyakk!@#$%^&*()_",
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_043 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": "",
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_044 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": " ",
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_create_045 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(64)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_046 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(65)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_047 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": "12334698asdghjglshfl!@#~$%^&&*(("
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_048 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": ""
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_049 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": " "
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_050 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                },{
                    "id": 2,
                    "name": get_str(4)
                },{
                    "id": 3,
                    "name": get_str(4)
                },{
                    "id": 4,
                    "name": get_str(4)
                },{
                    "id": 5,
                    "name": get_str(4)
                },{
                    "id": 6,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                },{
                    "id": 2,
                    "name": get_str(4)
                },{
                    "id": 3,
                    "name": get_str(4)
                },{
                    "id": 4,
                    "name": get_str(4)
                },{
                    "id": 5,
                    "name": get_str(4)
                },{
                    "id": 6,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                },{
                    "id": 2,
                    "name": get_str(4)
                },{
                    "id": 3,
                    "name": get_str(4)
                },{
                    "id": 4,
                    "name": get_str(4)
                },{
                    "id": 5,
                    "name": get_str(4)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {}]
        self.param_create_051 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": "test_intents名称".join(get_str(4)),
            "examples": [
                {
                    "id": 1,
                    "name": "test_intents 相似说法".join(get_str(4))
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": "test_intents 关键词等于".join(get_str(4))
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": "test_intents 关键词包含".join(get_str(4))
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="创建意图成功"'], {'intents_id': 'res["data"]["intent_id"]'}]
        """
        删除意图
        """
        self.param_del_001 = [{
            "agent_id": None,
            "intent_id": None
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": None
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_003 = [{
            "agent_id": None,
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_004 = [{
            "agent_id": "1231FGFJHFJFJFJffjfj$$!%^@&#",
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_005 = [{
            "agent_id": "",
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_006 = [{
            "agent_id": " ",
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_007 = [{
            "agent_id": get_int(4),
            "intent_id": get_int(4)
        }, ['res["code"]==10005', 'res["msg"]=="删除意图失败"'], {}]
        self.param_del_008 = [{
            "agent_id": get_str(4),
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_009 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": "123123asjhjahkdahk#$@&&672991!@"
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_010 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": ""
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_011 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": " "
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_012 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_str(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_del_013 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_int(4)
        }, ['res["code"]==10005', 'res["msg"]=="删除意图失败"'], {}]
        self.param_del_014 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id")
        }, ['res["code"]==0', 'res["msg"]=="删除意图成功"'], {}]

        """
        单个意图详情
        """
        self.param_datail_intents_001 = [{
            "agent_id": None,
            "intent_id": None
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": None
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_003 = [{
            "agent_id": None,
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_004 = [{
            "agent_id": "1231FGFJHFJFJFJffjfj$$!%^@&#",
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_005 = [{
            "agent_id": "",
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_006 = [{
            "agent_id": " ",
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_007 = [{
            "agent_id": get_int(4),
            "intent_id": get_int(4)
        }, ['res["code"]==10007', 'res["msg"]=="获取单个意图详情信息失败"'], {}]
        self.param_datail_intents_008 = [{
            "agent_id": get_str(4),
            "intent_id": get_int(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_009 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": "123123asjhjahkdahk#$@&&672991!@"
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_010 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": ""
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_011 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": " "
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_012 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_str(4)
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_datail_intents_013 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_int(4)
        }, ['res["code"]==10007', 'res["msg"]=="获取单个意图详情信息失败"'], {}]
        self.param_datail_intents_014 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id")
        }, ['res["code"]==0', '"test_intents" in res["data"]["intent_name"]'], {}]
        self.param_datail_intents_015 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id")
        }, ['res["code"]==0', '"test_intents" not in res["data"]["intent_name"]'], {}]

        """
        编辑意图 
        """
        self.param_edit_001 = [{
            "agent_id": None,
            "intent_id": None,
            "intent_name": None,
            "intent_type": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": None,
            "intent_name": None,
            "intent_type": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_003 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": None,
            "intent_type": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_004 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_005 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_edit_006 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_edit_007 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_edit_008 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_edit_009 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_edit_010 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": None
                }
            ]
        }, ['res["code"]==200', '"NoneType" in res["msg"]'], {}]
        self.param_edit_011 = [{
            "agent_id": get_int(5),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10006', 'res["msg"]=="修改意图失败"'], {}]
        self.param_edit_012 = [{
            "agent_id": get_str(5),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_013 = [{
            "agent_id": "",
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,

            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_014 = [{
            "agent_id": " ",
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_015 = [{
            "agent_id": "1213128!@#$%^^&*()_)_+)_++",
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_016 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_int(4),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10006', 'res["msg"]=="修改意图失败"'], {}]
        self.param_edit_017 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_str(4),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_018 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": "1123679579!~@#$%^&*()_QEGHJghjkssasd",
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_019 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": "",
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_020 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": " ",
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_021 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_int(128),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_022 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": "",
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10006', 'res["msg"]=="修改意图失败"'], {}]
        self.param_edit_023 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": " ",
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10006', 'res["msg"]=="修改意图失败"'], {}]
        self.param_edit_024 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": "123567234789!@#$%^&*()_`1",
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10008', 'res["msg"]=="意图名称已存在"'], {}]
        self.param_edit_025 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_int(129),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_026 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": get_int(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10006', 'res["msg"]=="修改意图失败"'], {}]
        self.param_edit_027 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_028 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": "12345469094586074SDDFDajsgdhjgaja!@#$%^&",
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_029 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": "",
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_030 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": " ",
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_031 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 2,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10006', 'res["msg"]=="修改意图失败"'], {}]
        self.param_edit_032 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_033 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": get_int(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_034 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": "123112!@#$%^^&**(())Fgjasd",
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_035 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": "",
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_036 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": " ",
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_037 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_int(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_038 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": "1231214!@#$%^&*()~sd"
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_039 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": ""
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_040 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": " "
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_041 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(128)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_042 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(129)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_043 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": get_str(4),
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_044 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_045 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": "1231453657ASDF!@#$%^&*(((",
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_046 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": "",
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_047 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": " ",
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_048 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(64)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_049 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(65)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_050 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": "12131!@#$%^&&**(())___"
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_051 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": ""
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_052 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": " "
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_053 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_054 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": get_str(4),
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_055 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": "123gyakk!@#$%^&*()_",
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_056 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": "",
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_057 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": " ",
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"'], {}]
        self.param_edit_058 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(64)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_059 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(65)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_060 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": "12334698asdghjglshfl!@#~$%^&&*(("
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_061 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": ""
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_062 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": " "
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_063 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }, {
                    "id": 2,
                    "name": get_str(4)
                }, {
                    "id": 3,
                    "name": get_str(4)
                }, {
                    "id": 4,
                    "name": get_str(4)
                }, {
                    "id": 5,
                    "name": get_str(4)
                }, {
                    "id": 6,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }, {
                    "id": 2,
                    "name": get_str(4)
                }, {
                    "id": 3,
                    "name": get_str(4)
                }, {
                    "id": 4,
                    "name": get_str(4)
                }, {
                    "id": 5,
                    "name": get_str(4)
                }, {
                    "id": 6,
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }, {
                    "id": 2,
                    "name": get_str(4)
                }, {
                    "id": 3,
                    "name": get_str(4)
                }, {
                    "id": 4,
                    "name": get_str(4)
                }, {
                    "id": 5,
                    "name": get_str(4)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]
        self.param_edit_064 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, ['res["code"]==0', 'res["msg"]=="修改意图成功"'], {}]