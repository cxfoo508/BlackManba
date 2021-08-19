from modules.logger import log
from modules.request_base import rear_post


class skills_base_class:

    @classmethod
    def __skills_base(cls, url, data):
        """
        slot case
        """

        log.info(f"send data:{data}")
        res = rear_post(url, data)
        con = res.content.decode()
        log.info(f"res:{con}")
        return con

    @classmethod
    def skill_list(cls, data=None):
        """
        获取技能列表
        """
        url = '/v1/skills/list'
        res = cls.__skills_base(url,data)
        return res

    @classmethod
    def skill_change_status(cls, data=None):
        """
        技能是否生效
        """
        url = '/v1/skills/change_status'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_create(cls, data=None):
        """
        创建技能
        """
        url = '/v1/skills/create'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_set(cls, data=None):
        """
        设置技能
        """
        url = '/v1/skills/set_skill'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_detail_set(cls, data=None):
        """
        获取单个设置技能设置信息
        """
        url = '/v1/skills/detail_set_skill'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_delete(cls, data=None):
        """
        删除技能
        """
        url = '/v1/skills/delete'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_detail(cls, data=None):
        """
        获取技能信息
        """
        url = '/v1/skills/detail'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_detail_by_id_list(cls, data=None):
        """
        获取技能信息-通过技能id数组
        """
        url = '/v1/skills/detail/by_id_list'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_edit(cls, data=None):
        """
        编辑技能
        """
        url = '/v1/skills/edit'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_category_tag(cls, data=None):
        """
        获取分类树任意节点的子节点数据
        """
        url = '/v1/skills/category/tag'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_category_create(cls, data=None):
        """
        创建分类节点
        """
        url = '/v1/skills/category/create'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_category_delete(cls, data=None):
        """
        删除分类节点
        """
        url = '/v1/skills/category/delete'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_category_edit(cls, data=None):
        """
        修改分类节点
        """
        url = '/v1/skills/category/edit'
        res = cls.__skills_base(url, data)
        return res

    @classmethod
    def skill_category_all(cls, data=None):
        """
        获取机器人下分类树全部节点
        """
        url = '/v1/skills/category/all'
        res = cls.__skills_base(url, data)
        return res





