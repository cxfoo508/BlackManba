# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : channels_base.py
# DATE : 2021/7/27 13:58
from base_case import *
from modules.logger import log
from modules.request_base import *
from modules.request_base import request_data_channel
class channels_base_class:

    @classmethod
    def __channels_base_token(cls, url, data):
        """
        渠道基础用例
        """
        log.info(f"send data:{data}")
        res = rear_post(url, data)
        con = res.content.decode()
        log.info(f"res:{con}")
        return con

    @classmethod
    def __channels_base_acctoken(cls, url, data):
        log.info(f"send data:{data}")
        res = request_data_channel(url, data)
        con = res.content.decode()
        log.info(f"res:{con}")
        return con

    @classmethod
    def get_channels_detail(cls, data):
        """
        获取渠道类型
        """
        url = "/v1/channels/detail"
        res = cls.__channels_base_token(url, data)
        return res

    @classmethod
    def get_channels_auth(cls, data):
        """
        获取渠道全鉴Token
        """
        url = "/v1/channels/auth"
        res = cls.__channels_base_token(url, data)
        return res

    @classmethod
    def create_channels_user(cls, data):
        """
        创建渠道用户
        """
        url = "/v1/channels/user/create"
        res = cls.__channels_base_acctoken(url, data)
        return res

    @classmethod
    def get_channels_user(cls, data):
        """
        获取渠道用户信息
        """
        url = "/v1/channels/user/get"
        res = cls.__channels_base_acctoken(url, data)
        return res

    @classmethod
    def get_channels_response(cls, data):
        """
        获取机器人对话回复
        """
        url = "/v1/channels/msg/bot_response"
        res = cls.__channels_base_acctoken(url, data)
        return res

