# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : test_channels_new.py
# DATE : 2021/8/6 18:29
import pytest

from modules.logger import log
from case.pytest_base import PyBase
from case.test_channels_new.channels_sort_data import channels_sort_new_class
from data.data_method import *
from modules.request_base import *
from base_case import *


def get_data():
    data_list = channels_sort_new_class.get_channels_list()
    log.info(data_list)
    return data_list

class TestCase(PyBase):

    def setup_class(self):
        """
        获取渠道鉴权token
        """
        log.info("---setup class---")
        self.run(self, "channels_sort_new_class.channels_setup_class")


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
        self.run(self, "channels_sort_new_class.channels_teardown_class")