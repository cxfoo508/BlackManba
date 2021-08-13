import os

from data.data_method import *


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
                'res["data"]["rows"][0]["phrases"]=="测试1$测试2$测试3"'], {}
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
                'res["data"]["rows"][0]["phrases"]=="测试1$测试2$测试3"', 'res["data"]["rows"][0]["replacetext"]=="替换文本"'], {}]
        # </editor-fold>

        # <editor-fold desc = "创建实体值">
        self.parm_entity_009 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(4),
                "phrases": None,
                "replacetext": None
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]

        self.parm_entity_009_1 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "entity_id": os.environ.get('entity_id'),
                "entity_type": os.environ.get('entity_type'),
                "value": get_str(4),
                "phrases": "测试1$测试2$测试3",
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
                "phrases": "测试1$测试2$测试3",
                "replacetext": "替换文本"
            },
            ['res["code"]==0', 'res["msg"]=="实体值创建成功"', 'res["data"]["entity_value_id"]!=None'],
            {'entity_value_id': 'res["data"]["entity_value_id"]'}
        ]
        # 枚举实体值
        # 系统实体值
        # </editor-fold>

        # <editor-fold desc = "更新实体">
        # </editor-fold>
