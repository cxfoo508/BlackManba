import os

from data_method import *


class app_data_class:
    def __init__(self):
        """
        节点参数
        """
        """
        单元测试-创建app
        """
        self.param_001 = [{
            "agent_name": get_str(9),
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_002 = [{
            "agent_name": "测试app",
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_003 = [{
            "agent_name": "test!@~#$%^& ,.;'",
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_004 = [{
            "agent_name": "12344",
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_005 = [{
            "agent_name": "12344",
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_006 = [{
            "agent_name": get_str(33),
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["data"][0]["loc"][0]=="body"', 'res["data"][0]["msg"]=="ensure this value has at most 32 characters"',
            'res["data"][0]["type"]=="value_error.any_str.max_length"', 'res["data"][0]["ctx"]["limit_value"]==32'],
             {}
        ]
        self.param_006_1 = [{
            "agent_name": get_str(32),
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_006_2 = [{
            "agent_name": get_str(99),
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        },
            ['res["data"][0]["loc"][0]=="body"', 'res["data"][0]["msg"]=="ensure this value has at most 32 characters"',
             'res["data"][0]["type"]=="value_error.any_str.max_length"', 'res["data"][0]["ctx"]["limit_value"]==32'],
             {}
        ]
        self.param_007 = [{
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, [],  {"agent_id": "res['data']['agent_id']"}]
        # agent_ditail
        self.param_008 = [{
            "agent_name": get_str(9),
            "agent_detail": "总问字符",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_009 = [{
            "agent_name": get_str(9),
            "agent_detail": "test～！@#¥%……&*，。 ",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_010 = [{
            "agent_name": get_str(9),
            "agent_detail": get_str(512),
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_010_1 = [{
            "agent_name": get_str(9),
            "agent_detail": get_str(513),
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        },
            ['res["data"][0]["loc"][1]=="agent_detail"', 'res["data"][0]["msg"]=="ensure this value has at most 512 characters"',
             'res["data"][0]["type"]=="value_error.any_str.max_length"', 'res["data"][0]["ctx"]["limit_value"]==512'],
             {}
        ]
        self.param_011 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]

        self.param_012 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试!@~#$%^&*<>, ?",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]

        self.param_013 = [{
            "agent_name": get_str(9),
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, [],  {"agent_id": "res['data']['agent_id']"}]

        # agent_logo
        self.param_014 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_015 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "agent_logo": "12312334!@#$%^ ,.",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_016 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "agent_logo": "data/科比.jpeg",
            "lang": "en-US"
        }, ['res["code"]==0', 'res["data"]!=None'],  {"agent_id": "res['data']['agent_id']"}]
        self.param_017 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "agent_logo": "data/科比.jpeg",
            "lang": "esdfsdag善良的看法离开的肌肤"
        },
            ['res["data"][0]["loc"][1]=="lang"',
             'res["data"][0]["msg"]=="ensure this value has at most 10 characters"',
             'res["data"][0]["type"]=="value_error.any_str.max_length"', 'res["data"][0]["ctx"]["limit_value"]==10'],
            {}
        ]

        """
        del app
        """
        self.param_019 = [
            {
                "agent_id": os.environ.get("agent_id")
            },
            ['res["code"]==0'],
             {}

        ]
