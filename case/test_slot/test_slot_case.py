# coding = utf-8

import pytest

from case.pytest_base import PyBase
from case.test_slot.slot_sort_data import slot_sort_class
from modules.logger import log


def get_data():
    data_list = slot_sort_class.get_slot_list("slot_case_004")
    return data_list


class TestCase(PyBase):

    def setup_class(self):
        """
        预制条件
        """
        log.info("---setup_class---")
        self.run('node_sort_class.node_set_up')
        self.run('entity_sort_class.entity_case_032')

    @pytest.fixture(params=get_data())
    def creat_data(self, request):
        return request.param

    def test_case(self, creat_data):
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
        self.run('node_sort_class.node_teardown')
