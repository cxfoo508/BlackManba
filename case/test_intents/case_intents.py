# # coding:utf-8
# # Author : guanlu
# # CONTACT: 719667588@qq.com
# # SOFTWARE: PyCharm
# # FILE : case_intents.py.py
# # DATE : 2021/6/16 16:27
#
#
# import json
#
# import pytest
#
# from base_case import *
# from data_method import *
#
#
# class Testcase:
#
#     def auth_login(self):
#         """
#         登陆
#         """
#         print("---test login---")
#         data = {
#             "username": "laiye",
#             "password": "123123",
#             "is_keep_login": True
#         }
#         res = auth_login(data)
#         con = res.content.decode()
#         con_data = json.loads(con)
#         return con_data["data"]["jwt_token"]
#
#     def intents_list(self, agent_id):
#         """
#         获取意图列表
#         """
#         data = {
#             "agent_id": agent_id,
#             "search": {
#                 "examples": "string",
#                 "intent_name": "string"
#             },
#             "filters": {
#                 "intent_type": [
#                     0
#                 ],
#                 "trigger_type": [
#                     0
#                 ],
#                 "skill_type": [
#                     1,
#                     3
#                 ]
#             },
#             "sort": {
#                 "examples_count": "string",
#                 "update_time": "string"
#             },
#             "page_size": 20,
#             "page_num": 1
#         }
#         res = get_intents_list(data)
#         con = res.content.decode()
#         con_data = json.loads(con)
#         return con_data["data"]["intents_list"]
#
#     def intents_detail(self, agent_id, intent_id):
#         """
#         意图详情页面
#         """
#         data = {
#             "agent_id": agent_id,
#             "intent_id": intent_id
#         }
#         res = intents_detail(data)
#         con = res.content.decode()
#         con_dict = json.loads(con)
#         return con_dict["data"]
#
#     def setup_class(self):
#         print("---setup_class---")
#         os.environ["token"] = self.auth_login(None)
#         data = {
#             "agent_name": get_str(4),
#             "agent_detail": "测试",
#             "agent_logo": "string",
#             "lang": "zh-CN"
#         }
#
#         res = creat_app(data)
#         con = res.content.decode()
#         con_dict = json.loads(con)
#         assert '{"code":0,"msg":"机器人创建成功","data":{"agent_id"' in con, con
#         os.environ["agent_id"] = con_dict["data"]["agent_id"]
#         print(f"Agent_id:{os.environ.get('agent_id')}")
#
#     def test_001_create_intents(self):
#         """
#         新建意图
#         """
#         print("---test_create---")
#         agent_id = os.environ.get('agent_id')
#         data = {
#             "agent_id": agent_id,
#             "intent_name": get_str(6),
#             "examples": [
#                 {
#                     "id": 0,
#                     "name": "相似问题"
#                 }
#             ],
#             "keywords_eq": [
#                 {
#                     "id": 0,
#                     "name": "等于关键词"
#                 }
#             ],
#             "keywords_include": [
#                 {
#                     "id": 0,
#                     "name": "包含关键词"
#                 }
#             ]
#         }
#         res = create_intent(data)
#         con = res.content.decode()
#         con_dict = json.loads(con)
#         print(con_dict)
#         assert '"code":0,"msg":"创建意图成功",' in con, con
#         os.environ["intent_id"] = str(con_dict["data"]["intent_id"])
#         data_sol = Testcase.intents_list(self, agent_id)
#         print(data_sol)
#         intent_id = int(os.environ.get("intent_id"))
#         intent_id_list = list()
#         for dict_sol in data_sol:
#             intent_id_list.append(dict_sol["intent_id"])
#         assert intent_id in intent_id_list, intent_id_list
#
#     def test_002_edit_intents(self):
#         """
#         编辑意图
#         """
#         intent_id = os.environ.get("intent_id")
#         agent_id = os.environ.get("agent_id")
#         print("---test edit---")
#         data = {
#             "agent_id": agent_id,
#             "intent_id": intent_id,
#             "intent_name": get_str(2),
#             "intent_type": 1,
#             "examples": [
#                 {
#                     "id": 0,
#                     "name": "相似问题1"
#                 }
#             ],
#             "keywords_eq": [
#                 {
#                     "id": 0,
#                     "name": "关键词等于1"
#                 }
#             ],
#             "keywords_include": [
#                 {
#                     "id": 0,
#                     "name": "关键词包含1"
#                 }
#             ]
#         }
#         res = edit_intents(data)
#         con = res.content.decode()
#         con_dict = json.loads(con)
#         print(con_dict)
#         data_dict = Testcase.intents_detail(self, agent_id, intent_id)
#         if data_dict["examples"][0]["name"] == "相似问题1" and data_dict["keywords_eq"][0]["name"] == "关键词等于1" and \
#                 data_dict["keywords_include"][0]["name"] == "关键词包含1":
#             a = True
#         else:
#             a = False
#         assert a
#
#     def test_003_intents_detail(self):
#         """
#         意图详情
#         """
#         intent_id = os.environ.get("intent_id")
#         agent_id = os.environ.get("agent_id")
#         data = {
#             "agent_id": agent_id,
#             "intent_id": intent_id
#         }
#         res = intents_detail(data)
#         con = res.content.decode()
#         print(con)
#         assert '"code":0' in con, con
#
#     def test_004_intents_list(self):
#         """
#         意图列表
#         """
#         agent_id = os.environ.get("agent_id")
#         data = {
#             "agent_id": agent_id,
#             "search": {
#                 "examples": "string",
#                 "intent_name": "string"
#             },
#             "filters": {
#                 "intent_type": [
#                     0
#                 ],
#                 "trigger_type": [
#                     0
#                 ],
#                 "skill_type": [
#                     1,
#                     3
#                 ]
#             },
#             "sort": {
#                 "examples_count": "string",
#                 "update_time": "string"
#             },
#             "page_size": 20,
#             "page_num": 1
#         }
#         res = get_intents_list(data)
#         con = res.content.decode()
#         print(con)
#         assert '"code":0' in con, con
#
#     def test_005_delete_intents(self):
#         """
#         删除意图
#         """
#         intent_id = os.environ.get("intent_id")
#         agent_id = os.environ.get("agent_id")
#         data = {
#             "agent_id": agent_id,
#             "intent_id": intent_id
#         }
#         res = delete_intents(data)
#         con = res.content.decode()
#         con_dict = json.loads(con)
#         print(con_dict)
#         data_sol = Testcase.intents_list(self, agent_id)
#         print(data_sol)
#         print(os.environ.get("intent_id"))
#         intent_id_list = list()
#         for dict_sol in data_sol:
#             intent_id_list.append(dict_sol["intent_id"])
#         assert intent_id not in intent_id_list, intent_id_list
#
#     def teardown(self):
#         """
#         收尾工作
#         """
#         print("---tear down---")
#         data = {
#             "agent_id": os.environ.get("agent_id")
#         }
#         res = del_app(data)
#         con = res.content.decode()
#         print(con)
#         assert '"code":0' in con, con
#
#
# if __name__ == "__main__":
#     pytest.main("-s -v case_intents.py::Testcase")
