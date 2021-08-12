# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : labelquery_data.py
# DATE : 2021/8/6 18:31
import os
from data_method import *


class labelquery_data_class:

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
        # <editor-fold desc="新建待审核">

        # </editor-fold>

        # <editor-fold desc="更新待审核">

        # </editor-fold>

        # <editor-fold desc="添加到意图">

        # </editor-fold>

        # <editor-fold desc="删除">

        # </editor-fold>

        # <editor-fold desc="">

        # </editor-fold>

        # <editor-fold desc="查找">

        # </editor-fold>