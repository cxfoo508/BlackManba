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
        # <editor-fold desc="新增实体参数">
        self.param_create_entity_001 = [{"agentId": None,
                                         "data": {
                                        "mutateOperations": [
                                            {
                                                "entityOperation": {
                                                    "create": {
                                                        "id": None,
                                                        "displayName": None,
                                                        "type":None
                                                        }
                                                    }
                                                }
                                            ]
                                         }
                                            }, [], {}]
        self.param_create_entity_002 = [{"agentId": os.environ.get("agent_id"),
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": None,
                                                             "displayName": None,
                                                             "type": None
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_003 = [{"agentId": None,
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": 1,
                                                             "displayName": None,
                                                             "type": None
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_004 = [{"agentId": None,
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": None,
                                                             "displayName": get_str(4),
                                                             "type": None
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_005 = [{"agentId": None,
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": None,
                                                             "displayName": None,
                                                             "type": 1
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_006 = [{"agentId": "",
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": "",
                                                             "displayName": "",
                                                             "type": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]
        self.param_create_entity_007 = [{"agentId": os.environ.get("agent_id"),
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": "",
                                                             "displayName": "",
                                                             "type": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_008 = [{"agentId": "",
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": 1,
                                                             "displayName": "",
                                                             "type": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_009 = [{"agentId": "",
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": "",
                                                             "displayName": get_str(4),
                                                             "type": ""
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_010 = [{"agentId": "",
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": "",
                                                             "displayName": "",
                                                             "type": 1
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_011 = [{"agentId": " ",
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": " ",
                                                             "displayName": " ",
                                                             "type": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]
        self.param_create_entity_012 = [{"agentId": os.environ.get("agent_id"),
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": " ",
                                                             "displayName": " ",
                                                             "type": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_013 = [{"agentId": " ",
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": 1,
                                                             "displayName": " ",
                                                             "type": " "
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]

        self.param_create_entity_014 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": " ",
                                                           "displayName": get_str(4),
                                                           "type": " "
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_create_entity_015 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": " ",
                                                           "displayName": " ",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_create_entity_016 = [{"agentId": " ",
                                      "data": {
                                          "mutateOperations": [
                                              {
                                                  "entityOperation": {
                                                      "create": {
                                                          "id": " ",
                                                          "displayName": " ",
                                                          "type": 1
                                                      }
                                                  }
                                              }
                                          ]
                                      }
                                      }, [], {}]
        self.param_create_entity_017 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_018 = [{"agentId": get_str(4),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_019 = [{"agentId": get_int(10),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_020 = [{"agentId": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_021 = [{"agentId": "",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_022 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_023 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": get_str(4),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_024 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": get_int(4),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_025 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_026 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": "",
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_027 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": " ",
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_028 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_int(128),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_029 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_int(129),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_030 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_031 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": "",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_032 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": " ",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_033 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": get_str(4)
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_034 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": get_int(4)
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_035 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_036 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": ""
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_037 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": " "
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_038 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": 0
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_039 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_040 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": 2
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_041 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": 4
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_042 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "create": {
                                                           "id": -1,
                                                           "displayName": get_str(128),
                                                           "type": 4
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_create_entity_043 = [{"agentId": os.environ.get("agent_id"),
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": -1,
                                                             "displayName": get_str(128),
                                                             "type": 4
                                                         }
                                                     }
                                                 },{
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": -1,
                                                             "displayName": get_str(128),
                                                             "type": 1
                                                         }
                                                     }
                                                 },{
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": -1,
                                                             "displayName": get_str(128),
                                                             "type": 2
                                                         }
                                                     }
                                                 },{
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": -1,
                                                             "displayName": get_str(128),
                                                             "type": 3
                                                         }
                                                     }
                                                 },{
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": -1,
                                                             "displayName": get_str(128),
                                                             "type": 4
                                                         }
                                                     }
                                                 },{
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": -1,
                                                             "displayName": get_str(128),
                                                             "type": 1
                                                         }
                                                     }
                                                 },{
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": 100,
                                                             "displayName": get_str(128),
                                                             "type": 2
                                                         }
                                                     }
                                                 },{
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": -1,
                                                             "displayName": get_str(129),
                                                             "type": 4
                                                         }
                                                     }
                                                 },{
                                                     "entityOperation": {
                                                         "create": {
                                                             "id": -1,
                                                             "displayName": get_str(128),
                                                             "type": 4
                                                         }
                                                     }
                                                 }
                                             ]
                                         }
                                         }, [], {}]


        # </editor-fold>

        # <editor-fold desc="更新实体参数">
        self.param_update_entity_001 = [{"agentId": None,
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": None,
                                                           "displayName": None,
                                                           "type": None
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_002 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": None,
                                                           "displayName": None,
                                                           "type": None
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_003 = [{"agentId": None,
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": None,
                                                           "type": None
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_004 = [{"agentId": None,
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": None,
                                                           "displayName": get_str(4),
                                                           "type": None
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_005 = [{"agentId": None,
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": None,
                                                           "displayName": None,
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_006 = [{"agentId": "",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": "",
                                                           "displayName": "",
                                                           "type": ""
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_007 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": "",
                                                           "displayName": "",
                                                           "type": ""
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_008 = [{"agentId": "",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": "",
                                                           "type": ""
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_009 = [{"agentId": "",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": "",
                                                           "displayName": get_str(4),
                                                           "type": ""
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_010 = [{"agentId": "",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": "",
                                                           "displayName": "",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_011 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": " ",
                                                           "displayName": " ",
                                                           "type": " "
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_012 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": " ",
                                                           "displayName": " ",
                                                           "type": " "
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_013 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": " ",
                                                           "type": " "
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_014 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": " ",
                                                           "displayName": get_str(4),
                                                           "type": " "
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_015 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": " ",
                                                           "displayName": " ",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]

        self.param_update_entity_016 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": " ",
                                                           "displayName": " ",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_017 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_018 = [{"agentId": get_str(4),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_019 = [{"agentId": get_int(10),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_020 = [{"agentId": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_021 = [{"agentId": "",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_022 = [{"agentId": " ",
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_023 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": get_str(4),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_024 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": get_int(4),
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_025 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_026 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": "",
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_027 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": " ",
                                                           "displayName": get_str(4),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_028 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_int(128),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_029 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_int(129),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_030 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_031 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": "",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_032 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": " ",
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_033 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": get_str(4)
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_034 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": get_int(4)
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_035 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_036 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": ""
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_037 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": " "
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_038 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": 0
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_039 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": 1
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_040 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": 2
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_041 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": 4
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_042 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {
                                           "mutateOperations": [
                                               {
                                                   "entityOperation": {
                                                       "update": {
                                                           "id": os.environ.get("entity_id"),
                                                           "displayName": get_str(128),
                                                           "type": 4
                                                       }
                                                   }
                                               }
                                           ]
                                       }
                                       }, [], {}]
        self.param_update_entity_043 = [{"agentId": os.environ.get("agent_id"),
                                         "data": {
                                             "mutateOperations": [
                                                 {
                                                     "entityOperation": {
                                                         "update": {
                                                             "id": os.environ.get("entity_id"),
                                                             "displayName": get_str(128),
                                                             "type": 4
                                                         }
                                                     }
                                                 }, {
                                                     "entityOperation": {
                                                         "update": {
                                                             "id": os.environ.get("entity_id"),
                                                             "displayName": get_str(128),
                                                             "type": 1
                                                         }
                                                     }
                                                 }, {
                                                     "entityOperation": {
                                                         "update": {
                                                             "id": os.environ.get("entity_id"),
                                                             "displayName": get_str(128),
                                                             "type": 2
                                                         }
                                                     }
                                                 }, {
                                                     "entityOperation": {
                                                         "update": {
                                                             "id": -1,
                                                             "displayName": get_str(128),
                                                             "type": 3
                                                         }
                                                     }
                                                 }, {
                                                     "entityOperation": {
                                                         "update": {
                                                             "id": os.environ.get("entity_id"),
                                                             "displayName": get_str(128),
                                                             "type": 4
                                                         }
                                                     }
                                                 }, {
                                                     "entityOperation": {
                                                         "update": {
                                                             "id": os.environ.get("entity_id"),
                                                             "displayName": get_str(128),
                                                             "type": 1
                                                         }
                                                     }
                                                 }, {
                                                     "entityOperation": {
                                                         "update": {
                                                             "id": os.environ.get("entity_id"),
                                                         "displayName": get_str(128),
                                                         "type": 2
                                                     }
                                                 }
                                         }, {
                                             "entityOperation": {
                                                 "update": {
                                                     "id": os.environ.get("entity_id"),
                                                     "displayName": get_str(129),
                                                     "type": 4
                                                 }
                                             }
                                         }, {
                                            "entityOperation": {
                                                "update": {
                                                    "id": os.environ.get("entity_id"),
                                                    "displayName": get_str(128),
                                                    "type": 4
                                                }
                                            }
                                        }
                                        ]
        }
        }, [], {}]

        # </editor-fold>

        # <editor-fold desc="删除实体参数">
        self.param_delete_entity_001 = [{"agentId": None,
                                       "data": {
                                           "mutateOperations": [
                                               {"entityOperation": {
                                               "delete": None
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_002 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": None
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_003 = [{"agentId": None,
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": get_int(10)
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_004 = [{"agentId": "",
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": ""
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_005 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": ""
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_006 = [{"agentId": "",
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": get_int(10)
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_007 = [{"agentId": " ",
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": " "
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_008 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": " "
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_009 = [{"agentId": " ",
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": get_int(10)
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_010 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": os.environ.get("entity_id")
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_011 = [{"agentId": get_int(10),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": os.environ.get("entity_id")
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_012 = [{"agentId": get_str(4),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": os.environ.get("entity_id")
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_013 = [{"agentId": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": os.environ.get("entity_id")
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_014 = [{"agentId": "",
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": os.environ.get("entity_id")
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_015 = [{"agentId": " ",
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": os.environ.get("entity_id")
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_016 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": get_str(4)
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_017 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": get_int(10)
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_018 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_019 = [{"agentId": os.environ.get("agent_id"),
                                       "data": {"mutateOperations": [
                                               {
                                           "entityOperation": {
                                               "delete": ""
                                           }
                                       }]
                                       }}, [], {}]
        self.param_delete_entity_020 = [{"agentId": os.environ.get("agent_id"),
                                         "data": {"mutateOperations": [
                                                 {
                                             "entityOperation": {
                                                 "delete": " "
                                             }
                                         }]
                                         }}, [], {}]



        # </editor-fold>

        # <editor-fold desc="新增实体值参数">
        self.param_create_entityvalue_001 = [{"agentId": None,
                                            "data":{"mutateOperations": [
                                               {
                                          "entityValueOperation": {
                                              "create": {
                                                  "id": None,
                                                  "entityId": None,
                                                  "value":None,
                                                  "regex": None,
                                                  "synonyms":[],
                                                  "enableTokenization":None
                                              }
                                          }
                                               }]}}, [], {}]
        self.param_create_entityvalue_002 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": None,
                                                        "entityId": None,
                                                        "value": None,
                                                        "regex": None,
                                                        "synonyms": [],
                                                        "enableTokenization": None
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_003 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": get_int(10),
                                                        "entityId": None,
                                                        "value": None,
                                                        "regex": None,
                                                        "synonyms": [],
                                                        "enableTokenization": None
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_004 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": None,
                                                        "entityId": get_int(110),
                                                        "value": None,
                                                        "regex": None,
                                                        "synonyms": [],
                                                        "enableTokenization": None
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_005 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": None,
                                                        "entityId": None,
                                                        "value": get_str(4),
                                                        "regex": None,
                                                        "synonyms": [],
                                                        "enableTokenization": None
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_006 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": None,
                                                        "entityId": None,
                                                        "value": None,
                                                        "regex": get_str(4),
                                                        "synonyms": [],
                                                        "enableTokenization": None
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_007 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": None,
                                                        "entityId": None,
                                                        "value": None,
                                                        "regex": None,
                                                        "synonyms": [],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_008 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": "",
                                                        "entityId": "",
                                                        "value": "",
                                                        "regex": "",
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_009 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": "",
                                                        "entityId": "",
                                                        "value": "",
                                                        "regex": "",
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_010 = [{"agentId": "",
                                            "data": {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": get_int(10),
                                                        "entityId": "",
                                                        "value": "",
                                                        "regex": "",
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }}, [], {}]
        self.param_create_entityvalue_011 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": "",
                                                        "entityId": get_int(110),
                                                        "value": "",
                                                        "regex": "",
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_012 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": "",
                                                        "entityId": "",
                                                        "value": get_str(4),
                                                        "regex": "",
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_013 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": "",
                                                        "entityId": "",
                                                        "value": "",
                                                        "regex": get_str(4),
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_014 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": "",
                                                        "entityId": "",
                                                        "value": "",
                                                        "regex": "",
                                                        "synonyms": [],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_015 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": " ",
                                                        "entityId": " ",
                                                        "value": " ",
                                                        "regex": " ",
                                                        "synonyms": [],
                                                        "enableTokenization": " "
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_016 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": " ",
                                                        "entityId": " ",
                                                        "value": " ",
                                                        "regex": " ",
                                                        "synonyms": [],
                                                        "enableTokenization": " "
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_017 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": get_int(10),
                                                        "entityId": " ",
                                                        "value": " ",
                                                        "regex": " ",
                                                        "synonyms": [],
                                                        "enableTokenization": " "
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_018 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": " ",
                                                        "entityId": get_int(110),
                                                        "value": " ",
                                                        "regex": " ",
                                                        "synonyms": [],
                                                        "enableTokenization": " "
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_019 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": " ",
                                                        "entityId": " ",
                                                        "value": get_str(4),
                                                        "regex": " ",
                                                        "synonyms": [],
                                                        "enableTokenization": " "
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_020 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": " ",
                                                        "entityId": " ",
                                                        "value": " ",
                                                        "regex": get_str(4),
                                                        "synonyms": [],
                                                        "enableTokenization": " "
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_021 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": " ",
                                                        "entityId": " ",
                                                        "value": " ",
                                                        "regex": " ",
                                                        "synonyms": [],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}}, [], {}]
        self.param_create_entityvalue_022 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                          "entityValueOperation": {
                                              "create": {
                                                  "id": -1,
                                                  "entityId": os.environ.get("entity_id"),
                                                  "value":get_str(4),
                                                  "regex": get_str(4),
                                                  "synonyms":[get_str(5), get_str(5), get_str(5), get_str(5), get_str(5)],
                                                  "enableTokenization":True
                                                              }
                                                          }
                                                     }]
                                                 }}
                                            , [], {}]
        self.param_create_entityvalue_023 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_024 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_025 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_026 = [{"agentId": get_str(4),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_027 = [{"agentId": get_int(10),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_028 = [{"agentId": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_029 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_030 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_031 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": get_str(4),
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_032 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": get_int(4),
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_033 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_034 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": "",
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_035 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": " ",
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_036 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": get_str(4),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_037 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": get_int(4),
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_038 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_039 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": "",
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_040 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": " ",
                                                        "value": get_str(4),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_041 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(128),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_042 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "create": {
                                                            "id": -1,
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(128),
                                                            "regex": "",
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_043 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("enum_entity_id"),
                                                        "value": get_str(129),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_044 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(128),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_045 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(129),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_046 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_int(128),
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                        }
            , [], {}]
        self.param_create_entityvalue_047 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_048 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": "",
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_049 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": " ",
                                                        "regex": get_str(4),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_050 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": get_str(512),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_051 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": get_str(513),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_052 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": get_int(255),
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_053 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_054 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "",
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_055 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": " ",
                                                        "synonyms": [get_str(5), get_str(5), get_str(5), get_str(5)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_056 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [get_str(128), get_str(129), get_int(128), get_int(129)],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_057 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [""],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_058 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [" "],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_059 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": ["12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_060 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": ["12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"],
                                                        "enableTokenization": True
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_061 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": ["12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"],
                                                        "enableTokenization": False
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_062 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [],
                                                        "enableTokenization": get_str(4)
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_063 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [],
                                                        "enableTokenization": get_int(4)
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_064 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [],
                                                        "enableTokenization": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_065 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_066 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [],
                                                        "enableTokenization": " "
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_067 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                               {
                                                "entityValueOperation": {
                                                    "create": {
                                                        "id": -1,
                                                        "entityId": os.environ.get("entity_id"),
                                                        "value": get_str(12),
                                                        "regex": "^[0-9]*$",
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }]}
                                            }
            , [], {}]
        self.param_create_entityvalue_068 = [{"agentId": os.environ.get("agent_id"),
                                              "data": {"mutateOperations": [
                                                  {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("enum_entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": True
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "create": {
                                                              "id": -1,
                                                              "entityId": os.environ.get("enum_entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "",
                                                              "synonyms": [get_str(1), get_str(1), get_str(1), get_str(1)],
                                                              "enableTokenization": True
                                                          }
                                                      }
                                                  }]}
                                              }
            , [], {}]


        # </editor-fold>

        # <editor-fold desc="更新实体值参数">
        self.param_update_entityvalue_001 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": None,
                                                            "entityId": None,
                                                            "value": None,
                                                            "regex": None,
                                                            "synonyms": [],
                                                            "enableTokenization": None
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_002 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": None,
                                                            "entityId": None,
                                                            "value": None,
                                                            "regex": None,
                                                            "synonyms": [],
                                                            "enableTokenization": None
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_003 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": get_int(10),
                                                            "entityId": None,
                                                            "value": None,
                                                            "regex": None,
                                                            "synonyms": [],
                                                            "enableTokenization": None
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_004 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": None,
                                                            "entityId": get_int(110),
                                                            "value": None,
                                                            "regex": None,
                                                            "synonyms": [],
                                                            "enableTokenization": None
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_005 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": None,
                                                            "entityId": None,
                                                            "value": get_str(4),
                                                            "regex": None,
                                                            "synonyms": [],
                                                            "enableTokenization": None
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_006 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": None,
                                                            "entityId": None,
                                                            "value": None,
                                                            "regex": get_str(4),
                                                            "synonyms": [],
                                                            "enableTokenization": None
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_007 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": None,
                                                            "entityId": None,
                                                            "value": None,
                                                            "regex": None,
                                                            "synonyms": [],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_008 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": "",
                                                            "entityId": "",
                                                            "value": "",
                                                            "regex": "",
                                                            "synonyms": [],
                                                            "enableTokenization": ""
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_009 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": "",
                                                            "entityId": "",
                                                            "value": "",
                                                            "regex": "",
                                                            "synonyms": [],
                                                            "enableTokenization": ""
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_010 = [{"agentId": "",
                                            "data": {
                                                "entityValueOperation": {
                                                    "update": {
                                                        "id": get_int(10),
                                                        "entityId": "",
                                                        "value": "",
                                                        "regex": "",
                                                        "synonyms": [],
                                                        "enableTokenization": ""
                                                    }
                                                }
                                            }}, [], {}]
        self.param_update_entityvalue_011 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": "",
                                                            "entityId": get_int(110),
                                                            "value": "",
                                                            "regex": "",
                                                            "synonyms": [],
                                                            "enableTokenization": ""
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_012 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": "",
                                                            "entityId": "",
                                                            "value": get_str(4),
                                                            "regex": "",
                                                            "synonyms": [],
                                                            "enableTokenization": ""
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_013 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": "",
                                                            "entityId": "",
                                                            "value": "",
                                                            "regex": get_str(4),
                                                            "synonyms": [],
                                                            "enableTokenization": ""
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_014 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": "",
                                                            "entityId": "",
                                                            "value": "",
                                                            "regex": "",
                                                            "synonyms": [],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_015 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": " ",
                                                            "entityId": " ",
                                                            "value": " ",
                                                            "regex": " ",
                                                            "synonyms": [],
                                                            "enableTokenization": " "
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_016 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": " ",
                                                            "entityId": " ",
                                                            "value": " ",
                                                            "regex": " ",
                                                            "synonyms": [],
                                                            "enableTokenization": " "
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_017 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": get_int(10),
                                                            "entityId": " ",
                                                            "value": " ",
                                                            "regex": " ",
                                                            "synonyms": [],
                                                            "enableTokenization": " "
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_018 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": " ",
                                                            "entityId": get_int(110),
                                                            "value": " ",
                                                            "regex": " ",
                                                            "synonyms": [],
                                                            "enableTokenization": " "
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_019 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": " ",
                                                            "entityId": " ",
                                                            "value": get_str(4),
                                                            "regex": " ",
                                                            "synonyms": [],
                                                            "enableTokenization": " "
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_020 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": " ",
                                                            "entityId": " ",
                                                            "value": " ",
                                                            "regex": get_str(4),
                                                            "synonyms": [],
                                                            "enableTokenization": " "
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_021 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": " ",
                                                            "entityId": " ",
                                                            "value": " ",
                                                            "regex": " ",
                                                            "synonyms": [],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}}, [], {}]
        self.param_update_entityvalue_022 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5), get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]
                                            }}
            , [], {}]
        self.param_update_entityvalue_023 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_024 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_025 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_026 = [{"agentId": get_str(4),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_027 = [{"agentId": get_int(10),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_028 = [{"agentId": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_029 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_030 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_031 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": get_str(4),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_032 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": get_int(4),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_033 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_034 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": "",
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_035 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": " ",
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_036 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": get_str(4),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_037 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": get_int(4),
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_038 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_039 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": "",
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_040 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": " ",
                                                            "value": get_str(4),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_041 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(128),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_042 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(128),
                                                            "regex": "",
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_043 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("enum_entity_id"),
                                                            "value": get_str(129),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_044 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(128),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_045 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(129),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_046 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_int(128),
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_047 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_048 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": "",
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_049 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": " ",
                                                            "regex": get_str(4),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_050 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": get_str(512),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_051 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": get_str(513),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_052 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": get_int(255),
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_053 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_054 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "",
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_055 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": " ",
                                                            "synonyms": [get_str(5), get_str(5), get_str(5),
                                                                         get_str(5)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_056 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [get_str(128), get_str(129), get_int(128),
                                                                         get_int(129)],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_057 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [""],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_058 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [" "],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_059 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": ["12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_060 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": ["12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"],
                                                            "enableTokenization": True
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_061 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": ["12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"],
                                                            "enableTokenization": False
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_062 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [],
                                                            "enableTokenization": get_str(4)
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_063 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [],
                                                            "enableTokenization": get_int(4)
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_064 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [],
                                                            "enableTokenization": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_065 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [],
                                                            "enableTokenization": ""
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_066 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [],
                                                            "enableTokenization": " "
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_067 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "update": {
                                                            "id": os.environ.get("entity_value_id"),
                                                            "entityId": os.environ.get("entity_id"),
                                                            "value": get_str(12),
                                                            "regex": "^[0-9]*$",
                                                            "synonyms": [],
                                                            "enableTokenization": ""
                                                        }
                                                    }
                                                }]}
                                            }
            , [], {}]
        self.param_update_entityvalue_068 = [{"agentId": os.environ.get("agent_id"),
                                              "data": {"mutateOperations": [
                                                  {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": False
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("enum_entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "^[0-9]*$",
                                                              "synonyms": [],
                                                              "enableTokenization": True
                                                          }
                                                      }
                                                  }, {
                                                      "entityValueOperation": {
                                                          "update": {
                                                              "id": os.environ.get("entity_value_id"),
                                                              "entityId": os.environ.get("enum_entity_id"),
                                                              "value": get_str(12),
                                                              "regex": "",
                                                              "synonyms": [get_str(1), get_str(1), get_str(1),
                                                                           get_str(1)],
                                                              "enableTokenization": True
                                                          }
                                                      }
                                                  }]}
                                              }
            , [], {}]
        # </editor-fold>

        # <editor-fold desc="删除实体值参数">
        self.param_delete_entityvalue_001 = [{"agentId": None,
                                            "data": {
                                                "mutateOperations": [
                                                    {"entityValueOperation": {
                                                        "delete": None
                                                    }
                                                    }]
                                            }}, [], {}]
        self.param_delete_entityvalue_002 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": None
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_003 = [{"agentId": None,
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": get_int(10)
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_004 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": ""
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_005 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": ""
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_006 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": get_int(10)
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_007 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": " "
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_008 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": " "
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_009 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": get_int(10)
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_010 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": os.environ.get("entity_value_id")
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_011 = [{"agentId": get_int(10),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": os.environ.get("entity_value_id")
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_012 = [{"agentId": get_str(4),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": os.environ.get("entity_value_id")
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_013 = [{"agentId": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": os.environ.get("entity_value_id")
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_014 = [{"agentId": "",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": os.environ.get("entity_value_id")
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_015 = [{"agentId": " ",
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": os.environ.get("entity_value_id")
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_016 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": get_str(4)
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_017 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": get_int(10)
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_018 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_019 = [{"agentId": os.environ.get("agent_id"),
                                            "data": {"mutateOperations": [
                                                {
                                                    "entityValueOperation": {
                                                        "delete": ""
                                                    }
                                                }]
                                            }}, [], {}]
        self.param_delete_entityvalue_020 = [{"agentId": os.environ.get("agent_id"),
                                              "data": {"mutateOperations": [
                                                  {
                                                      "entityValueOperation": {
                                                          "delete": " "
                                                      }
                                                  }]
                                              }}, [], {}]

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
        self.param_test_entityvalue_001 = [{"agent_id":None,
                                       "entity_id":None,
                                       "data": {"text": None,
                                      "regexes": [
                                          {
                                      "value": None,
                                      "regex": None
                                          }
                                                  ]
                                          }}, [], {}]
        self.param_test_entityvalue_002 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": None,
                                          "data": {"text": None,
                                                   "regexes": [
                                                       {
                                                           "value": None,
                                                           "regex": None
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_003 = [{"agent_id": None,
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": None,
                                                   "regexes": [
                                                       {
                                                           "value": None,
                                                           "regex": None
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_004 = [{"agent_id": None,
                                          "entity_id": None,
                                          "data": {"text": get_str(4),
                                                   "regexes": [
                                                       {
                                                           "value": None,
                                                           "regex": None
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_005 = [{"agent_id": None,
                                          "entity_id": None,
                                          "data": {"text": None,
                                                   "regexes": [
                                                       {
                                                           "value": get_str(4),
                                                           "regex": None
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_006 = [{"agent_id": None,
                                          "entity_id": None,
                                          "data": {"text": None,
                                                   "regexes": [
                                                       {
                                                           "value": None,
                                                           "regex": get_int(4)
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_007 = [{"agent_id": "",
                                          "entity_id": "",
                                          "data": {"text": "",
                                                   "regexes": [
                                                       {
                                                           "value": "",
                                                           "regex": ""
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_008 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": "",
                                          "data": {"text": "",
                                                   "regexes": [
                                                       {
                                                           "value": "",
                                                           "regex": ""
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_009 = [{"agent_id": "",
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "",
                                                   "regexes": [
                                                       {
                                                           "value": "",
                                                           "regex": ""
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_010 = [{"agent_id": "",
                                          "entity_id": "",
                                          "data": {"text": get_str(4),
                                                   "regexes": [
                                                       {
                                                           "value": "",
                                                           "regex": ""
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_011 = [{"agent_id": "",
                                          "entity_id": "",
                                          "data": {"text": "",
                                                   "regexes": [
                                                       {
                                                           "value": get_str(4),
                                                           "regex": ""
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_012 = [{"agent_id": "",
                                          "entity_id": "",
                                          "data": {"text": "",
                                                   "regexes": [
                                                       {
                                                           "value": "",
                                                           "regex": get_int(4)
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_013 = [{"agent_id": " ",
                                          "entity_id": " ",
                                          "data": {"text": " ",
                                                   "regexes": [
                                                       {
                                                           "value": " ",
                                                           "regex": " "
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_014 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": " ",
                                          "data": {"text": " ",
                                                   "regexes": [
                                                       {
                                                           "value": " ",
                                                           "regex": " "
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_015 = [{"agent_id": " ",
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": " ",
                                                   "regexes": [
                                                       {
                                                           "value": " ",
                                                           "regex": " "
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_016 = [{"agent_id": " ",
                                          "entity_id": " ",
                                          "data": {"text": get_str(4),
                                                   "regexes": [
                                                       {
                                                           "value": " ",
                                                           "regex": " "
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_017 = [{"agent_id": " ",
                                          "entity_id": " ",
                                          "data": {"text": " ",
                                                   "regexes": [
                                                       {
                                                           "value": get_str(4),
                                                           "regex": " "
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_018 = [{"agent_id": " ",
                                          "entity_id": " ",
                                          "data": {"text": " ",
                                                   "regexes": [
                                                       {
                                                           "value": " ",
                                                           "regex": get_int(4)
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_019 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_020 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("enum_entity_id"),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_021 = [{"agent_id": get_str(4),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_022 = [{"agent_id": get_int(4),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_023 = [{"agent_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_024 = [{"agent_id": "",
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_025 = [{"agent_id": " ",
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_026 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": get_str(4),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_027 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": get_int(4),
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_028 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_029 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_030 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": "",
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_031 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": " ",
                                          "data": {"text": "121312412312312",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_032 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": get_str(4),
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_033 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": get_int(4),
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_034 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_035 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_036 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": " ",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_037 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": get_str(128),
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_038 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": get_str(129),
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_039 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": get_int(128),
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_040 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_041 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": "",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_042 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": " ",
                                                           "regex": "^[0-9]*$"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_043 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": get_str(512)
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_044 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": get_int(513)
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_045 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><"
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_046 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": ""
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_047 = [{"agent_id": os.environ.get("agent_id"),
                                          "entity_id": os.environ.get("entity_id"),
                                          "data": {"text": "12367eqwwyeuiqwieasdj!@#$%^&*()_+:L><",
                                                   "regexes": [
                                                       {
                                                           "value": "数字",
                                                           "regex": " "
                                                       }
                                                   ]
                                                   }}, [], {}]
        self.param_test_entityvalue_048 = [{"agent_id": os.environ.get("agent_id"),
                                            "entity_id": os.environ.get("entity_id"),
                                            "data": {"text": "121312412312312",
                                                     "regexes": [
                                                         {
                                                             "value": "数字1",
                                                             "regex": "^[0-9]*$"
                                                         },{
                                                             "value": "数字2",
                                                             "regex": "^\d{n}$"
                                                         },{
                                                             "value": "数字3",
                                                             "regex": "^\d{4,}$"
                                                         },{
                                                             "value": "数字4",
                                                             "regex": "^\d{1,10}$"
                                                         },{
                                                             "value": "数字5",
                                                             "regex": "：^(0|[1-9][0-9]*)$$"
                                                         },{
                                                             "value": "数字6",
                                                             "regex": "^([1-9][0-9]*)+(.[0-9]{1,2})?$"
                                                         },{
                                                             "value": "数字7",
                                                             "regex": "^[1-9]\d*$"
                                                         },{
                                                             "value": "汉字",
                                                             "regex": "^[\u4e00-\u9fa5]{0,}$"
                                                         },{
                                                             "value": "英文和数字",
                                                             "regex": "^[A-Za-z0-9]+$"
                                                         }
                                                     ]
                                                     }}, [], {}]

        # </editor-fold>
