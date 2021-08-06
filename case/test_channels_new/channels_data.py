# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : channels_data.py
# DATE : 2021/8/6 18:29
import os
from data_method import *


class channels_data_class:

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
        # <editor-fold desc="新增渠道">
        self.param_create_channels_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="更新渠道">
        self.param_update_channels_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="删除渠道">
        self.param_delete_channels_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="获取渠道">
        self.param_get_channels_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="获取渠道列表">
        self.param_get_channelslist_001 = [{}, [], {}]
        # </editor-fold>