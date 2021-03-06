from modules.logger import log
from modules.request_base import rear_post


class SlotCaseBase:

    @classmethod
    def __node_base(cls, url, data):
        """
        slot case
        """
        log.info(f"send data: {data}")
        res = rear_post(url, data)
        con = res.content.decode()
        log.info(f"res: {con}")
        return con

    @classmethod
    def rule_get_node_dialog_tree(cls, data):
        """
        获取对话数节点
        """
        url = '/v1/rule/get_base_node_for_dialog_tree'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def rule_update_trigger_node(cls, data):
        """
        更新出发节点
        """
        url = '/v1/rule/update_trigger_node_with_skill'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def rule_update_complete_node(cls, data):
        """
        更新正常结束node
        """
        url = '/v1/rule/update_complete_node_with_skill'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def xxx(cls, data):
        """
        更新异常结束node
        """
        url = '/v1/rule/update_fallback_node_with_skill'
        con = cls.__node_base(url, data)
        return con
