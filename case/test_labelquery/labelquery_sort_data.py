# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : labelquery_sort_data.py
# DATE : 2021/8/6 18:31
class labelquery_sort_class:


    # 接口初始化操作
    entity_setup_class = {"sort":["auth_login", "creat_app"],
                            'params':['labelquery_data_class.setup_login', 'labelquery_data_class.setup_create_app']}
    # 接口收尾工作
    entity_teardown_class = {"sort": ["del_app"], 'params': ['labelquery_data_class.teardown_class']}
    # 场景化用例操作
    entity_scenario_case_001 = {"sort": [],
                                  "params": []}
    param_list = dir()

    @classmethod
    def get_labelquery_list(cls, parm_name=None) -> list:
        lists = []
        if parm_name is None:
            for i in cls.param_list:
                if "case" in i:
                    lists.append('labelquery_sort_class.' + i)
        else:
            for item in cls.param_list:
                if parm_name in item:
                    lists.append('labelquery_sort_class.' + item)
        return lists


if __name__ == "__main__":
    pass