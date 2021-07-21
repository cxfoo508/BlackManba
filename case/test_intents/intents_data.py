# coding:utf-8
# Author : guanlu
# CONTACT: 719667588@qq.com
# SOFTWARE: PyCharm
# FILE : intents_data.py
# DATE : 2021/7/19 15:17
import os

from data_method import *

class intents_data_class:

    def __init__(self):
        """
        意图参数
        """

        """
        意图列表
        """
        self.param_list_001 = [{
                              "agent_id": None,
                              "search": {
                                "examples": None,
                                "intent_name":None
                              },
                              "filters": {
                                "intent_type": [None

                                ],
                                "trigger_type": [None

                                ],
                                "skill_type": [None
                                ]
                              },
                              "sort": {
                                "examples_count": None,
                                "update_time": None
                              },
                              "page_size": None,
                              "page_num": None
                            },[],{}]
        self.param_list_002 = [{
                              "agent_id": os.environ.get("agent_id"),
                              "search": {
                                "examples": None,
                                "intent_name":None
                              },
                              "filters": {
                                "intent_type": [None

                                ],
                                "trigger_type": [None

                                ],
                                "skill_type": [None
                                ]
                              },
                              "sort": {
                                "examples_count": None,
                                "update_time": None
                              },
                              "page_size": None,
                              "page_num": None
                            },[],{}]
        self.param_list_003 = [{
                                  "agent_id": get_int(10),
                                  "search": {
                                    "examples": None,
                                    "intent_name": None
                                  },
                                  "filters": {
                                    "intent_type": [

                                    ],
                                    "trigger_type": [

                                    ],
                                    "skill_type": [
                                    ]
                                  },
                                  "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },[],{}]
        self.param_list_004 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": "test",
                                    "intent_name": "test"
                                  },
                                  "filters": {
                                    "intent_type": [

                                    ],
                                    "trigger_type": [

                                    ],
                                    "skill_type": [
                                    ]
                                  },
                                  "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },[],{}]
        self.param_list_005 = [{
                                  "agent_id": os.environ.get("agent_id"),
                                  "search": {
                                    "examples": None,
                                    "intent_name": None
                                  },
                                  "filters": {
                                    "intent_type": [
                                            0
                                    ],
                                    "trigger_type": [

                                    ],
                                    "skill_type": [
                                    ]
                                  },
                                  "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                  },
                                  "page_size": 20,
                                  "page_num": 1
                                },[],{}]
        self.param_list_006 = [{
                                "agent_id": os.environ.get("agent_id"),
                                "search": {
                                    "examples": None,
                                    "intent_name": None
                                },
                                "filters": {
                                    "intent_type": [
                                        1
                                    ],
                                    "trigger_type": [

                                    ],
                                    "skill_type": [
                                    ]
                                },
                                "sort": {
                                    "examples_count": None,
                                    "update_time": None
                                },
                                "page_size": 20,
                                "page_num": 1
                            }, [], {}]
        self.param_list_007 = [{
                            "agent_id": os.environ.get("agent_id"),
                            "search": {
                                "examples": None,
                                "intent_name": None
                            },
                            "filters": {
                                "intent_type": [
                                    2
                                ],
                                "trigger_type": [

                                ],
                                "skill_type": [
                                ]
                            },
                            "sort": {
                                "examples_count": None,
                                "update_time": None
                            },
                            "page_size": 20,
                            "page_num": 1
                        }, [], {}]
        self.param_list_008 = [{
                            "agent_id": os.environ.get("agent_id"),
                            "search": {
                                "examples": None,
                                "intent_name": None
                            },
                            "filters": {
                                "intent_type": [
                                    3
                                ],
                                "trigger_type": [

                                ],
                                "skill_type": [
                                ]
                            },
                            "sort": {
                                "examples_count": None,
                                "update_time": None
                            },
                            "page_size": 20,
                            "page_num": 1
                        }, [], {}]
        self.param_list_009 = [{
                        "agent_id": os.environ.get("agent_id"),
                        "search": {
                            "examples": None,
                            "intent_name": None
                        },
                        "filters": {
                            "intent_type": [
                                0,1,2
                            ],
                            "trigger_type": [

                            ],
                            "skill_type": [
                            ]
                        },
                        "sort": {
                            "examples_count": None,
                            "update_time": None
                        },
                        "page_size": 20,
                        "page_num": 1
                    }, [], {}]
        self.param_list_010 = [{
                        "agent_id": os.environ.get("agent_id"),
                        "search": {
                            "examples": None,
                            "intent_name": None
                        },
                        "filters": {
                            "intent_type": [
                                0
                            ],
                            "trigger_type": [
                                0
                            ],
                            "skill_type": [
                            ]
                        },
                        "sort": {
                            "examples_count": None,
                            "update_time": None
                        },
                        "page_size": 20,
                        "page_num": 1
                    }, [], {}]
        self.param_list_011 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    1
                ],
                "skill_type": [
                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_012 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    2
                ],
                "skill_type": [
                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_013 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    3
                ],
                "skill_type": [
                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_014 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    4
                ],
                "skill_type": [
                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_015 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    0,1,2,3,4
                ],
                "skill_type": [
                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_016 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    0
                ],
                "skill_type": [

                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_017 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    "WWQW!@!#!@$!123123"
                ],
                "trigger_type": [
                    "WWQW!@!#!@$!123123"
                ],
                "skill_type": [

                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_018 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    0
                ],
                "skill_type": [

                ]
            },
            "sort": {
                "examples_count": 12,
                "update_time": 12
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_019 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    0
                ],
                "skill_type": [

                ]
            },
            "sort": {
                "examples_count": "123",
                "update_time": "123124"
            },
            "page_size": 20,
            "page_num": 1
        }, [], {}]
        self.param_list_020 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    0
                ],
                "skill_type": [

                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 200,
            "page_num": 1
        }, [], {}]
        self.param_list_021 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    0
                ],
                "skill_type": [

                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 201,
            "page_num": 1
        }, [], {}]
        self.param_list_022 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    0
                ],
                "skill_type": [

                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 200,
            "page_num": get_int(10)
        }, [], {}]
        self.param_list_023 = [{
            "agent_id": os.environ.get("agent_id"),
            "search": {
                "examples": None,
                "intent_name": None
            },
            "filters": {
                "intent_type": [
                    0
                ],
                "trigger_type": [
                    0
                ],
                "skill_type": [

                ]
            },
            "sort": {
                "examples_count": None,
                "update_time": None
            },
            "page_size": 0,
            "page_num": 0
        }, [], {}]
        """
        新增意图
        """
        self.param_create_001 = [{
                      "agent_id": None,
                      "intent_name": None,
                      "examples": [
                        {
                          "id": None,
                          "name": None
                        }
                      ],
                      "keywords_eq": [
                        {
                          "id": None,
                          "name": None
                        }
                      ],
                      "keywords_include": [
                        {
                          "id": None,
                          "name": None
                        }
                      ]
                    },[],{}]
        self.param_create_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_create_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_create_003 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_create_004 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_create_005 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_create_006 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_create_007 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_create_008 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_009 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_010 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": "test",
            "examples": [
                {
                    "id": None,
                    "name": "test"
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": "test"
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": "test"
                }
            ]
        }, [], {}]
        self.param_create_011 = [{
            "agent_id": get_int(10),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_011 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_int(10),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_012 = [{
            "agent_id": "12312321321423DFFFGGFGDjhhhfdf@#$$%%%^!",
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_013 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_int(4),
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_014 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": get_int(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id":  get_int(4),
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id":  get_int(4),
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_015 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": get_str(4),
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": get_str(4),
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_016 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": get_str(1),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id":  get_int(1),
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id":  get_int(1),
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_create_017= [{
            "agent_id": os.environ.get("agent_id"),
            "intent_name": get_str(4),
            "examples": [
                {
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                },{
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ]
        }, [], {}]
        """
        删除意图
        """
        self.param_del_001 = [{
            "agent_id": None,
            "intent_id": None
        }, [], {}]
        self.param_del_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": None
        }, [], {}]
        self.param_del_003 = [{
            "agent_id": get_int(4),
            "intent_id": None
        }, [], {}]
        self.param_del_004 = [{
            "agent_id": "1231FGFJHFJFJFJffjfj$$!%^@&#",
            "intent_id": None
        }, [], {}]
        self.param_del_005 = [{
            "agent_id": None,
            "intent_id": get_int(4)
        }, [], {}]
        self.param_del_006 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_int(4)
        }, [], {}]
        self.param_del_007 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": "123123asjhjahkdahk#$@&&672991!@"
        }, [], {}]
        self.param_del_008 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id")
        }, [], {}]
        self.param_del_009 = [{
            "agent_id": get_int(4),
            "intent_id": get_int(4)
        }, [], {}]
        """
        单个意图详情
        """
        self.param_datail_intents_001 = [{
            "agent_id": None,
            "intent_id": None
        }, [], {}]
        self.param_datail_intents_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": None
        }, [], {}]
        self.param_datail_intents_003 = [{
            "agent_id": get_int(4),
            "intent_id": None
        }, [], {}]
        self.param_datail_intents_004 = [{
            "agent_id": "1231FGFJHFJFJFJffjfj$$!%^@&#",
            "intent_id": None
        }, [], {}]
        self.param_datail_intents_005 = [{
            "agent_id": None,
            "intent_id": get_int(4)
        }, [], {}]
        self.param_datail_intents_006 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_int(4)
        }, [], {}]
        self.param_datail_intents_007 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": "123123asjhjahkdahk#$@&&672991!@"
        }, [], {}]
        self.param_datail_intents_008 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id")
        }, [], {}]
        self.param_datail_intents_009 = [{
            "agent_id": get_int(4),
            "intent_id": get_int(4)
        }, [], {}]
        """
        编辑意图
        """
        self.param_edit_001 = [{
            "agent_id": None,
            "intent_id": None,
            "intent_name": None,
            "intent_type": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_002 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": None,
            "intent_name": None,
            "intent_type": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_003 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": get_int(4),
            "intent_name": None,
            "intent_type": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_004 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": None,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_005 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_006 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": None
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_007 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_008 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": None
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_009 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_010 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": None
                }
            ]
        }, [], {}]
        self.param_edit_011 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_edit_012 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 0,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_edit_013 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": None,
                    "name": "test"
                }
            ],
            "keywords_eq": [
                {
                    "id": None,
                    "name": "test"
                }
            ],
            "keywords_include": [
                {
                    "id": None,
                    "name": "test"
                }
            ]
        }, [], {}]
        self.param_edit_014 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(128),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_edit_015 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_int(10),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_edit_016 = [{
            "agent_id": "12312321321423DFFFGGFGDjhhhfdf@#$$%%%^!",
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_edit_017 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": "12312321321423DFFFGGFGDjhhhfdf@#$$%%%^!",
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_edit_018 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": "12312321321423DFFFGGFGDjhhhfdf@#$$%%%^!",
            "examples": [
                {
                    "id": 1,
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_edit_019 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": 1,
                    "name": get_str(128)
                }
            ],
            "keywords_eq": [
                {
                    "id": 1,
                    "name": get_str(128)
                }
            ],
            "keywords_include": [
                {
                    "id": 1,
                    "name": get_str(128)
                }
            ]
        }, [], {}]
        self.param_edit_020 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": get_int(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                }
            ],
            "keywords_include": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                }
            ]
        }, [], {}]
        self.param_edit_021 = [{
            "agent_id": os.environ.get("agent_id"),
            "intent_id": os.environ.get("intents_id"),
            "intent_name": get_str(4),
            "intent_type": 1,
            "examples": [
                {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ],
            "keywords_eq": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ],
            "keywords_include": [
                {
                    "id": get_int(4),
                    "name": get_str(2)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }, {
                    "id": get_str(4),
                    "name": get_str(4)
                }
            ]
        }, [], {}]

