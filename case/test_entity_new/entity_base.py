# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : entity_base.py
# DATE : 2021/8/5 19:18
from base_case import *
from modules.logger import log
from modules.request_base import *


class entity_base_class:

    @classmethod
    def __entity_base_token(cls, method, url, data):
        """
        新实体基础用例
        """
        if method == "get":
            log.info(f"send url:{url}")
            log.info(f"send data:{data}")
            res = rear_get(url, data)
            con = res.content.decode()
            return con
        elif method == "post":
            log.info(f"send url:{url}")
            log.info(f"send data:{data}")
            res = rear_post(url, data)
            con = res.content.decode()
            return con
        else:
            log.info("method is not allowed!")

    @classmethod
    def mutate_entity(cls, data):
        """
        实体及实体值公共操作请求
        """
        agent_id = data["agent_id"]
        res_data = data["res_data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/entities/mutate"
        res = cls.__entity_base_token("post", url, res_data)
        return res

    @classmethod
    def get_entity_list(cls, data):
        """
        获取实体列表数据
        """
        agent_id = data["agent_id"]
        entity_type = data["entity_type"]
        res_data = data["res_data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/entities/{entity_type}"
        res = cls.__entity_base_token("get", url, res_data)
        return res

    @classmethod
    def get_entiytvalue_list(cls, data):
        """
        获取实体值列表数据
        """
        agent_id = data["agent_id"]
        entity_id = data["entity_id"]
        res_data = data["res_data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/entities/{entity_id}/value"
        res = cls.__entity_base_token("get", url, res_data)
        return res

    @classmethod
    def export_entity(cls, data):
        """
        导出实体列表数据
        """
        agent_id = data["agent_id"]
        entity_type = data["entity_type"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/entities/{entity_type}/export"
        res = cls.__entity_base_token("get", url)
        return res

    @classmethod
    def export_entityvalue(cls, data):
        """
        导出实体值列表数据
        """
        agent_id = data["agent_id"]
        entity_id = data["entity_id"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/entities/{entity_id}/value/export"
        res = cls.__entity_base_token("get", url)
        return res

    @classmethod
    def import_entity(cls, data):
        """
        导入实体
        """
        agent_id = data["agent_id"]
        entity_type = data["entity_type"]
        res_data = data["res_data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/entities/{entity_type}/import"
        res = cls.__entity_base_token("post", url, res_data)
        return res

    @classmethod
    def import_entityvalue(cls, data):
        """
        导入实体值
        """
        agent_id = data["agent_id"]
        entity_id = data["entity_id"]
        res_data = data["res_data"]
        url = f"/chatbot/v1alpha1/agents/{agent_id}/entities/{entity_id}/value/import"
        res = cls.__entity_base_token("post", url, res_data)
        return res
