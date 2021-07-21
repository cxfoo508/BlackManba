# coding = utf-8

import pytest

from case.pytest_base import PyBase
from case.test_node.node_sort_data import node_sort_class
from modules.logger import log


def get_data():
    data_list = node_sort_class.get_node_list("node_case")
    return data_list


class TestCase(PyBase):

    def setup_class(self):
        """
        预制条件
        """
        log.info("---setup_class---")
        self.run(self, 'node_sort_class.node_set_up')

    @pytest.fixture(params=get_data())
    def creat_data(self, request):
        return request.param

    def test_node_1(self, creat_data):
        """
        执行测试case
        """
        log.info('---test start---')
        self.run(creat_data)

    def teardown_class(self):
        """
        释放预制条件
        """
        log.info("---teardown_class---")
        self.run(self, 'node_sort_class.node_teardown')


if __name__ == '__main__':
    pytest.main("-s -v test_case_node.py::TestCass")
