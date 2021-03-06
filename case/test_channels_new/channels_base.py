# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : channels_base.py
# DATE : 2021/8/6 18:28
from base_case import *
from modules.logger import log
from modules.request_base import *

class channels_base_new_class:

    @classmethod
    def __channels_base_token(cls, method, url, data=None):
        """
        新渠道基础用例
        """
        if method == "get":
            log.info(f"send url:{url}")
            res = rear_get(url, url_ver=2)
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
            log.info("method is not allowed!")

    @classmethod
    def channels_mutate(cls, data):
        """
        新渠道操作公共接口
        """
        agent_id = data["agent_id"]
        res_data = data["data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/channel:mutate"
        res = cls.__channels_base_token("post", url, res_data)
        return res

    @classmethod
    def get_channels_by_id(cls, data):
        """
        根据id获取渠道信息
        """
        agent_id = data["agent_id"]
        id = data["id"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/channel/{id}"
        res = cls.__channels_base_token("get", url)
        return res

    @classmethod
    def get_channels_list(cls, data):
        """
        获取渠道列表
        """
        agent_id = data["agent_id"]
        page = data["page"]
        pageSize = data["pageSize"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/channel/list?page={page}&pageSize={pageSize}"
        res = cls.__channels_base_token("get", url)
        return res
