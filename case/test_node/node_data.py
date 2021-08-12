import os

from data_method import *


class node_data_class:
    def __init__(self):
        """
        节点参数
        """

        """
        call-获取节点列表
        """
        self.param_001 = [{
            "agent_id": os.environ.get("agent_id"),
            "is_details_required": 0,
            "page_no": 1,
            "number_per_page": 10
        }, ['res["code"]==200', 'res["data"]==None'],
            {}]

        self.param_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "search_opt": {
                "node_id_list": [
                    "string"
                ]
            },
            "is_details_required": 0,
            "page_no": 1,
            "number_per_page": 50
        }, ['res["code"]==200', 'res["data"]==None'],
            {}]

        """
        scene
        """
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

        # 创建节点
        self.param_004 = [{
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": "测试",
        },
            ["res['code']==0", "res['msg']=='节点创建成功'", "res['data']!=None"],
            {}
        ]
        self.param_004_1 = [{
            # 创建回复节点
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": "测试",
            "trigger_intent_ids": [os.environ.get("intent_id")],
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
            {}
        ]

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

        # <editor-fold desc = "获取预置节点">
        self.param_009 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),

            },
            ['res["code"]==0'], {'trigger_node_id': 'res["data"]["trigger_node"]["node_id"]',
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

        # del app
        self.param_008 = [
            {
                "agent_id": os.environ.get("agent_id")
            },
            ['res["code"]==0'],
            {}

        ]
