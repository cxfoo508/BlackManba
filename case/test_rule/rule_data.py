import os

from data.data_method import *


class rule_data_class:
    def __init__(self):
        """
        节点参数
        """
        # <editor-fold desc ="获取节点列表">
        """
        call-获取节点列表
        """
        self.param_001 = [{
            "agent_id": os.environ.get("agent_id"),
            "is_details_required": 0,
            "page_no": 1,
            "number_per_page": 10
        }, ['res["code"]==0', 'len(res["data"]["rows"])==2'],
            {}]

        self.param_001_2 = [{
            "agent_id": os.environ.get("agent_id"),
            "search_opt": {
                "node_id_list": [
                    os.environ.get('node_id_1'),
                    os.environ.get('node_id')
                ]
            },
            "is_details_required": 0,
            "page_no": 1,
            "number_per_page": 50
        }, ['res["code"]==0', 'len(res["data"]["rows"])==2'],
            {}]
        self.param_001_3 = [{
            # 获取回复详情
            "agent_id": os.environ.get("agent_id"),
            "is_details_required": 1,
            "page_no": 1,
            "number_per_page": 10
        }, ['res["code"]==0'],
            {}]
        self.param_001_4 = [{
            "agent_id": os.environ.get("agent_id"),
            "is_details_required": 0,
            "page_no": 1,
            "number_per_page": 10
        }, ['res["code"]==0', 'len(res["data"]["rows"])==3'],
            {}]
        self.param_001_5 = [{
            "agent_id": os.environ.get("agent_id"),
            "is_details_required": 1,
            "page_no": 1,
            "number_per_page": 10
        }, ['res["code"]==0', 'len(res["data"]["rows"])==4', 'res["data"]["rows"][1]["node_order"] in [0,1,2]'],
            {}]
        self.param_001_6 = [{
            "agent_id": os.environ.get("agent_id"),
            "is_details_required": 0,
            "page_no": 1,
            "number_per_page": 10
        }, ['res["code"]==0', 'len(res["data"]["rows"])==1'],
            {}]
        self.param_001_7 = [{
            "is_details_required": 0,
            "page_no": 1,
            "number_per_page": 10
        }, ['res["code"]==10009',
            'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
            'res["data"][0]["msg"]=="field required"'],
            {}]
        self.param_001_8 = [{
            "agent_id": os.environ.get('agent_id'),
            "is_details_required": 0,
            "page_no": 1,
        }, ['res["code"]==10009',
            'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="number_per_page"',
            'res["data"][0]["msg"]=="field required"'],
            {}]

        # </editor-fold>

        # <editor-fold desc = "创建节点">
        self.param_004 = [{
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": "测试",
            "node_order": 1,
            "parent_node_id": os.environ.get('trigger_node_id'),
        },
            ["res['code']==0", "res['msg']=='节点创建成功'", "res['data']!=None"],
            {'node_id': 'res["data"]["node_id"]'}
        ]
        self.param_004_1 = [{
            # 创建回复节点
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": get_str(4),
            "node_order": 1,
            "trigger_intent_ids": [os.environ.get("intent_id")],
            'parent_node_id': os.environ.get('trigger_node_id'),
            "prompts":
                {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_type_id": 2,
                            "resp_content": "节点1回复"
                        }
                    ]
                }

        },
            ["res['code']==0", "res['msg']=='节点创建成功'", "res['data']!=None"],
            {'node_id_1': 'res["data"]["node_id"]'}
        ]
        self.param_004_2 = [{
            # 创建回复子节点
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_order": 1,
            "node_name": get_str(4),
            "trigger_intent_ids": [os.environ.get("intent_id")],
            'parent_node_id': os.environ.get('node_id_1'),
            "prompts":
                {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_type_id": 2,
                            "resp_content": "节点2回复"
                        }
                    ]
                }

        },
            ["res['code']==0", "res['msg']=='节点创建成功'", "res['data']!=None"],
            {'node_id': 'res["data"]["node_id"]'}
        ]
        self.param_004_2_1 = [{
            # 创建回复子节点
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": get_str(4),
            "node_order": 2,
            "trigger_intent_ids": [os.environ.get("intent_id")],
            'parent_node_id': os.environ.get('node_id_1'),
            "prompts":
                {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_type_id": 2,
                            "resp_content": "节点3回复"
                        }
                    ]
                }

        },
            ["res['code']==0", "res['msg']=='节点创建成功'", "res['data']!=None"],
            {'node_id': 'res["data"]["node_id"]'}
        ]
        self.param_004_2_2 = [{
            # 绑定实体
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": get_str(4),
            "node_order": 1,
            "trigger_intent_ids": [os.environ.get("intent_id")],
            'parent_node_id': os.environ.get('trigger_node_id'),
            'trigger_entities': [
                {
                    'entity_id': os.environ.get('entity_id'),
                    'entity_value_id': os.environ.get('entity_value_id'),
                    'entity_type_id': os.environ.get('entity_type'),
                    'entity_value': os.environ.get('entity_value')
                }
            ],
            "prompts":
                {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_type_id": 2,
                            "resp_content": "节点3回复"
                        }
                    ]
                }

        },
            ["res['code']==0", "res['msg']=='节点创建成功'", "res['data']!=None"],
            {'node_id': 'res["data"]["node_id"]'}
        ]
        self.param_004_2_3 = [{
            # 绑定实体必填项
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": get_str(4),
            "node_order": 1,
            "trigger_intent_ids": [os.environ.get("intent_id")],
            'parent_node_id': os.environ.get('trigger_node_id'),
            'trigger_entities': [
                {
                    'entity_value_id': os.environ.get('entity_value_id'),
                    'entity_type_id': os.environ.get('entity_type'),
                    'entity_value': os.environ.get('entity_value')
                }
            ],
            "prompts":
                {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_type_id": 2,
                            "resp_content": "节点3回复"
                        }
                    ]
                }

        },
            ["res['code']==10009", "res['msg']=='接口参数验证出错'", "res['data'][0]['loc'][3]=='entity_id'"],
            {}
        ]
        self.param_004_2_4 = [{
            # 绑定实体必填项
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": get_str(4),
            "node_order": 1,
            "trigger_intent_ids": [os.environ.get("intent_id")],
            'parent_node_id': os.environ.get('trigger_node_id'),
            'trigger_entities': [
                {
                    'entity_id': os.environ.get('entity_id'),
                    'entity_value_id': os.environ.get('entity_value_id'),
                    'entity_value': os.environ.get('entity_value')
                }
            ],
            "prompts":
                {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_type_id": 2,
                            "resp_content": "节点3回复"
                        }
                    ]
                }

        },
            ["res['code']==10009", "res['msg']=='接口参数验证出错'", "res['data'][0]['loc'][3]=='entity_type_id'"],
            {}
        ]

        self.param_004_3 = [{
            # None
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": "测试",
            "parent_node_id": os.environ.get('trigger_node_id'),
        },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
             'res["data"][0]["msg"]=="field required"'],
            {}
        ]
        self.param_004_4 = [{
            # None
            "agent_id": os.environ.get('agent_id'),
            "node_name": "测试",
            "parent_node_id": os.environ.get('trigger_node_id'),
        },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="skill_one_id"',
             'res["data"][0]["msg"]=="field required"'],
            {}
        ]
        self.param_004_5 = [{
            # None
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "parent_node_id": os.environ.get('trigger_node_id'),
        },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="node_name"',
             'res["data"][0]["msg"]=="field required"'],
            {}
        ]
        self.param_004_6 = [{
            # None
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": "测试",
        },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="parent_node_id"',
             'res["data"][0]["msg"]=="field required"'],
            {}
        ]
        self.param_004_7 = [{
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": get_str(128),
            "parent_node_id": os.environ.get('trigger_node_id'),
        },
            ["res['code']==0", "res['msg']=='节点创建成功'", "res['data']!=None"],
            {'node_id': 'res["data"]["node_id"]'}
        ]
        self.param_004_8 = [{
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": get_str(129),
            "parent_node_id": os.environ.get('trigger_node_id'),
        },
            [
                'res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="node_name"',
                'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'
            ],
            {}
        ]
        # </editor-fold>

        # <editor-fold desc = "set_up">
        """
        set_up
        """
        # 登陆
        self.param_005 = [
            {
                "username": "laiye",
                "password": "123123",
                "is_keep_login": True
            },
            [],
            {'token': 'res["data"]["jwt_token"]'}
        ]
        # 创建app
        self.param_006 = [
            {
                "agent_name": get_str(4),
                "agent_detail": "测试",
                "agent_logo": "string",
                "lang": "zh-CN"
            },
            ['res["code"]==0', 'res["msg"]=="机器人创建成功"', 'res["data"]["agent_id"]!=None'],
            {'agent_id': 'res["data"]["agent_id"]'}
        ]
        # 创建意图
        self.param_007 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "intent_name": '测试意图',
                "examples": [
                    {
                        "id": 0,
                        "name": "相似问测试"
                    }
                ],
                "keywords_eq": [
                    {
                        "id": 0,
                        "name": "严格"
                    }
                ],
                "keywords_include": [
                    {
                        "id": 0,
                        "name": "包含"
                    }
                ]
            },
            ['res["code"]==0', 'res["msg"]=="创建意图成功"'],
            {'intent_id': 'res["data"]["intent_id"]'}

        ]
        # 技能
        self.param_003 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "category_id": 4,
                "intent_id": os.environ.get('intent_id'),
                "skill_type": 1,
                "skill_content": {
                    "skill_name": get_str(4),
                    "description": get_str(4)
                }},
            ['res["data"]["agent_id"] == int(os.environ.get("agent_id"))', 'res["data"]["skill_id"] != ""'],
            {"skill_one_id": 'res["data"]["skill_one_id"]'}]

        # </editor-fold>

        # <editor-fold desc = "意图">
        self.param_007_1 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "intent_name": '节点1意图',
                "examples": [
                    {
                        "id": 0,
                        "name": "节点1"
                    }
                ],
                "keywords_eq": [
                    {
                        "id": 0,
                        "name": "严格1"
                    }
                ],
                "keywords_include": [
                    {
                        "id": 0,
                        "name": "包含1"
                    }
                ]
            },
            ['res["code"]==0', 'res["msg"]=="创建意图成功"'],
            {'intent_id': 'res["data"]["intent_id"]'}

        ]
        self.param_007_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "intent_name": get_str(4),
                "examples": [
                    {
                        "id": 0,
                        "name": "节点2"
                    }
                ],
                "keywords_eq": [
                    {
                        "id": 0,
                        "name": "严格2"
                    }
                ],
                "keywords_include": [
                    {
                        "id": 0,
                        "name": "包含2"
                    }
                ]
            },
            ['res["code"]==0', 'res["msg"]=="创建意图成功"'],
            {'intent_id': 'res["data"]["intent_id"]'}

        ]
        # </editor-fold>

        # <editor-fold desc = "获取预置节点">
        self.param_009 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),

            },
            ['res["code"]==0'],
            {'trigger_node_id': 'res["data"]["trigger_node"]["node_id"]',
             "complete_node_name": 'res["data"]["complete_node"]["node_name"]',
             "fallback_node_name": 'res["data"]["fallback_node"]["node_name"]'}
        ]
        # </editor-fold>

        # <editor-fold desc = "更新节点">
        self.param_010 = [
            {  # 更新root节点
                "node_id": os.environ.get('trigger_node_id'),
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "trigger_intent_ids": [os.environ.get('intent_id')],
                "prompts": {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_content": "跟节点回复",
                            "resp_type_id": 2
                        }
                    ]
                }
            }
            , ['res["code"]==0', 'res["msg"]=="节点更新成功"'], {}

        ]
        self.param_010_1 = [
            {  # 更新成功结束节点
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_name": os.environ.get('complete_node_name'),
                "responses": {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_content": "成功结束回复",
                            "resp_type_id": 2
                        }
                    ]
                }
            }
            , ['res["code"]==0', 'res["msg"]=="节点更新成功"',
               'res["data"]["node_name"]==os.environ.get("complete_node_name")'], {}

        ]
        self.param_010_2 = [
            {  # 更新失败结束节点
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_name": os.environ.get('fallback_node_name'),
                "prompts": {
                    "agent_id": os.environ.get('agent_id'),
                    "responses": [
                        {
                            "resp_content": "失败结束回复",
                            "resp_type_id": 2
                        }
                    ]
                }
            }
            , ['res["code"]==0', 'res["msg"]=="节点更新成功"'], {}

        ]
        # </editor-fold>

        # <editor-fold desc = "删除节点">
        self.param_011 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_id": os.environ.get('node_id')
            }, ['res["code"]==0', 'res["msg"]=="节点删除成功"', 'res["data"]["rowcount"]==1'], {}
        ]
        self.param_011_1 = [
            {
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_id": os.environ.get('node_id')
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.param_011_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "node_id": os.environ.get('node_id')
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="skill_one_id"',
                'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.param_011_3 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="node_id"',
                'res["data"][0]["msg"]=="field required"'], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "获取指定节点">
        self.param_012 = [
            {  # 获取指定节点
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_id": os.environ.get('node_id')
            }, ['res["code"]==0', 'res["data"]!=None'], {}
        ]
        self.param_012_1 = [
            {
                # 获取跟节点
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),

            }, ['res["code"]==0', 'res["data"]!=None'], {}
        ]
        self.param_012_2 = [
            {
                "skill_one_id": os.environ.get('skill_one_id'),

            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.param_012_3 = [
            {
                "agent_id": os.environ.get('agent_id'),

            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="skill_one_id"',
                'res["data"][0]["msg"]=="field required"'], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "获取指定节点的子节点">
        self.param_013 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_id": os.environ.get('node_id'),
                "page_no": 1,
                "number_per_page": 5
            }, ['res["code"]==0', 'res["data"]["node_name"]=="测试"'], {}
        ]
        self.param_013_1 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_id": os.environ.get('node_id'),
                "page_no": 1,
                "number_per_page": 5
            }, ['res["code"]==0', 'res["data"]["node_name"]=="测试"',
                'res["data"]["prompts"]["responses"][0]["resp_content"]=="节点1回复"'], {}
        ]
        self.param_013_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_id": os.environ.get('node_id_1'),
                "page_no": 1,
                "number_per_page": 5
            }, ['res["code"]==0', 'res["data"]["count"]==2', "len(res['data']['rows'])==2"], {}]

        self.param_013_3 = [
            {
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_id": os.environ.get('node_id_1'),
                "page_no": 1,
                "number_per_page": 5
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'], {}]
        self.param_013_4 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "node_id": os.environ.get('node_id_1'),
                "page_no": 1,
                "number_per_page": 5
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="skill_one_id"',
                'res["data"][0]["msg"]=="field required"'], {}]
        self.param_013_5 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "page_no": 1,
                "number_per_page": 5
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="node_id"',
                'res["data"][0]["msg"]=="field required"'], {}]
        self.param_013_6 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "node_id": os.environ.get('node_id_1'),
                "page_no": 1,
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="number_per_page"',
                'res["data"][0]["msg"]=="field required"'], {}]

        # </editor-fold>

        # del app
        self.param_008 = [
            {
                "agent_id": os.environ.get("agent_id")
            },
            ['res["code"]==0'],
            {}

        ]
