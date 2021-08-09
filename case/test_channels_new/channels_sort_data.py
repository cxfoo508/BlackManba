# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : channels_sort_data.py
# DATE : 2021/8/6 18:29
class channels_sort_class:


    # 接口初始化操作
    channels_setup_class = {"sort":["auth_login", "creat_app"],
                            'params':['channels_data_class.setup_login', 'channels_data_class.setup_create_app']}
    # 接口收尾工作
    channels_teardown_class = {"sort": ["del_app"], 'params': ['channels_data_class.teardown_class']}
    # 场景化用例操作
    channels_scenario_case_001 = {"sort": [], "params": []}
    param_list = dir()

    @classmethod
    def get_channels_list(cls, parm_name=None) -> list:
        lists = []
        if parm_name is None:
            for i in cls.param_list:
                if "case" in i:
                    lists.append('channels_sort_class.' + i)
        else:
            for item in cls.param_list:
                if parm_name in item:
                    lists.append('channels_sort_class.' + item)
        return lists


if __name__ == "__main__":
    pass