# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : botfallbackconfig_base.py
# DATE : 2021/7/20 15:02
from base_case import *
from modules.logger import log
from modules.request_base import *


class botfallbackconfig_base_class:

    @classmethod
    def __botfallbackconfig_base(cls, url, data):
        """
        机器人回复策略基础用例
        """
        log.info(f"senddata:{data}")
        res = rear_post(url, data)
        con = res.content.decode()
        log.info(f"res:{con}")
        return con

    @classmethod
    def get_config(cls, data):
        """
        获取对话机器人兜底策略
        """
        url = "/v1/fallback_config/get_config"
        res = cls.__botfallbackconfig_base(url, data)
        return res

    @classmethod
    def update_config(cls, data):
        """
        新建及修改机器人兜底策略
        """
        url = "/v1/fallback_config/update_config"
        res = cls.__botfallbackconfig_base(url, data)
        return res