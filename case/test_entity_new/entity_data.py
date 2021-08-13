# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : entity_data.py
# DATE : 2021/8/5 19:18
import os
from data.data_method import *


class entity_data_class:

    def __init__(self):
        # <editor-fold desc="初始化及收尾参数列表">

        self.setup_login = [{
            "username": "laiye",
            "password": "123123",
            "is_keep_login": True
        }, [], {'token': 'res["data"]["jwt_token"]'}]
        self.setup_create_app = [{
            "agent_name": get_str(4),
            "agent_detail": "测试",
            "agent_logo": "string",
            "lang": "zh-CN"
        }, ['res["code"]==0', 'res["msg"]=="机器人创建成功"'], {'agent_id': 'res["data"]["agent_id"]'}]
        self.teardown_class = [{
            "agent_id": os.environ.get("agent_id")
        }, ['res["code"]==0'], {}]

        # </editor-fold>
        # <editor-fold desc="">

        # </editor-fold>
        # </editor-fold>
        # <editor-fold desc="新增实体参数">
        self.param_create_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="更新实体参数">
        self.param_update_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="删除实体参数">
        self.param_delete_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="新增实体值参数">
        self.param_create_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="更新实体值参数">
        self.param_update_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="删除实体值参数">
        self.param_delete_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="获取实体列表参数">
        self.param_get_entity_001 = [{"agent_id":None, 
                                    "entity_type":None,
                                    "page": None,
                                    "page_size": None,
                                    "keywords": None,
                                    "require_value":None
                                }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), 
                                    "entity_type": None,
                                          "page": None,
                                          "page_size": None,
                                          "keywords": None,
                                          "require_value": None
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": None, "entity_type": 1,
                                      
                                          "page": None,
                                          "page_size": None,
                                          "keywords": None,
                                          "require_value": None
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": None, "entity_type": None,
                                      
                                          "page": 1,
                                          "page_size": None,
                                          "keywords": None,
                                          "require_value": None
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": None, "entity_type": None,
                                      
                                          "page": None,
                                          "page_size": 10,
                                          "keywords": None,
                                          "require_value": None
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": None, "entity_type": None,
                                      
                                          "page": None,
                                          "page_size": None,
                                          "keywords": get_str(3),
                                          "require_value": None
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": None, "entity_type": None,
                                      
                                          "page": None,
                                          "page_size": None,
                                          "keywords": None,
                                          "require_value": True
                                      }, [], {}]                              
        self.param_get_entity_001 = [{"agent_id":"", "entity_type":"",
                                
                                    "page": "",
                                    "page_size": "",
                                    "keywords": "",
                                    "require_value":""
                                }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": "",
                                      
                                          "page": "",
                                          "page_size": "",
                                          "keywords": "",
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": "", "entity_type": 1,
                                      
                                          "page": "",
                                          "page_size": "",
                                          "keywords": "",
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": "", "entity_type": "",
                                      
                                          "page": 1,
                                          "page_size": "",
                                          "keywords": "",
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": "", "entity_type": "",
                                      
                                          "page": "",
                                          "page_size": 10,
                                          "keywords": "",
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": "", "entity_type": "",
                                      
                                          "page": "",
                                          "page_size": "",
                                          "keywords": get_str(3),
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": "", "entity_type": "",
                                      
                                          "page": "",
                                          "page_size": "",
                                          "keywords": "",
                                          "require_value":True
                                      }, [], {}]                              
        self.param_get_entity_001 = [{"agent_id":" ", "entity_type":" ",
                                
                                    "page": " ",
                                    "page_size": " ",
                                    "keywords": " ",
                                    "require_value":" "
                                }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": " ",
                                      
                                          "page": " ",
                                          "page_size": " ",
                                          "keywords": " ",
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": " ", "entity_type": 1,
                                      
                                          "page": " ",
                                          "page_size": " ",
                                          "keywords": " ",
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": " ", "entity_type": " ",
                                      
                                          "page": 1,
                                          "page_size": " ",
                                          "keywords": " ",
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": " ", "entity_type": " ",
                                      
                                          "page": " ",
                                          "page_size": 10,
                                          "keywords": " ",
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": " ", "entity_type": " ",
                                      
                                          "page": " ",
                                          "page_size": " ",
                                          "keywords": get_str(3),
                                    "require_value":" "}, [], {}]
        self.param_get_entity_001 = [{"agent_id": " ", "entity_type": " ",
                                      
                                          "page": " ",
                                          "page_size": " ",
                                          "keywords": " ",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 2,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 0,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":False
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 2,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":False
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 0,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":False}, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": get_str(4),
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": get_int(4),
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_type": "",
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,
                                    "require_value":True
             }, [], {}]
        self.param_get_entity_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_type": " ",
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,
                                    "require_value":True
             }, [], {}]
        self.param_get_entity_001 = [{"agent_id": get_str(4), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": get_int(10), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><", "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": "", "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": " ", "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": get_str(4),
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": get_int(10),
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": "",
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": " ",
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": get_str(4),
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": get_int(10),
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": "",
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": " ",
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": get_str(4),
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": get_int(4),
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": "",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": " ",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":get_str(4)
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":get_int(4)
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":"12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":""
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":False
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": "test",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_001 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 2,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": "test",
                                    "require_value":True
                                      }, [], {}]


        # </editor-fold>

        # <editor-fold desc="获取实体值列表参数">
        self.param_get_entityvalue_001 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": os.environ.get("agent_id"), "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": None, "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": 1,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": 10,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": get_str(3),"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":True}, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": "", "entity_id": "",
                                           
                                               "page": "",
                                               "page_size": "",
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": os.environ.get("agent_id"), "entity_id": "",
                                           
                                               "page": "",
                                               "page_size": "",
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": "", "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": "",
                                               "page_size": "",
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": "", "entity_id": "",
                                           
                                               "page": 1,
                                               "page_size": "",
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": "", "entity_id": "",
                                           
                                               "page": "",
                                               "page_size": 10,
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": "", "entity_id": "",
                                           
                                               "page": "",
                                               "page_size": "",
                                               "keywords": get_str(3),"is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": "", "entity_id": "",
                                           
                                               "page": "",
                                               "page_size": "",
                                               "keywords": "","is_tokenization":True
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": " ", "entity_id": " ",
                                           
                                               "page": " ",
                                               "page_size": " ",
                                               "keywords": " ","is_tokenization":" "
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": os.environ.get("agent_id"), "entity_id": " ",
                                           
                                               "page": " ",
                                               "page_size": " ",
                                               "keywords": " ","is_tokenization":" "
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": " ", "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": " ",
                                               "page_size": " ",
                                               "keywords": " ","is_tokenization":" "
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": " ", "entity_id": " ",
                                           
                                               "page": 1,
                                               "page_size": " ",
                                               "keywords": " ","is_tokenization":" "
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": " ", "entity_id": " ",
                                           
                                               "page": " ",
                                               "page_size": 10,
                                               "keywords": " ","is_tokenization":" "
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": " ", "entity_id": " ",
                                           
                                               "page": " ",
                                               "page_size": " ",
                                               "keywords": get_str(3),"is_tokenization":" "
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": " ", "entity_id": " ",
                                           
                                               "page": " ",
                                               "page_size": " ",
                                               "keywords": " ",
                                                "is_tokenization":True}, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None
                 ,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": os.environ.get("agent_id"), "entity_id": get_str(4),
                                           
                                               "page": 1,
                                               "page_size": 20,
                                               "keywords": None,"is_tokenization":False
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": os.environ.get("agent_id"), "entity_id": get_int(4),
                                           
                                               "page": 1,
                                               "page_size": 20,
                                               "keywords": None,"is_tokenization":False
                                           }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": "",
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": " ",
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": get_str(4), "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": 1,
                                               "page_size": 20,
                                               "keywords": None,"is_tokenization":False
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": get_int(10), "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": 1,
                                               "page_size": 20,
                                               "keywords": None,"is_tokenization":False
                                           }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><", "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": "", "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": 1,
                                               "page_size": 20,
                                               "keywords": None,"is_tokenization":False
                                           }, [], {}]
        self.param_get_entityvalue_001 = [{"agent_id": " ", "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": 1,
                                               "page_size": 20,
                                               "keywords": None,"is_tokenization":False
                                           }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": get_str(4),
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": get_int(10),
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": "",
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": " ",
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": get_str(4),
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": get_int(10),
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": "",
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": " ",
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": get_str(4),"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": get_int(4),"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><","is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": "","is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": " ","is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":False
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":True
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":get_str(4)
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":get_int(4)
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":"12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":""
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,"is_tokenization":" "
             }, [], {}]

        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": "test",
                 "is_tokenization":True
             }, [], {}]
        self.param_get_entityvalue_001 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": "test",
                 "is_tokenization":False
             }, [], {}]
        # </editor-fold>

        # <editor-fold desc="导入实体参数">
        self.param_import_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="导出实体参数">
        self.param_export_entity_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="导入实体值参数">
        self.param_port_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="导出实体值参数">
        self.param_export_entityvalue_001 = [{}, [], {}]
        # </editor-fold>

        # <editor-fold desc="正则实体待输入文本测试">
        self.param_test_entityvalue_001 = [{}, [], {}]
        # </editor-fold>
