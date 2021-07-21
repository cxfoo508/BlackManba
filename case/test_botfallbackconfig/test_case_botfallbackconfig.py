# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : test_case_botfallbackconfig.py
# DATE : 2021/7/20 15:03
import pytest

from base_case import *
from modules.logger import log
from case.pytest_base import PyBase
from case.test_botfallbackconfig.botfallbackconfig_sort_data import botfallbackconfig_sort_class
from data_method import *


class TestCase(PyBase):

    def setup_class(self):
        """
        创建机器人
        """
        log.info("---setup class---")
        log.info("---test login ---")
        data = {
            "username": "laiye",
            "password": "123123",
            "is_keep_login": True
        }
        con = auth_login(data)
        con_data = json.loads(con)

        os.environ["token"] = con_data["data"]["jwt_token"]
        data = {
            "agent_name": get_str(4),
            "agent_detail": "测试",
            "agent_logo": "string",
            "lang": "zh-CN"
        }
        con = creat_app(data)
        con_dict = json.loads(con)
        assert '{"code":0,"msg":"机器人创建成功","data":{"agent_id"' in con, con
        os.environ["agent_id"] = con_dict["data"]["agent_id"]
        log.info(f"Agent_id:{os.environ.get('agent_id')}")

    def get_data(self):
        data_list = botfallbackconfig_sort_class.get_botfallbackconfig_list()
        log.info(data_list)
        return data_list

    @pytest.fixture(params=get_data(None))
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
        data = {
            "agent_id": os.environ.get("agent_id")
        }
        con = del_app(data)
        log.info(con)
        assert '"code":0' in con, con