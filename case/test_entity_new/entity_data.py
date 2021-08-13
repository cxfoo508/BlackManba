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
        self.param_get_entity_002 = [{"agent_id": os.environ.get("agent_id"), 
                                    "entity_type": None,
                                        "page": None,
                                        "page_size": None,
                                        "keywords": None,
                                        "require_value": None
                                    }, [], {}]
        self.param_get_entity_003 = [{"agent_id": None, "entity_type": 1,
                                        "page": None,
                                        "page_size": None,
                                        "keywords": None,
                                        "require_value": None
                                    }, [], {}]
        self.param_get_entity_004 = [{"agent_id": None, "entity_type": None,
                                      
                                        "page": 1,
                                          "page_size": None,
                                          "keywords": None,
                                          "require_value": None
                                      }, [], {}]
        self.param_get_entity_005 = [{"agent_id": None, "entity_type": None,
                                      
                                          "page": None,
                                          "page_size": 10,
                                          "keywords": None,
                                          "require_value": None
                                      }, [], {}]
        self.param_get_entity_006 = [{"agent_id": None, "entity_type": None,
                                      
                                          "page": None,
                                          "page_size": None,
                                          "keywords": get_str(3),
                                          "require_value": None
                                      }, [], {}]
        self.param_get_entity_007 = [{"agent_id": None, "entity_type": None,
                                      
                                          "page": None,
                                          "page_size": None,
                                          "keywords": None,
                                          "require_value": True
                                      }, [], {}]                              
        self.param_get_entity_008 = [{"agent_id":"", "entity_type":"",
                                
                                    "page": "",
                                    "page_size": "",
                                    "keywords": "",
                                    "require_value":""
                                }, [], {}]
        self.param_get_entity_009 = [{"agent_id": os.environ.get("agent_id"), "entity_type": "",
                                      
                                          "page": "",
                                          "page_size": "",
                                          "keywords": "",
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_010 = [{"agent_id": "", "entity_type": 1,
                                      
                                          "page": "",
                                          "page_size": "",
                                          "keywords": "",
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_011 = [{"agent_id": "", "entity_type": "",
                                      
                                          "page": 1,
                                          "page_size": "",
                                          "keywords": "",
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_012 = [{"agent_id": "", "entity_type": "",
                                      
                                          "page": "",
                                          "page_size": 10,
                                          "keywords": "",
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_013 = [{"agent_id": "", "entity_type": "",
                                      
                                          "page": "",
                                          "page_size": "",
                                          "keywords": get_str(3),
                                          "require_value":""
                                      }, [], {}]
        self.param_get_entity_014 = [{"agent_id": "", "entity_type": "",
                                      
                                          "page": "",
                                          "page_size": "",
                                          "keywords": "",
                                          "require_value":True
                                      }, [], {}]                              
        self.param_get_entity_015 = [{"agent_id":" ", "entity_type":" ",
                                
                                    "page": " ",
                                    "page_size": " ",
                                    "keywords": " ",
                                    "require_value":" "
                                }, [], {}]
        self.param_get_entity_016 = [{"agent_id": os.environ.get("agent_id"), "entity_type": " ",
                                      
                                          "page": " ",
                                          "page_size": " ",
                                          "keywords": " ",
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_017 = [{"agent_id": " ", "entity_type": 1,
                                      
                                          "page": " ",
                                          "page_size": " ",
                                          "keywords": " ",
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_018 = [{"agent_id": " ", "entity_type": " ",
                                      
                                          "page": 1,
                                          "page_size": " ",
                                          "keywords": " ",
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_019 = [{"agent_id": " ", "entity_type": " ",
                                      
                                          "page": " ",
                                          "page_size": 10,
                                          "keywords": " ",
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_020 = [{"agent_id": " ", "entity_type": " ",
                                      
                                          "page": " ",
                                          "page_size": " ",
                                          "keywords": get_str(3),
                                    "require_value":" "}, [], {}]
        self.param_get_entity_021 = [{"agent_id": " ", "entity_type": " ",
                                      
                                          "page": " ",
                                          "page_size": " ",
                                          "keywords": " ",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_022 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_023 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 2,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_024 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 0,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_025 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":False
                                      }, [], {}]
        self.param_get_entity_026 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 2,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":False
                                      }, [], {}]
        self.param_get_entity_027 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 0,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":False}, [], {}]
        self.param_get_entity_028 = [{"agent_id": os.environ.get("agent_id"), "entity_type": get_str(4),
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_029 = [{"agent_id": os.environ.get("agent_id"), "entity_type": get_int(4),
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_030 = [{"agent_id": os.environ.get("agent_id"), "entity_type": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_031 = [
            {"agent_id": os.environ.get("agent_id"), "entity_type": "",
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,
                                    "require_value":True
             }, [], {}]
        self.param_get_entity_032 = [
            {"agent_id": os.environ.get("agent_id"), "entity_type": " ",
             
                 "page": 1,
                 "page_size": 20,
                 "keywords": None,
                                    "require_value":True
             }, [], {}]
        self.param_get_entity_033 = [{"agent_id": get_str(4), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_034 = [{"agent_id": get_int(10), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_035 = [{"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><", "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_036 = [{"agent_id": "", "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_037 = [{"agent_id": " ", "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_038 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": get_str(4),
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_039 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": get_int(10),
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_040 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_041 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": "",
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_042 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": " ",
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_043 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": get_str(4),
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_044 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": get_int(10),
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_045 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_045 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": "",
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_047 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": " ",
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_048 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": get_str(4),
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_049 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": get_int(4),
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_050 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_051 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": "",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_052 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": " ",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_053 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":get_str(4)
                                      }, [], {}]
        self.param_get_entity_054 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":get_int(4)
                                      }, [], {}]
        self.param_get_entity_055 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":"12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                      }, [], {}]
        self.param_get_entity_056 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":""
                                      }, [], {}]
        self.param_get_entity_057 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":" "
                                      }, [], {}]
        self.param_get_entity_058 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_059 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": None,
                                    "require_value":False
                                      }, [], {}]
        self.param_get_entity_060 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 1,
                                      
                                          "page": 1,
                                          "page_size": 20,
                                          "keywords": "test",
                                    "require_value":True
                                      }, [], {}]
        self.param_get_entity_061 = [{"agent_id": os.environ.get("agent_id"), "entity_type": 2,
                                      
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
        self.param_get_entityvalue_002 = [{"agent_id": os.environ.get("agent_id"), "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_003 = [{"agent_id": None, "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_004 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": 1,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_005 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": 10,
                                               "keywords": None,"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_006 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": get_str(3),"is_tokenization":None
                                           }, [], {}]
        self.param_get_entityvalue_007 = [{"agent_id": None, "entity_id": None,
                                           
                                               "page": None,
                                               "page_size": None,
                                               "keywords": None,"is_tokenization":True}, [], {}]
        self.param_get_entityvalue_008 = [{"agent_id": "", "entity_id": "",
                                           
                                               "page": "",
                                               "page_size": "",
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_009 = [{"agent_id": os.environ.get("agent_id"), "entity_id": "",
                                           
                                               "page": "",
                                               "page_size": "",
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_010 = [{"agent_id": "", "entity_id": os.environ.get("entity_id"),
                                           
                                               "page": "",
                                               "page_size": "",
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_011 = [{"agent_id": "", "entity_id": "",
                                           
                                               "page": 1,
                                               "page_size": "",
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_012 = [{"agent_id": "", "entity_id": "",
                                           
                                               "page": "",
                                               "page_size": 10,
                                               "keywords": "","is_tokenization":""
                                           }, [], {}]
        self.param_get_entityvalue_013 = [{"agent_id": "", "entity_id": "",
                                            
                                                "page": "",
                                                "page_size": "",
                                                "keywords": get_str(3),"is_tokenization":""
                                            }, [], {}]
        self.param_get_entityvalue_014 = [{"agent_id": "", "entity_id": "",
                                            
                                                "page": "",
                                                "page_size": "",
                                                "keywords": "","is_tokenization":True
                                            }, [], {}]
        self.param_get_entityvalue_015 = [{"agent_id": " ", "entity_id": " ",
                                            
                                                "page": " ",
                                                "page_size": " ",
                                                "keywords": " ","is_tokenization":" "
                                            }, [], {}]
        self.param_get_entityvalue_016 = [{"agent_id": os.environ.get("agent_id"), "entity_id": " ",
                                            
                                                "page": " ",
                                                "page_size": " ",
                                                "keywords": " ","is_tokenization":" "
                                            }, [], {}]
        self.param_get_entityvalue_017 = [{"agent_id": " ", "entity_id": os.environ.get("entity_id"),
                                            
                                                "page": " ",
                                                "page_size": " ",
                                                "keywords": " ","is_tokenization":" "
                                            }, [], {}]
        self.param_get_entityvalue_018 = [{"agent_id": " ", "entity_id": " ",
                                            
                                                "page": 1,
                                                "page_size": " ",
                                                "keywords": " ","is_tokenization":" "
                                            }, [], {}]
        self.param_get_entityvalue_019 = [{"agent_id": " ", "entity_id": " ",
                                                
                                                "page": " ",
                                                "page_size": 10,
                                                "keywords": " ","is_tokenization":" "
                                            }, [], {}]
        self.param_get_entityvalue_020 = [{"agent_id": " ", "entity_id": " ",
                                            
                                                "page": " ",
                                                "page_size": " ",
                                                "keywords": get_str(3),"is_tokenization":" "
                                            }, [], {}]
        self.param_get_entityvalue_021 = [{"agent_id": " ", "entity_id": " ",
                                            
                                                "page": " ",
                                                "page_size": " ",
                                                "keywords": " ",
                                                "is_tokenization":True}, [], {}]
        self.param_get_entityvalue_022 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
                
                    "page": 1,
                    "page_size": 20,
                    "keywords": None
                    ,"is_tokenization":False
                }, [], {}]
        self.param_get_entityvalue_023 = [{"agent_id": os.environ.get("agent_id"), "entity_id": get_str(4),
                                            
                                                "page": 1,
                                                "page_size": 20,
                                                "keywords": None,"is_tokenization":False
                                            }, [], {}]
        self.param_get_entityvalue_024 = [{"agent_id": os.environ.get("agent_id"), "entity_id": get_int(4),
                                            
                                                "page": 1,
                                                "page_size": 20,
                                                "keywords": None,"is_tokenization":False
                                            }, [], {}]
        self.param_get_entityvalue_025 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                
                    "page": 1,
                    "page_size": 20,
                    "keywords": None,"is_tokenization":False
                }, [], {}]
        self.param_get_entityvalue_026 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": "",
                
                    "page": 1,
                    "page_size": 20,
                    "keywords": None,"is_tokenization":False
                }, [], {}]
        self.param_get_entityvalue_027 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": " ",
            
                "page": 1,
                "page_size": 20,
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_028 = [{"agent_id": get_str(4), "entity_id": os.environ.get("entity_id"),
                                        
                                            "page": 1,
                                            "page_size": 20,
                                            "keywords": None,"is_tokenization":False
                                        }, [], {}]
        self.param_get_entityvalue_029 = [{"agent_id": get_int(10), "entity_id": os.environ.get("entity_id"),
                                        
                                            "page": 1,
                                            "page_size": 20,
                                            "keywords": None,"is_tokenization":False
                                        }, [], {}]
        self.param_get_entityvalue_030 = [
            {"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><", "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_031 = [{"agent_id": "", "entity_id": os.environ.get("entity_id"),
                                        
                                            "page": 1,
                                            "page_size": 20,
                                            "keywords": None,"is_tokenization":False
                                        }, [], {}]
        self.param_get_entityvalue_032 = [{"agent_id": " ", "entity_id": os.environ.get("entity_id"),
                                        
                                            "page": 1,
                                            "page_size": 20,
                                            "keywords": None,"is_tokenization":False
                                        }, [], {}]
        self.param_get_entityvalue_033 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": get_str(4),
                "page_size": 20,
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_034 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": get_int(10),
                "page_size": 20,
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_035 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                "page_size": 20,
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_036 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": "",
                "page_size": 20,
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_037 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": " ",
                "page_size": 20,
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_038 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": get_str(4),
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_039 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": get_int(10),
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_040 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_041 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": "",
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_042 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": " ",
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_043 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": get_str(4),"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_044 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": get_int(4),"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_045 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><","is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_046 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": "","is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_047 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": " ","is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_048 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": None,"is_tokenization":False
            }, [], {}]
        self.param_get_entityvalue_049 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": None,"is_tokenization":True
            }, [], {}]
        self.param_get_entityvalue_050 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": None,"is_tokenization":get_str(4)
            }, [], {}]
        self.param_get_entityvalue_051 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": None,"is_tokenization":get_int(4)
            }, [], {}]
        self.param_get_entityvalue_052 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
            "keywords": None,"is_tokenization":"12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
            }, [], {}]
        self.param_get_entityvalue_053 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
            "page": 1,
                "page_size": 20,
                "keywords": None,"is_tokenization":""
            }, [], {}]
        self.param_get_entityvalue_054 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": None,"is_tokenization":" "
            }, [], {}]

        self.param_get_entityvalue_055 = [
            {"agent_id": os.environ.get("agent_id"), "entity_id": os.environ.get("entity_id"),
            
                "page": 1,
                "page_size": 20,
                "keywords": "test",
                "is_tokenization":True
            }, [], {}]
        self.param_get_entityvalue_056 = [
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
