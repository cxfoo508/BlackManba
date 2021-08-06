# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : test_case_entity_new.py
# DATE : 2021/8/5 19:17
import pytest

from modules.logger import log
from case.pytest_base import PyBase
from case.test_entity_new.entity_sort_data import entity_sort_class
from data_method import *
from request_base import *
from base_case import *


def get_data():
    data_list = entity_sort_class.get_entity_list()
    log.info(data_list)
    return data_list

class TestCase(PyBase):

    def setup_class(self):
        """
        获取渠道鉴权token
        """
        log.info("---setup class---")
        self.run(self, "entity_sort_class.entity_setup_class")


    @pytest.fixture(params=get_data())
    def create_data(self, request):
        return request.param

    def test_channels(self, create_data):
        """
        执行测试case
        """
        self.run(create_data)

    def teardown_class(self):
        """
        删除app
        """
        log.info("---teardown_class---")
        self.run(self, "entity_sort_class.entity_teardown_class")
