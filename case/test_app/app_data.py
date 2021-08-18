import os

from data.data_method import *

class app_data_class:
    def __init__(self):
        """
        节点参数
        """
        # <editor-fold desc="创建app">
        """
        单元测试-创建app
        """
        self.param_001 = [{
            "agent_name": get_str(9),
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'],
            {"agent_id": "res['data']['agent_id']", "agent_name": "req['agent_name']"}]
        self.param_002 = [{
            "agent_name": "测试app",
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_003 = [{
            "agent_name": "test!@~#$%^& ,.;'",
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_004 = [{
            "agent_name": "12344",
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_005 = [{
            "agent_name": "12344",
            "agent_detail": "test",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
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
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
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
        }, [], {"agent_id": "res['data']['agent_id']"}]
        # agent_ditail
        self.param_008 = [{
            "agent_name": get_str(9),
            "agent_detail": "总问字符",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_009 = [{
            "agent_name": get_str(9),
            "agent_detail": "test～！@#¥%……&*，。 ",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_010 = [{
            "agent_name": get_str(9),
            "agent_detail": get_str(512),
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_010_1 = [{
            "agent_name": get_str(9),
            "agent_detail": get_str(513),
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        },
            ['res["data"][0]["loc"][1]=="agent_detail"',
             'res["data"][0]["msg"]=="ensure this value has at most 512 characters"',
             'res["data"][0]["type"]=="value_error.any_str.max_length"', 'res["data"][0]["ctx"]["limit_value"]==512'],
            {}
        ]
        self.param_011 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]

        self.param_012 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试!@~#$%^&*<>, ?",
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]

        self.param_013 = [{
            "agent_name": get_str(9),
            "agent_logo": "data/科比.jpeg",
            "lang": "zh-CN"
        }, [], {"agent_id": "res['data']['agent_id']"}]

        # agent_logo
        self.param_014 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_015 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "agent_logo": "12312334!@#$%^ ,.",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
        self.param_016 = [{
            "agent_name": get_str(9),
            "agent_detail": "测试",
            "agent_logo": "data/科比.jpeg",
            "lang": "en-US"
        }, ['res["code"]==0', 'res["data"]!=None'], {"agent_id": "res['data']['agent_id']"}]
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
        # </editor-fold>

        # <editor-fold desc = "更新app">
        """
        更新 app
        """
        self.up_parm_001 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_str(4),
            "agent_log": '',
            "agent_detail": "test",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]["rowcount"]!=None', 'res["msg"]=="机器人更新成功"'],
            {"agent_name": 'req["agent_name"]'}]
        self.up_parm_002 = [{
            "agent_name": "测试app",
            "agent_detail": "test",
            "lang": "zh-CN"
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
            'res["data"][0]["msg"]=="field required"'], {}]
        self.up_parm_003 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": f"{get_str(3)}!@~#$%^& ,.;'",
            "agent_detail": "test",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]["rowcount"]!=None', 'res["msg"]=="机器人更新成功"'],
            {"agent_name": 'req["agent_name"]'}]
        self.up_parm_004 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_int(4),
            "agent_detail": "test",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]["rowcount"]!=None', 'res["msg"]=="机器人更新成功"'],
            {"agent_name": 'req["agent_name"]'}]

        self.up_parm_005 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_str(32),
            "agent_detail": "test",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]["rowcount"]!=None', 'res["msg"]=="机器人更新成功"'],
            {"agent_name": 'req["agent_name"]'}]
        self.up_parm_006 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_str(33),
            "agent_detail": "test",
            "lang": "zh-CN"
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_name"',
            'res["data"][0]["msg"]=="ensure this value has at most 32 characters"'],
            {}]
        self.up_parm_007 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_str(5),
            "agent_detail": get_str(512),
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]["rowcount"]!=None', 'res["msg"]=="机器人更新成功"'],
            {"agent_name": 'req["agent_name"]'}]
        self.up_parm_008 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_str(5),
            "agent_detail": get_str(513),
            "lang": "zh-CN"
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_detail"',
            'res["data"][0]["msg"]=="ensure this value has at most 512 characters"'],
            {}]
        self.up_parm_009 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_str(5),
            "agent_detail": None,
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["data"]["rowcount"]!=None', 'res["msg"]=="机器人更新成功"'],
            {"agent_name": 'req["agent_name"]'}]
        self.up_parm_010 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_str(5),
            "agent_detail": None,
            "lang": "en-US"
        }, ['res["code"]==0', 'res["data"]["rowcount"]!=None', 'res["msg"]=="机器人更新成功"'],
            {"agent_name": 'req["agent_name"]'}]
        self.up_parm_011 = [{
            "agent_id": os.environ.get('agent_id'),
            "agent_name": get_str(5),
            "agent_detail": None,
            "lang": "en-US"
        }, ['res["code"]==0', 'res["data"]["rowcount"]!=None', 'res["msg"]=="机器人更新成功"'],
            {"agent_name": 'req["agent_name"]'}]
        # </editor-fold>

        # <editor-fold desc="机器人列表">
        """
        获取机器人列表
        """
        self.get_app_lit_001 = [{
            "page_no": 1,
            "number_per_page": 20,
            "agent_id": os.environ.get('agent_id')
        }, ["res['data']['rows'][0]['agent_name']==os.environ.get('agent_name')"], {}]

        self.get_app_lit_002 = [{
            "page_no": 1,
            "number_per_page": 20,
        }, ["len(res['data']['rows']) >=0", "res['code']==0"], {}]

        self.get_app_lit_003 = [{
            "page_no": 1,
            "number_per_page": 1,
        }, ["len(res['data']['rows']) == 1", "res['code']==0"], {}]

        self.get_app_lit_004 = [{
            "page_no": 1,
            "number_per_page": 0,
        }, ["res['data'][0]['loc'][1] == 'number_per_page'", "res['code']==10009", "res['msg'] == '接口参数验证出错'"], {}]

        self.get_app_lit_005 = [{
            "page_no": 1,
            "number_per_page": 200,
        }, ["len(res['data']['rows']) >= 0", "res['code']==0"], {}]

        self.get_app_lit_006 = [{
            "page_no": 0,
            "number_per_page": 20,
        }, ["res['data'][0]['loc'][1] == 'page_no'", "res['code']==10009", "res['msg'] == '接口参数验证出错'",
            "res['data'][0]['msg']=='ensure this value is greater than or equal to 1'"], {}]
        self.get_app_lit_007 = [{
            "page_no": 1,
        }, ["res['data'][0]['loc'][1] == 'number_per_page'", "res['code']==10009", "res['msg'] == '接口参数验证出错'",
            "res['data'][0]['msg']=='field required'"], {}]
        self.get_app_lit_008 = [{
            "number_per_page": 1,
        }, ["len(res['data']['rows']) == 1", "res['code']==0"], {}]
        # </editor-fold>

        # <editor-fold desc = "del app">
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
        # </editor-fold>

        # <editor-fold desc="用户登陆">
        """
        用户登陆
        """
        self.param_login = [
            {
                "username": "laiye",
                "password": "123123",
                "is_keep_login": True
            },
            [], {'token': 'res["data"]["jwt_token"]'}
        ]
        # </editor-fold>

        # <editor-fold desc="发布机器人">
        self.param_agent_start = [
            {
                "agent_id": os.environ.get('agent_id')
            }
            , [], {}, {'sleep_time': 30}
        ]

        # </editor-fold>
