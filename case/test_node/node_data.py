import os

from data_method import *


class node_data_class:
    def __init__(self):
        """
        节点参数
        """

        """
        获取节点列表
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
        }, [],
            {}]

        """
        创建技能
        """
        self.param_003 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "category_id": 4,
                "intent_id": os.environ.get('intent_id'),
                "skill_type": 1,
                "skill_content": {
                    "skill_name": get_str(4),
                    "description": "描述"
                }},
            [], {"skill_one_id": 'res["data"]["skill_one_id"]'}]

        """
        创建节点
        """
        self.param_004 = [{
            "agent_id": os.environ.get('agent_id'),
            "skill_one_id": os.environ.get('skill_one_id'),
            "node_name": "测试",
        },
         [],
         {}
        ]
