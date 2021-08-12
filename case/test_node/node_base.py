from modules.logger import log
from modules.request_base import rear_post


class node_base_class:

    @classmethod
    def __node_base(cls, url, data):
        """
        slot case
        """

        log.info(f"send data:{data}")
        res = rear_post(url, data)
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
        更新
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
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def get_dialog_tree_root_node(cls, data):
        """
        获取跟节点
        """
        url = "/v1/rule/get_base_node_for_dialog_tree"
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def update_dialog_tree_root_node(cls, data):
        """
        更新跟节点
        """
        url = '/v1/rule/update_trigger_node_with_skill'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def update_dialog_tree_complete_node(cls, data):
        """
        更新成功结束节点
        """
        url = '/v1/rule/update_complete_node_with_skill'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def update_dialog_tree_fallback_node(cls, data):
        """
        更新异常结束节点
        """
        url = '/v1/rule/update_fallback_node_with_skill'
        con = cls.__node_base(url, data)
        return con
