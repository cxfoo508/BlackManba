# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : intents_base.py.py
# DATE : 2021/7/19 11:51
from base_case import *
from modules.logger import log
from modules.request_base import *

class intents_base_class:

    @classmethod
    def __intents_base(cls, url, data):
        """
        意图基础用例
        """
        log.info(f"send data:{data}")
        res = rear_post(url, data)
        con = res.content.decode()
        log.info(f"res:{con}")
        return con

    @classmethod
    def intents_list(cls, data):
        """
        意图列表
        """
        url = "/v1/intents/list"
        res = cls.__intents_base(url, data)
        return res

    @classmethod
    def intents_detail(cls, data):
        """
        意图详情页面
        """
        url = "/v1/intents/detail"
        res = cls.__intents_base(url, data)
        return res

    @classmethod
    def create_intents(cls, data):
        """
        新建意图
        """
        url = "/v1/intents/create"
        res = cls.__intents_base(url, data)
        return res

    @classmethod
    def edit_intents(cls, data):
        """
        编辑意图
        """
        url = "/v1/intents/edit"
        res = cls.__intents_base(url, data)
        return res

    @classmethod
    def del_intents(cls, data):
        """
        删除意图
        """
        url = "/v1/intests/delete"
        res = cls.__intents_base(url, data)
        return res