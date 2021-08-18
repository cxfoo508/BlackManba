from base_case import *
from modules.logger import log

class SlotCaseBase:
    @classmethod
    def __slot_base(cls, url, data):
        """
        slot case
        """
        log.info(f"send data: {data}")
        res = rear_post(url, data)
        con = res.content.decode()
        log.info(f"res: {con}")
        return con

    @classmethod
    def slot_create(cls, data):
        """
        创建词槽
        """
        url = "/v1/slot/create"
        return cls.__slot_base(url, data)

    @classmethod
    def slot_update(cls, data):
        """
        升级词槽
        """
        url = "/v1/slot/update"
        return cls.__slot_base(url, data)

    @classmethod
    def slot_del(cls, data):
        """
        del slot
        """
        url = "/v1/slot/del"
        return cls.__slot_base(url, data)

    @classmethod
    def slot_list(cls, data):
        """
        get slot list
        """
        url = "/v1/slot/list"
        return cls.__slot_base(url, data)

    @classmethod
    def slot_ref_skills(cls, data):
        """
        获取引用词槽的技能列表
        """
        url = '/v1/slot/ref_skills'
        return cls.__slot_base(url, data)
