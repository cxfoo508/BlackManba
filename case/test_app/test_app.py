# coding = utf-8
import json
import uuid

import pandas
import pytest

from base_case import *
from data.creat_app_data import *
from data.create_entity import *
from data.create_entity_value import *
from data.get_entity_value_list import *
from data.update_app_data import *
from data.update_entity import *
from data.update_entity_value import *

from case.test_app.app_sort_data import app_sort_class
from case.pytest_base import PyBase
agent_id = []


def get_py_data():
    data_list = app_sort_class.get_node_list()
    return data_list


class TestCase(PyBase):
    def read_excel(self, excel_path):
        """
        pandas excel
        """

        global f, n
        n = 0
        f = pandas.read_excel(excel_path)
        num_list = [i for i in range(len(f.values))]
        data_list = f.values
        # print(data_list)
        return data_list
        # save excel
        # pandas.DataFrame(f).to_excel(excel_path,index = 0)

    def setup_method(self):
        print('---setup_method---')
        os.environ["token"] = self.auth_login()
        print(f'TOKEN:{os.environ.get("token")}')

    @pytest.fixture(params=get_py_data())
    def creat_data(self, request):
        # print('1', request.param)
        return request.param

    def test01_app_creat(self, creat_data):
        """
        测试创建app
        """
        print("---creat app---")
        self.run(creat_data)
    # def get_update_data(self):
    #     data_list = get_update_list()
    #     return data_list
    #
    # @pytest.fixture(params=get_update_data(None))
    # def update_data(self, request):
    #     return request.param

    # def test02_app_update(self, update_data):
    #     """
    #     测试机器人更新
    #     """
    #     print("---app update---")
    #     global agent_id
    #     data = eval(update_data)
    #     data[0]["agent_id"] = agent_id[0]
    #     # data[0]["agent_id"] = "121"
    #     print(data[0])
    #     res = update_app(data[0])
    #     print(f'status code:{res.status_code}')
    #     content = res.content.decode()
    #     print(res.headers)
    #     print(content)
    #     check_res = str(data[1])
    #     assert check_res in content, f'res:{content}'
    #
    # def test03_app_del(self):
    #     """
    #     删除机器人
    #     """
    #     print("---del app---")
    #     global agent_id
    #     for i in agent_id:
    #         data = {
    #             "agent_id": i
    #         }
    #         print(data)
    #         res = del_app(data)
    #         assert res.status_code == 200, f"code:{res.status_code}"
    #
    # # @pytest.mark.skip
    # def test04_app_list(self, ):
    #     """
    #     获取列表
    #     """
    #     print("---get list---")
    #     data = {
    #         "page_no": 6,
    #         "number_per_page": 20,
    #         "agent_id": 0
    #     }
    #     res = getlist_app(data)
    #     print(res.status_code)
    #     con_list = json.loads(res.content.decode())
    #     print(con_list)
    #     for i in con_list["data"]["rows"]:
    #         if i["agent_id"] == '121':
    #             print(i)
    #     assert res.status_code == 200, f'code:{res.status_code}'
    #
    # def select_agent_info(self, parm_agent_id):
    #     """
    #     查找app字段
    #     """
    #     print("---select agent info ---")
    #     num = 1
    #     while True:
    #         data = {
    #             "page_no": num,
    #             "number_per_page": 20
    #         }
    #         res = getlist_app(data)
    #         print(num)
    #         con_list = json.loads(res.content.decode())
    #         # print(f'{res.status_code}\n{con_list}')
    #         print(con_list)
    #         for i in con_list['data']['rows']:
    #             if i["agent_id"] == parm_agent_id:
    #                 return i
    #         num += 1
    #
    # def test_auth_systemInfo(self, ):
    #     """
    #     系统信息
    #     """
    #     print("---test systemInfo---")
    #     res = auth_systemInfo()
    #     print(f'response:{res.content.decode()}')
    #     print(f"header:{res.headers}")
    #
    def auth_login(self, ):
        """
        登陆
        """
        print("---test login---")
        data = {
            "username": "laiye",
            "password": "123123",
            "is_keep_login": True
        }
        con = auth_login(data)
        con_data = json.loads(con)
        return con_data["data"]["jwt_token"]
    #
    # def get_create_entity_data(self):
    #     data_list = get_create_entity_list()
    #     # print(data_list)
    #     return data_list
    #
    # @pytest.fixture(params=get_create_entity_data(None))
    # def create_entity_data(self, request):
    #     return request.param
    #
    # def test_create_entity(self, create_entity_data):
    #     """
    #     test 创建实体
    #     """
    #     print('---create entity---')
    #
    #     data = eval(create_entity_data)
    #     res = create_entity(data[0])
    #     con = res.content.decode()
    #     con_data = json.loads(con)
    #     print(con)
    #     assert data[1] in con, con
    #
    # def get_update_entity_data(self):
    #     data_list = get_update_entity_list()
    #     return data_list
    #
    # @pytest.fixture(params=get_update_entity_data(None))
    # def update_entity_data(self, request):
    #     return request.param
    #
    # def test_update_entity(self, update_entity_data):
    #     """
    #     test 更新实体
    #     """
    #
    #     print('---update entity---')
    #     data = parm_entity_001
    #     data[0]["entity_name"] = str(uuid.uuid4()).replace('-', '')
    #     res = create_entity(data[0])
    #     con = res.content.decode()
    #     con_data = json.loads(con)
    #     entity_id = con_data["data"]["entity_id"]
    #     print(con)
    #     data1 = eval(update_entity_data)
    #     keys = dict(data1[0]).keys()
    #     if 'entity_id' in keys:
    #         data1[0]["entity_id"] = entity_id
    #     res = update_entity(data1[0])
    #     con1 = res.content.decode()
    #     con_data1 = json.loads(con)
    #     print(con_data1)
    #     assert data1[1] in con1, con1
    #
    #     # 查询
    #     # 查询实体
    #     data_select = {
    #         "agent_id": "409",
    #         "entity_type": 1,
    #         "entity_id": entity_id,
    #         "page_no": 1,
    #         "number_per_page": 5
    #     }
    #     res = get_entity_list(data_select)
    #     con = res.content.decode()
    #     print(con)
    #     # 删除实体
    #     data = {
    #         "agent_id": 409,
    #         "entity_id": entity_id,
    #         "entity_type": 1
    #     }
    #     res = del_entity(data)
    #     con = res.content.decode()
    #     print(con)
    #     assert '"code":0' in con, con
    #
    # def test_entity_flow(self):
    #     """
    #     实体流程
    #     """
    #     print('---entity flow---')
    #     # 创建实体
    #     print('-创建实体-')
    #     data = parm_entity_001
    #     res = create_entity(data[0])
    #     con = res.content.decode()
    #     con_data = json.loads(con)
    #     entity_id = con_data["data"]["entity_id"]
    #     print(entity_id)
    #     # 创建value
    #     print('-创建value-')
    #     data = parm_entity_value_001
    #     data[0]["entity_id"] = entity_id
    #     res = create_entity_value(data[0])
    #     con = res.content.decode()
    #     con_data = json.loads(con)
    #     entity_value_id = con_data["data"]["entity_value_id"]
    #     print(entity_value_id)
    #     # 查询实体
    #     print('-查询-')
    #     data_select = {
    #         "agent_id": "409",
    #         "entity_type": 1,
    #         "entity_id": entity_id,
    #         "page_no": 1,
    #         "number_per_page": 5
    #     }
    #     res = get_entity_list(data_select)
    #     con = res.content.decode()
    #     print(con)
    #     assert ("409" in con) and (entity_id in con) and (entity_value_id in con) and ("测试value" in con), con
    #
    #     # 更新实体值
    #     print('-更新实体值-')
    #     update_entity_value_001[0]["entity_id"] = entity_id
    #     update_entity_value_001[0]["entity_value_id"] = entity_value_id
    #     res = update_entity_value(update_entity_value_001[0])
    #     con = res.content.decode()
    #     print(con)
    #     # 查询
    #     print('-查询-')
    #     res = get_entity_list(data_select)
    #     print(res.content.decode())
    #     # 删除实体值
    #     data = {
    #         "agent_id": 409,
    #         "entity_id": entity_id,
    #         "entity_value_id": entity_value_id,
    #         "entity_type": 1
    #     }
    #     res = del_entity_value(data)
    #     con = res.content.decode()
    #     print(con)
    #     # 删除实体
    #     print('-删除实体-')
    #     data = {
    #         "agent_id": 409,
    #         "entity_id": entity_id,
    #         "entity_type": 1
    #     }
    #     res = del_entity(data)
    #     con = res.content.decode()
    #     print(con)
    #
    #     # 查询
    #     print('-查询-')
    #     res = get_entity_list(data_select)
    #     print(res.content.decode())
    #
    # def test_get_entity_type(self):
    #     """
    #     test 获取实体类型列表
    #     """
    #     print("---get entity type---")
    #     data = {
    #         "page_no": 1,
    #         "number_per_page": 10
    #     }
    #     res = get_entity_type(data)
    #     con = res.content.decode()
    #     con_data = json.loads(con)
    #     print(con)
    #
    # def case_get_entity_value_list(self, data):
    #     """
    #     获取实体列表
    #     """
    #     res = get_entity_value_list(data)
    #     con = res.content.decode()
    #     con_data = json.loads(con)
    #     return con, con_data
    #
    # def case_create_entity(self):
    #     # 创建实体
    #     print('-创建实体-')
    #     data = parm_entity_001
    #     res = create_entity(data[0])
    #     con = res.content.decode()
    #     con_data = json.loads(con)
    #     entity_id = con_data["data"]["entity_id"]
    #     print(entity_id)
    #     return entity_id
    #
    # def case_create_entity_value(self, entity_id, value=None):
    #     # 创建value
    #     print('-创建value-')
    #     data = parm_entity_value_001
    #     data[0]["entity_id"] = entity_id
    #     if value != None:
    #         data[0]["value"] = value
    #     res = create_entity_value(data[0])
    #     con = res.content.decode()
    #     con_data = json.loads(con)
    #     entity_value_id = con_data["data"]["entity_value_id"]
    #     print(entity_value_id)
    #     return entity_value_id
    #
    # def case_del_entity(self, entity_id):
    #     print('-del entity-')
    #     data = {
    #         "agent_id": "409",
    #         "entity_id": entity_id,
    #         "entity_type": 1
    #     }
    #     res = del_entity(data)
    #     con = res.content.decode()
    #     return con
    #
    # def get_entity_value_data(self):
    #     data_list = get_entity_value_list_data()
    #     return data_list
    #
    # @pytest.fixture(params=get_entity_value_data(None))
    # def entity_value_list_data(self, request):
    #     return request.param
    #
    # def test_get_entity_value_list(self, entity_value_list_data):
    #     """
    #     获取实体值列表
    #     """
    #     entity_id = self.case_create_entity()
    #     entity_value_id = []
    #     entity_values = []
    #     for i in range(5):
    #         value = get_str(4)
    #         entity_values.append(value)
    #         entity_value_id.append(self.case_create_entity_value(entity_id, value))
    #     data = eval(entity_value_list_data)
    #     print(data)
    #     if "entity_id" in str(data):
    #         data[0]["entity_id"] = str(entity_id)
    #     con, con_data = self.case_get_entity_value_list(data[0])
    #     print(con_data)
    #     if "code" in con:
    #         if con_data["code"] == 0:
    #             for i in range(len(entity_values)):
    #                 assert (entity_values[i] in con) and (entity_value_id[i] in con) and (
    #                         con_data["data"]['count'] == 5), con
    #     else:
    #         assert data[1] in con, con
    #     self.case_del_entity(entity_id)
    #
    # def get_data_001(self):
    #     data_list = get_parms_list_001()
    #     return data_list
    #
    # @pytest.fixture(params=get_data_001(None))
    # def get_data_list_001(self, request):
    #     return request.param




