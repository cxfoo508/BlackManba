# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : channels_sort_data.py
# DATE : 2021/7/27 13:59
from base_case import *
# from request_base import *
from modules.request_base import *

class channels_sort_class:

    # 获取渠道信息参数接口
    channels_case_001 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_001"]}
    channels_case_002 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_002"]}
    channels_case_003 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_003"]}
    channels_case_004 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_004"]}
    channels_case_005 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_005"]}
    channels_case_006 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_006"]}
    channels_case_007 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_007"]}
    channels_case_008 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_008"]}
    channels_case_009 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_009"]}
    channels_case_010 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_010"]}
    channels_case_011 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_011"]}
    channels_case_012 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_012"]}
    channels_case_013 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_013"]}
    channels_case_014 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_014"]}
    channels_case_015 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_015"]}
    channels_case_016 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_016"]}
    channels_case_017 = {"sort": ["channels_base_class.get_channels_detail"], "params": ["channels_data_class.param_get_detail_017"]}
    # 获取鉴权token
    channels_case_018 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_001"]}
    channels_case_019 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_002"]}
    channels_case_020 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_003"]}
    channels_case_021 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_004"]}
    channels_case_022 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_005"]}
    channels_case_023 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_006"]}
    channels_case_024 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_007"]}
    channels_case_025 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_008"]}
    channels_case_026 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_009"]}
    channels_case_027 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_010"]}
    channels_case_028 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_011"]}
    channels_case_029 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_012"]}
    channels_case_030 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_013"]}
    channels_case_031 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_014"]}
    channels_case_032 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_015"]}
    channels_case_033 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_016"]}
    channels_case_034 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_017"]}
    channels_case_035 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_018"]}
    channels_case_036 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_019"]}
    channels_case_037 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_020"]}
    channels_case_038 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_021"]}
    channels_case_039 = {"sort": ["channels_base_class.get_channels_auth"], "params": ["channels_data_class.param_get_auth_022"]}
    # 创建渠道用户
    channels_case_040 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_001"]}
    channels_case_041 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_002"]}
    channels_case_042 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_003"]}
    channels_case_043 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_004"]}
    channels_case_044 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_005"]}
    channels_case_045 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_006"]}
    channels_case_046 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_007"]}
    channels_case_047 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_008"]}
    channels_case_048 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_009"]}
    channels_case_049 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_010"]}
    channels_case_050 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_011"]}
    channels_case_051 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_012"]}
    channels_case_052 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_013"]}
    channels_case_053 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_014"]}
    channels_case_054 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_015"]}
    channels_case_055 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_016"]}
    channels_case_056 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_017"]}
    channels_case_077 = {"sort": ["channels_base_class.create_channels_user"], "params": ["channels_data_class.param_create_user_018"]}
    # 获取渠道用户
    channels_case_057 = {"sort": ["channels_base_class.get_channels_user"], "params": ["channels_data_class.param_get_user_001"]}
    channels_case_058 = {"sort": ["channels_base_class.get_channels_user"], "params": ["channels_data_class.param_get_user_002"]}
    channels_case_059 = {"sort": ["channels_base_class.get_channels_user"], "params": ["channels_data_class.param_get_user_003"]}
    channels_case_060 = {"sort": ["channels_base_class.get_channels_user"], "params": ["channels_data_class.param_get_user_004"]}
    channels_case_061 = {"sort": ["channels_base_class.get_channels_user"], "params": ["channels_data_class.param_get_user_005"]}
    channels_case_062 = {"sort": ["channels_base_class.get_channels_user"], "params": ["channels_data_class.param_get_user_006"]}
    channels_case_063 = {"sort": ["channels_base_class.get_channels_user"], "params": ["channels_data_class.param_get_user_007"]}
    # 获取渠道答复
    channels_case_064 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_001"]}
    channels_case_065 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_002"]}
    channels_case_066 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_003"]}
    channels_case_067 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_004"]}
    channels_case_068 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_005"]}
    channels_case_069 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_006"]}
    channels_case_070 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_007"]}
    channels_case_071 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_008"]}
    channels_case_072 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_009"]}
    channels_case_073 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_010"]}
    channels_case_074 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_011"]}
    channels_case_075 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_012"]}
    channels_case_076 = {"sort": ["channels_base_class.get_channels_response"], "params": ["channels_data_class.param_get_response_013"]}
    # 接口初始化操作
    channels_setup_class = {"sort":["auth_login", "creat_app", "channels_base_class.get_channels_detail"],
                            'params':['channels_data_class.setup_login', 'channels_data_class.setup_create_app', 'channels_data_class.param_get_detail_017']}
    channels_setup_class_auth = {"sort": ["channels_base_class.get_channels_auth"], "params":['channels_data_class.param_get_auth_022']}
    # 接口收尾工作
    channels_teardown_class = {"sort": ["del_app"], 'params': ['channels_data_class.teardown_class']}
    # 场景化用例操作
    channels_scenario_case_001 = {"sort": ["channels_base_class.create_channels_user", "channels_base_class.get_channels_user", "channels_base_class.get_channels_response"],
                                  "params": ["channels_data_class.param_create_user_010", "channels_data_class.param_get_user_007", "channels_data_class.param_get_response_012"]}
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