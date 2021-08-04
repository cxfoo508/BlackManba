# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : test_case_channels.py
# DATE : 2021/7/27 13:58
import pytest

from modules.logger import log
from case.pytest_base import PyBase
from case.test_channels.channels_sort_data import channels_sort_class
from data_method import *
from request_base import *
from base_case import *


def get_data():
    data_list = channels_sort_class.get_channels_list()
    log.info(data_list)
    return data_list

class TestCase(PyBase):

    def setup_class(self):
        """
        获取渠道鉴权token
        """
        log.info("---setup class---")
        self.run(self, "channels_sort_class.channels_setup_class")
        headers = get_headers()
        log.info(f"headers:{headers}")
        self.run(self, "channels_sort_class.channels_setup_class_auth")


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
        self.run(self, "channels_sort_class.channels_teardown_class")
