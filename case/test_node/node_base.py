from base_case import *
from log.log_method import MyLog

log = MyLog(__name__)


class node_base_class:

    @classmethod
    def __node_base(cls, url, data):
        """
        slot case
        """

        log.info(f"send data:{data}")
        res = request_data(url, data)
        con = res.content.decode()
        log.info(f"res:{con}")
        return con

    @classmethod
    def create_skills(cls, data):
        """
        创建技能
        """
        url = '/v1/skills/create'
        res = cls.__node_base(url, data)
        return res

    @classmethod
    def node_list(cls, data):
        """
        获取节点列表
        """
        url = '/v1/node/list'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def node_getnode(cls, data):
        """
        获取制定节点
        """
        url = '/v1/node/getnode'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def node_getchilds(cls, data):
        """
        获取制定节点的字
        """
        url = '/v1/node/getchilds'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def node_create(cls, data):
        """
        创建节点
        """
        url = '/v1/node/create'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def node_update(cls, data):
        """
        创建
        """
        url = '/v1/node/update'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def node_del(cls, data):
        """
        删除节点
        """
        url = '/v1/node/del'
        con = cls.__node_base(data)
        return con
