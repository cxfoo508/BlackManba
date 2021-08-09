# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : entity_data.py
# DATE : 2021/8/5 19:18
import os
from data_method import *


class entity_data_class:

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
        # </editor-fold>
        # <editor-fold desc="新增实体参数">
        self.param_create_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="更新实体参数">
        self.param_update_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="删除实体参数">
        self.param_delete_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="新增实体值参数">
        self.param_create_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="更新实体值参数">
        self.param_update_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="删除实体值参数">
        self.param_delete_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="获取实体列表参数">
        self.param_get_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="获取实体值列表参数">
        self.param_get_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="导入实体参数">
        self.param_import_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="导出实体参数">
        self.param_export_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="导入实体值参数">
        self.param_port_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="导出实体值参数">
        self.param_export_entityvalue_001 = [{}, [], {}]
        # </editor-fold>
