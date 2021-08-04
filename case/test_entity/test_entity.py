import pytest

from case.pytest_base import PyBase
from case.test_entity.entity_sort_data import entity_sort_class
from modules.logger import log

agent_id = []


def get_py_data():
    data_list = entity_sort_class.get_entity_list('entity_case_035')
    return data_list


class TestCase(PyBase):
    def setup_class(self):
        """
        预制条件
        """
        log.info("---setup_class---")
        self.run('entity_sort_class.entity_set_up')

    @pytest.fixture(params=get_py_data())
    def creat_data(self, request):
        return request.param

    def test01_app_creat(self, creat_data):
        """
        run test case
        """
        self.run(creat_data)

    def teardown_class(self):
        """
        释放预制条件
        """
        log.info("---teardown_class---")
        self.run('entity_sort_class.node_teardown')
