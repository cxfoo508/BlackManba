# coding = utf-8
import pytest

from case.pytest_base import PyBase
from case.test_skills.skills_sort_data import skills_sort_class
from modules.logger import log


def get_data():
    data_list = skills_sort_class.get_skills_data("skills_case_023")
    return data_list


class TestCase(PyBase):

    def setup_class(self):
        log.info('---set up---')
        self.run('skills_sort_class.skills_set_up')

    @pytest.fixture(params=get_data())
    def creat_data(self, request):
        return request.param

    def test_case_001(self, creat_data):
        self.run(creat_data)

    def teardown_class(self):
        """
        释放预制条件
        """
        log.info("---teardown_class---")
        self.run('node_sort_class.node_teardown')
