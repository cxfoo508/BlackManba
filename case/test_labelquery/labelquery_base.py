# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : labelquery_base.py
# DATE : 2021/8/6 18:30
from base_case import *
from modules.logger import log
from modules.request_base import *


class labelquery_base_class:

    @classmethod
    def __labelquery_base_token(cls, method, url, data):
        """
        标签信息操作基础用例
        """
        if method == "get":
            log.info(f"send url:{url}")
            log.info(f"send data:{data}")
            res = rear_get(url, data, url_ver=2)
            con = res.content.decode()
            log.info(f"res:{con}")
            return con
        elif method == "post":
            log.info(f"send url:{url}")
            log.info(f"send data:{data}")
            res = rear_post(url, data, url_ver=2)
            con = res.content.decode()
            log.info(f"res:{con}")
            return con
        else:
            log.info("method is not allowed")

    @classmethod
    def labelQuery(cls, data):
        """
        标签信息
        """
        agent_id = data["agent_id"]
        res_data = data["data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/labelQuery"
        res = cls.__labelquery_base_token("post", url, res_data)
        return res

    @classmethod
    def labelQuery_mutate(cls, data):
        """
        标签操作
        """
        agent_id = data["agent_id"]
        res_data = data["data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/labelQueries/mutate"
        res = cls.__labelquery_base_token("post", url, res_data)
        return res

    @classmethod
    def labelQuery_search(cls, data):
        """
        标签查询
        """
        agent_id = data["agent_id"]
        res_data = data["data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/labelQueries/search"
        res = cls.__labelquery_base_token("post", url, res_data)
        return res