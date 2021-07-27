# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : botresponse_base.py
# DATE : 2021/7/22 20:04
from base_case import *
from modules.logger import log
from modules.request_base import *

class botresponse_base_class:

    @classmethod
    def __botresponse_base(cls, url, data):
        """
        回复集基础用例
        """
        log.info(f"send data:{data}")
        res = rear_post(url, data)
        con = res.content.decode()
        log.info(f"res:{con}")
        return con

    @classmethod
    def get_response_type(cls, data):
        """
        获取对话机器人回复类型列表
        """
        url = "/v1/response/response_type"
        res = cls.__botresponse_base(url, data)
        return res

    @classmethod
    def get_responses_mode(cls, data):
        """
        获取对话机器人回复集类型列表
        """
        url = "/v1/response/responses_type"
        res = cls.__botresponse_base(url, data)
        return res

    @classmethod
    def get_responses_mode(cls, data):
        """
        获取对话回复集模式列表
        """
        url = "/v1/response/responses_mode"
        res = cls.__botresponse_base(url, data)
        return res

    @classmethod
    def get_custom_action(cls, data):
        """
        获取系统内置自定义动作回复
        """
        url = "/v1/response/custom_action"
        res = cls.__botresponse_base(url, data)
        return res

    @classmethod
    def get_responses(cls, data):
        """
        根据id获取回复集
        """
        url = "/v1/response/get_responses"
        res = cls.__botresponse_base(url, data)
        return res

    @classmethod
    def update_responses(cls, data):
        """
        新建或者更新回复集
        """
        url = "/v1/response/update_responses"
        res = cls.__botresponse_base(url, data)
        return res

    @classmethod
    def delete_responses(cls, data):
        """
        删除回复集
        """
        url = "/v1/response/delete_responses"
        res = cls.__botresponse_base(url, data)
        return res
