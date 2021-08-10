import os

from data_method import *


class entity_data_class:
    def __init__(self):
        # <editor-fold desc="创建实体">
        self.parm_entity_001 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 1
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]'}]
        self.parm_entity_002 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": f"{get_str(4)}",
            "entity_type": 2
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]'}
        ]
        self.parm_entity_003 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": f"{get_str(7)}",
            "entity_type": 3
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'], {"entity_id": 'res["data"]["entity_id"]'}
        ]
        self.parm_entity_004 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": f"{get_str(4)}",
            "entity_type": 4
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]'}
        ]
        self.parm_entity_001_1 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(4) + "~!@# $%^",
            "entity_type": 1
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'], {"entity_id": 'res["data"]["entity_id"]'}]
        self.parm_entity_001_2 = [{

            "entity_name": get_str(4),
            "entity_type": 1}
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
               'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_001_3 = [{
            "agent_id": os.environ.get('agent_id'),

            "entity_type": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_001_4 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(4)

        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
            'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_001_5 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(128),
            "entity_type": 1
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'], {"entity_id": 'res["data"]["entity_id"]'}]
        self.parm_entity_001_6 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(129),
            "entity_type": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'], {}]
        self.parm_entity_001_7 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": None,
            "entity_type": 4
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="none is not an allowed value"'], {}
        ]
        self.parm_entity_001_8 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(4),
            "entity_type": None
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
            'res["data"][0]["msg"]=="none is not an allowed value"'], {}
        ]
        self.parm_entity_001_9 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 1,
            "value_list": [get_str(3), get_str(3), get_int(5)]
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]',
             "value_list_len": 'len(req["value_list"])'}]
        self.parm_entity_001_10 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 1,
            "value_list": ['']
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]',
             "value_list_len": 'len(req["value_list"])'}]
        self.parm_entity_001_11 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 1,
            "value_list": [get_str(128)]
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]',
             "value_list_len": 'len(req["value_list"])'}]
        self.parm_entity_001_12 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 1,
            "value_list": [get_str(129)]
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]',
             "value_list_len": 'len(req["value_list"])'}]
        self.parm_entity_002_1 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(4) + "~!@# $%^",
            "entity_type": 2
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'], {"entity_id": 'res["data"]["entity_id"]'}]
        self.parm_entity_002_2 = [{

            "entity_name": get_str(4),
            "entity_type": 2}
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
               'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_002_3 = [{
            "agent_id": os.environ.get('agent_id'),

            "entity_type": 2
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_002_4 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(4)

        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
            'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_002_5 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(128),
            "entity_type": 2
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'], {"entity_id": 'res["data"]["entity_id"]'}]
        self.parm_entity_002_6 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(129),
            "entity_type": 2
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'], {}]
        self.parm_entity_002_7 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": None,
            "entity_type": 2
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="none is not an allowed value"'], {}
        ]
        self.parm_entity_002_9 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 2,
            "value_list": [get_str(3), get_str(3), get_int(5)]
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]',
             "value_list_len": 'len(req["value_list"])'}]
        self.parm_entity_002_10 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 2,
            "value_list": ['']
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]',
             "value_list_len": 'len(req["value_list"])'}]
        self.parm_entity_002_11 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 2,
            "value_list": [get_str(128)]
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]',
             "value_list_len": 'len(req["value_list"])'}]
        self.parm_entity_002_12 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(6),
            "entity_type": 2,
            "value_list": [get_str(129)]
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'],
            {"entity_id": 'res["data"]["entity_id"]', "entity_type": 'req["entity_type"]',
             "value_list_len": 'len(req["value_list"])'}
        ]
        self.parm_entity_003_1 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(4) + "~!@# $%^",
            "entity_type": 4
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'], {"entity_id": 'res["data"]["entity_id"]'}]
        self.parm_entity_003_2 = [{

            "entity_name": get_str(4),
            "entity_type": 4}
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
               'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_003_3 = [{
            "agent_id": os.environ.get('agent_id'),

            "entity_type": 4
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_003_4 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(4)

        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
            'res["data"][0]["msg"]=="field required"'], {}]
        self.parm_entity_003_5 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(128),
            "entity_type": 4
        }, ['res["code"]==0', 'res["msg"]=="实体创建成功"'], {"entity_id": 'res["data"]["entity_id"]'}]
        self.parm_entity_003_6 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(129),
            "entity_type": 4
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'], {}]
        self.parm_entity_003_7 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": None,
            "entity_type": 4
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="none is not an allowed value"'], {}
        ]

        # </editor-fold>
        # <editor-fold desc = "获取实体类型列表">

        self.parm_entity_005 = [
            {
                "page_no": 1,
                "number_per_page": 20
            }, ["len(res['data']['rows'])==4"], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "删除实体">
        self.parm_entity_006 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type')
            }
            , ['res["code"]==0', 'res["msg"]=="实体删除成功"'], {}
        ]
        self.parm_entity_006_1 = [
            {
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type')
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
               "res['data'][0]['msg']=='field required'"], {}
        ]
        self.parm_entity_006_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_type": os.environ.get('entity_type')
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_id"',
               "res['data'][0]['msg']=='field required'"], {}
        ]
        self.parm_entity_006_3 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
               "res['data'][0]['msg']=='field required'"], {}
        ]
        self.parm_entity_006_4 = [
            {
                "agent_id": '',
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type')
            }
            , ['res["code"]==10012', 'res["msg"]=="机器人非法"'], {}
        ]
        self.parm_entity_006_5 = [
            {
                "agent_id": None,
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type')
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
               "res['data'][0]['msg']=='none is not an allowed value'"], {}
        ]
        self.parm_entity_006_6 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": '',
                "entity_type": os.environ.get('entity_type')
            }
            , ['res["code"]==10005', 'res["msg"]=="实体删除失败"'], {}
        ]
        self.parm_entity_006_7 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": None,
                "entity_type": os.environ.get('entity_type')
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_id"',
               "res['data'][0]['msg']=='none is not an allowed value'"], {}
        ]
        self.parm_entity_006_8 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": 334
            }
            , ['res["code"]==10005', 'res["msg"]=="实体删除失败"'], {}
        ]
        self.parm_entity_006_9 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": None
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
               "res['data'][0]['msg']=='none is not an allowed value'"], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "获取实体列表">
        self.parm_entity_007 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_type": os.environ.get("entity_type"),
                "entity_id": os.environ.get('entity_id'),
                "entity_id_list": [
                ],
                "entity_name": None,
                "entity_value_required": 1,
                "page_no": 1,
                "number_per_page": 200
            }, ['str(len(res["data"]["rows"]))==os.environ.get("value_list_len")'], {}
        ]
        self.parm_entity_007_1 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_type": os.environ.get("entity_type"),
                "entity_id": os.environ.get('entity_id'),
                "entity_id_list": [
                ],
                "entity_name": None,
                "entity_value_required": 0,
                "page_no": 1,
                "number_per_page": 200
            }, ["res['data']['rows'][0]['entity_name']==os.environ.get('entity_name')"], {}
        ]
        self.parm_entity_007_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_type": os.environ.get("entity_type"),
                "entity_id": os.environ.get('entity_id'),
                "entity_id_list": [
                ],
                "entity_name": None,
                "entity_value_required": 0,
                "page_no": 1,
                "number_per_page": 200
            }, ["res['data']['count']==0"], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "获取实体值列表">
        self.parm_entity_008 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['str(len(res["data"]["rows"]))==os.environ.get("value_list_len")'], {}
        ]
        self.parm_entity_008_1 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['res["data"]["rows"][0]["id"]==os.environ.get("entity_value_id")'], {}
        ]
        self.parm_entity_008_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['res["data"]["rows"][0]["id"]==os.environ.get("entity_value_id")',
                'res["data"]["rows"][0]["phrases"]=="测试1$$测试2$$测试3"'], {}
        ]
        self.parm_entity_008_3 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['str(len(res["data"]["rows"]))=="3"'], {}]
        self.parm_entity_008_4 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['res["data"]["rows"][0]["id"]==os.environ.get("entity_value_id")',
                'res["data"]["rows"][0]["phrases"]=="测试1$$测试2$$测试3"', 'res["data"]["rows"][0]["replacetext"]=="替换文本"'],
            {}]
        self.parm_entity_008_5 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['str(len(res["data"]["rows"]))=="0"'], {}
        ]
        self.parm_entity_008_6 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['res["data"]["rows"][0]["value"]==os.environ.get("entity_value")'], {}
        ]
        self.parm_entity_008_7 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['res["data"]["rows"][0]["phrases"]==os.environ.get("entity_phrases")'], {}
        ]
        self.parm_entity_008_8 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": None,
                "page_no": 1,
                "number_per_page": 10
            }, ['res["data"]["rows"][0]["replacetext"]==os.environ.get("replacetext")'], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "创建实体值">
        self.parm_entity_009 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(4),
                "phrases": get_str(3),
                "replacetext": get_str(4)
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]', "entity_value": 'req["value"]',
             "entity_phrases": "req['phrases']", "replacetext": 'req["replacetext"]'}
        ]

        self.parm_entity_009_1 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(4),
                "phrases": "测试1$$测试2$$测试3",
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        self.parm_entity_009_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(4),
                "phrases": "测试1$$测试2$$测试3",
                "replacetext": "替换文本"
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        self.parm_entity_009_3 = [
            {
                # 必填项 agent_id
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(4),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
             'res["data"][0]["msg"]=="field required"'],
            {}]
        self.parm_entity_009_4 = [
            {
                "agent_id": os.environ.get('agent_id'),
                # 必填项 entity_id
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(4),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_id"',
             'res["data"][0]["msg"]=="field required"'],
            {}]
        self.parm_entity_009_5 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                # 必填项 entity_type
                "value": get_str(4),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
             'res["data"][0]["msg"]=="field required"'],
            {}]
        self.parm_entity_009_6 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                # entity_type=None
                "entity_type": None,
                "value": get_str(4),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
             'res["data"][0]["msg"]=="none is not an allowed value"'],
            {}]
        self.parm_entity_009_7 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": None,
                "entity_type": os.environ.get('entity-type'),
                "value": get_str(4),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_id"',
             'res["data"][0]["msg"]=="none is not an allowed value"'],
            {}]
        self.parm_entity_009_8 = [
            {
                "agent_id": None,
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity-type'),
                "value": get_str(4),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
             'res["data"][0]["msg"]=="none is not an allowed value"'],
            {}]
        self.parm_entity_009_9 = [
            {  # 实体值长度
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": None,
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        self.parm_entity_009_10 = [
            {  # 实体值长度
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(128),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        self.parm_entity_009_11 = [
            {  # 实体值长度
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(129),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"',
             'res["data"][0]["loc"][1]=="value"',
             'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'],
            {}
        ]
        self.parm_entity_009_12 = [
            {  # phrases长度
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": '1',
                "phrases": '',
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        self.parm_entity_009_13 = [
            {  # phrases长度
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(12),
                "phrases": get_str(128),
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        self.parm_entity_009_14 = [
            {  # phrases长度
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(12),
                "phrases": get_str(129),
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"',
             'res["data"][0]["loc"][1]=="phrases"',
             'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'],
            {}
        ]
        self.parm_entity_009_15 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": '1',
                "phrases": '1',
                "replacetext": ''
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        self.parm_entity_009_16 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(12),
                "phrases": get_str(18),
                "replacetext": get_str(256)
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        self.parm_entity_009_17 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(12),
                "phrases": get_str(12),
                "replacetext": get_str(257)
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"',
             'res["data"][0]["loc"][1]=="replacetext"',
             'res["data"][0]["msg"]=="ensure this value has at most 256 characters"'],
            {}]

        # </editor-fold>

        # <editor-fold desc = "更新实体">
        self.parm_entity_010 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_id": os.environ.get('entity_id'),
            "entity_name": get_str(6),
            "entity_type": 1
        }, ['res["code"]==0', 'res["msg"]=="实体更新成功"'],
            {"entity_type": 'req["entity_type"]', "entity_name": 'req["entity_name"]'}]
        self.parm_entity_010_1 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_id": os.environ.get('entity_id'),
            "entity_name": get_str(128),
            "entity_type": 1
        }, ['res["code"]==0', 'res["msg"]=="实体更新成功"'],
            {"entity_type": 'req["entity_type"]', "entity_name": 'req["entity_name"]'}]
        self.parm_entity_010_2 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_id": os.environ.get('entity_id'),
            "entity_name": get_str(129),
            "entity_type": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_name"',
            'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'],
            {"entity_type": 'req["entity_type"]', "entity_name": 'req["entity_name"]'}]
        self.parm_entity_010_3 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_id": os.environ.get('entity_id'),
            "entity_name": '',
            "entity_type": 1
        }, ['res["code"]==0', 'res["msg"]=="实体更新成功"'],
            {"entity_type": 'req["entity_type"]', "entity_name": 'req["entity_name"]'}]
        self.parm_entity_010_4 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_id": os.environ.get('entity_id'),
            "entity_name": None,
            "entity_type": 1
        }, ['res["code"]==0', 'res["msg"]=="实体更新成功"'],
            {"entity_type": 'req["entity_type"]', "entity_name": 'req["entity_name"]'}]
        self.parm_entity_010_5 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_id": os.environ.get('entity_id'),
            "entity_type": 1
        }, ['res["code"]==0', 'res["msg"]=="实体更新成功"'],
            {"entity_type": 'req["entity_type"]', "entity_name": 'req["entity_name"]'}]
        # 必填项
        self.parm_entity_010_6 = [{
            "entity_id": os.environ.get('entity_id'),
            "entity_name": get_str(12),
            "entity_type": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
            'res["data"][0]["msg"]=="field required"'],
            {"entity_type": 'req["entity_type"]', "entity_name": 'req["entity_name"]'}]
        self.parm_entity_010_7 = [{
            "agent_id": os.environ.get('agent_id'),
            "entity_name": get_str(12),
            "entity_type": 1
        }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_id"',
            'res["data"][0]["msg"]=="field required"'],
            {"entity_type": 'req["entity_type"]', "entity_name": 'req["entity_name"]'}]

        # </editor-fold>

        # <editor-fold desc = "更新枚举实体值">
        self.parm_entity_011 = [
            {  # 更新实体值
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'entity_value': 'req["value"]'}
        ]
        self.parm_entity_011_1 = [
            {  # 实体值长度
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(128),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'entity_value': 'req["value"]'}
        ]
        self.parm_entity_011_2 = [
            {  # 实体值长度
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(129),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="value"',
             'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'],
            {}
        ]
        self.parm_entity_011_3 = [
            {  # 实体值
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(12) + '!~@#$%^6, 23',
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'entity_value': 'req["value"]'}
        ]
        self.parm_entity_011_4 = [
            {  # 实体值
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": '',
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'entity_value': 'req["value"]'}
        ]
        self.parm_entity_011_5 = [
            {  # 实体值
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": None,
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'entity_value': 'req["value"]'}
        ]
        self.parm_entity_011_6 = [
            {  # phrases
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(5)}$${get_str(5)}&&{get_str(5)}~!@#$% @#',
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'entity_phrases': 'req["phrases"]'}
        ]
        self.parm_entity_011_7 = [
            {  # phrases
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(2048)}',
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'entity_phrases': 'req["phrases"]'}
        ]
        self.parm_entity_011_8 = [
            {  # phrases
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(2049)}',
                "replacetext": None
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="phrases"',
             'res["data"][0]["msg"]=="ensure this value has at most 2048 characters"'],
            {}
        ]
        self.parm_entity_011_9 = [
            {  # phrases
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": '',
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'entity_phrases': 'req["phrases"]'}
        ]
        self.parm_entity_011_10 = [
            {  # phrases
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {}
        ]
        self.parm_entity_011_11 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(5)}$${get_str(5)}&&{get_str(5)}~!@#$% @#',
                "replacetext": get_str(4)
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'replacetext': 'req["replacetext"]'}
        ]
        self.parm_entity_011_12 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(4)}',
                "replacetext": get_str(256)
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'replacetext': 'req["replacetext"]'}
        ]
        self.parm_entity_011_13 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(12)}',
                "replacetext": get_str(257)
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="replacetext"',
             'res["data"][0]["msg"]=="ensure this value has at most 256 characters"'],
            {}
        ]
        self.parm_entity_011_14 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": get_str(4),
                "replacetext": ''
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {'replacetext': 'req["replacetext"]'}
        ]
        self.parm_entity_011_15 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": get_str(4),
            },
            ['res["code"]==0', 'res["msg"]=="实体值更新成功"'],
            {}]
        # 必填项
        self.parm_entity_011_16 = [
            {
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(12)}',
                "replacetext": get_str(12)
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
             'res["data"][0]["msg"]=="field required"'],
            {}
        ]
        self.parm_entity_011_17 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_type": os.environ.get('entity_type'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(12)}',
                "replacetext": get_str(257)
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_id"',
             'res["data"][0]["msg"]=="field required"'],
            {}
        ]
        self.parm_entity_011_18 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_value_id": os.environ.get('entity_value_id'),
                "value": get_str(4),
                "phrases": f'{get_str(12)}',
                "replacetext": get_str(257)
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_type"',
             'res["data"][0]["msg"]=="field required"'],
            {}
        ]
        self.parm_entity_011_19 = [
            {  # replacetext
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(4),
                "phrases": f'{get_str(12)}',
                "replacetext": get_str(257)
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="entity_value_id"',
             'res["data"][0]["msg"]=="field required"'],
            {}
        ]
        # </editor-fold>

        # <editor-fold desc = "更新正则实体值 功能未实现">
        # </editor-fold>

        # <editor-fold desc = "获取枚举实体模版">
        self.parm_entity_012 = [
            None, ['res["code"]==0', 'res["data"]["url"]=="http://39.105.24.211:5555/chatbot/mid/oss/枚举实体导入模版.xlsx"'],
            {}
        ]
        # </editor-fold>
