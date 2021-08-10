# coding = utf-8

import pandas
import pytest

from case.pytest_base import PyBase
from case.test_app.app_sort_data import app_sort_class

agent_id = []


def get_py_data():
    data_list = app_sort_class.get_node_list()
    return data_list


class TestCase(PyBase):

    def setup_class(self):
        self.run('app_sort_class.set_up_login')

    @pytest.fixture(params=get_py_data())
    def creat_data(self, request):
        return request.param

    def test01_app_creat(self, creat_data):
        """
        测试创建app
        """
        self.run(creat_data)

