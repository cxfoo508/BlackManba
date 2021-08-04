# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : test_case_botfallbackconfig.py
# DATE : 2021/7/20 15:03
import pytest


from modules.logger import log
from case.pytest_base import PyBase
from case.test_botfallbackconfig.botfallbackconfig_sort_data import botfallbackconfig_sort_class
from data_method import *


def get_data():
    data_list = botfallbackconfig_sort_class.get_botfallbackconfig_list()
    log.info(data_list)
    return data_list

class TestCase(PyBase):

    def setup_class(self):
        """
        创建机器人
        """
        log.info("---setup class---")
        self.run(self, "botfallbackconfig_sort_class.botfallbackconfig_setup_class")



    @pytest.fixture(params=get_data())
    def create_data(self, request):
        return request.param

    def test_botfallbackconfig(self, create_data):
        """
        执行测试case
        """
        self.run(create_data)

    def teardown_class(self):
        """
        删除app
        """
        log.info("---teardown_class---")
        self.run(self, "botfallbackconfig_sort_class.botfallbackconfig_teardown_class")
