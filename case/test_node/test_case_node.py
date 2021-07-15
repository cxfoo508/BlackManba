# coding = utf-8
import json

import pytest


from base_case import *
from case.test_node.node_sort_data import node_sort_class
from data_method import *
from log.log_method import MyLog
import json
from case.pytest_base import PyBase
log = MyLog(__name__)


class TestCase(PyBase):

    def setup_class(self):
        """
        创建app ，创建意图
        """
        log.info("---setup_class---")
        log.info("---test login---")
        data = {
            "username": "laiye",
            "password": "123123",
            "is_keep_login": True
        }
        res = auth_login(data)
        con = res.content.decode()
        con_data = json.loads(con)

        os.environ["token"] = con_data["data"]["jwt_token"]

        data = {
            "agent_name": get_str(4),
            "agent_detail": "测试",
            "agent_logo": "string",
            "lang": "zh-CN"
        }
        res = creat_app(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        assert '{"code":0,"msg":"机器人创建成功","data":{"agent_id"' in con, con
        os.environ["agent_id"] = con_dict["data"]["agent_id"]
        log.info(f"Agent_id:{os.environ.get('agent_id')}")
        # 创建意图
        data = {
            "agent_id": os.environ.get('agent_id'),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 0,
                    "name": "相似问"
                }
            ],
            "keywords_eq": [
                {
                    "id": 0,
                    "name": "严格"
                }
            ],
            "keywords_include": [
                {
                    "id": 0,
                    "name": "包含"
                }
            ]
        }
        res = create_intent(data)
        con = res.content.decode()
        con_dict = json.loads(con)
        log.info(con_dict)
        os.environ["intent_id"] = str(con_dict["data"]["intent_id"])

    def get_data(self):
        data_list = node_sort_class.get_node_list()
        return data_list

    @pytest.fixture(params=get_data(None))
    def creat_data(self, request):
        return request.param

    def test_node(self, creat_data):
        """
        执行测试case
        """
        self.run(creat_data)



    def teardown_class(self):
        """
        删除app
        """
        log.info("---teardown_class---")
        data = {
            "agent_id": os.environ.get("agent_id")
        }
        res = del_app(data)
        con = res.content.decode()
        log.info(con)
        assert '"code":0' in con, con


if __name__ == '__main__':
    pytest.main("-s -v test_case_node.py::TestCass")
