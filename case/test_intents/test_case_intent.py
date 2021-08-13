# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : test_case_intent.py
# DATE : 2021/7/19 15:09
# import json
import pytest

from base_case import *
from modules.logger import log
from case.pytest_base import PyBase
from case.test_intents.inrents_sort_data import intents_sort_class
from data.data_method import *


def get_data():
    data_list = intents_sort_class.get_intents_list()
    log.info(data_list)
    return data_list

class TestCase(PyBase):

    def setup_class(self):
        """
        创建机器人
        """
        log.info("---setup class---")
        self.run(self, 'intents_sort_class.intents_setup_class')



    @pytest.fixture(params=get_data())
    def create_data(self, request):
        return request.param

    def test_intents(self, create_data):
        """
        执行测试case
        """
        self.run(create_data)

    def teardown_class(self):
        """
        删除app
        """
        log.info("---teardown_class---")
        self.run(self, 'intents_sort_class.intents_teardown_class')