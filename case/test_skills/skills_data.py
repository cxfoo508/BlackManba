import os

from data_method import *


class skills_data_class:
    def __init__(self):
        # <editor-fold desc = "新建技能">
        self.params_case_001 = [
            {  # faq
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]',
             'skill_id': 'res["data"]["skill_id"]'
             }]
        self.params_case_001_1_1 = [
            {  # 对话树
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 1,
                "category_id": os.environ.get('category_id'),
                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "skill_name": get_str(4),
                    "description": get_int(4)
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]', 'skill_id': 'res["data"]["skill_id"]',
             "skill_name": 'req["skill_content"]["skill_name"]'
             }]
        self.params_case_001_1_2 = [
            {  # faq-多个值
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    },
                        {
                            "resp_content": '我是回复',
                            "resp_type_id": 2
                        },
                        {
                            "resp_content": '我是回复2',
                            "resp_type_id": 2
                        },
                        {
                            "resp_content": '我是回复3',
                            "resp_type_id": 2
                        },
                        {
                            "resp_content": '我是回复4',
                            "resp_type_id": 2
                        }
                    ]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]'}]
        self.params_case_001_1_3 = [
            {  # faq-多个值
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 3,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    },
                        {
                            "resp_content": '我是回复',
                            "resp_type_id": 2
                        },
                        {
                            "resp_content": '我是回复2',
                            "resp_type_id": 2
                        },
                        {
                            "resp_content": '我是回复3',
                            "resp_type_id": 2
                        },
                        {
                            "resp_content": '我是回复4',
                            "resp_type_id": 2
                        }
                    ]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]'}]

        self.params_case_001_1_4 = [
            {  # faq
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]',
             'skill_id': 'res["data"]["skill_id"]'
             }, {"sleep_time": 1}
        ]

        self.params_case_001_1 = [
            {
                # 必填项
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'],
            {}]
        self.params_case_001_2 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][0]["loc"][1]=="skill_type"',
                'res["data"][0]["msg"]=="field required"'],
            {}]
        self.params_case_001_3 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_id"',
                'res["data"][0]["msg"]=="field required"'],
            {}]
        self.params_case_001_4 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][0]["loc"][1]=="intent_id"',
                'res["data"][0]["msg"]=="field required"'],
            {}]
        self.params_case_001_5 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][2]["loc"][2]=="custom_action_id_list"',
                'res["data"][0]["msg"]=="field required"'],
            {}]
        self.params_case_001_6 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][2]["loc"][2]=="mode_type"',
                'res["data"][0]["msg"]=="field required"'],
            {}]
        self.params_case_001_7 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,

                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][2]["loc"][2]=="faq_responses"',
                'res["data"][0]["msg"]=="field required"'],
            {}]

        self.params_case_001_8 = [
            {
                # 回复类型-image
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": 'https://laiye-tech.feishu.cn/file/boxcn9dlLodcSHnLUbiy5e4aJvc',
                        "resp_type_id": 3
                    }]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]'}]
        self.params_case_001_9 = [
            {
                # 回复类型-默认
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '默认回复',
                        "resp_type_id": 1
                    }]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]'}]
        self.params_case_001_10 = [
            {
                # 回复类型-语音
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": 'https://laiye-tech.feishu.cn/file/boxcn23MiHh57Bchpl5mdTy42Wb',
                        "resp_type_id": 4
                    }]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]'}]
        self.params_case_001_11 = [
            {
                # 回复类型-text-特殊符号
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '你好啊！@#¥%……？sdfasdfad  sf',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==0', 'res["msg"] == "创建技能成功"', 'res["data"]["skill_id"]!=None',
                'res["data"]["skill_one_id"]!=None'],
            {'skill_one_id': 'res["data"]["skill_one_id"]',
             'resp_content': 'req["skill_content"]["faq_responses"][0]["resp_content"]'}]

        self.params_case_001_12 = [
            {
                # None
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),
                "agent_id": None,
                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="none is not an allowed value"'],
            {}]
        self.params_case_001_13 = [
            {
                # None
                "agent_id": os.environ.get('agent_id'),
                "category_id": os.environ.get('category_id'),
                "skill_type": None,
                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][0]["loc"][1]=="skill_type"',
                'res["data"][0]["msg"]=="none is not an allowed value"'],
            {}]
        self.params_case_001_14 = [
            {
                # None
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "intent_id": os.environ.get('intent_id'),
                "category_id": None,
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_id"',
                'res["data"][0]["msg"]=="none is not an allowed value"'],
            {}]
        self.params_case_001_15 = [
            {
                # None
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),
                "intent_id": None,
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][0]["loc"][1]=="intent_id"',
                'res["data"][0]["msg"]=="none is not an allowed value"'],
            {}]
        self.params_case_001_16 = [
            {
                # None
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": None,
                    "mode_type": 1,
                    "faq_responses": [{

                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][2]["loc"][2]=="custom_action_id_list"',
                'res["data"][2]["msg"]=="none is not an allowed value"'],
            {}]
        self.params_case_001_17 = [
            {
                # None
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": None,
                    "faq_responses": [{
                        "resp_content": '我是回复',
                        "resp_type_id": 2
                    }]
                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][2]["loc"][2]=="mode_type"',
                'res["data"][2]["msg"]=="none is not an allowed value"'],
            {}]
        self.params_case_001_18 = [
            {
                # None
                "agent_id": os.environ.get('agent_id'),
                "skill_type": 4,
                "category_id": os.environ.get('category_id'),

                "intent_id": os.environ.get('intent_id'),
                "skill_content": {
                    "custom_action_id_list": [],
                    "mode_type": 1,
                    "faq_responses": None

                }
            }, ['res["code"]==10009', 'res["msg"] == "接口参数验证出错"', 'res["data"][2]["loc"][2]=="faq_responses"',
                'res["data"][2]["msg"]=="none is not an allowed value"'],
            {}]
        # </editor-fold>

        # <editor-fold desc = "获取机器人分类树全部节点">
        self.params_case_002 = [
            {
                "agent_id": os.environ.get('agent_id')
            },
            ['res["code"]==0', 'res["data"][0]["category_id"]!=None'], {'category_id': 'res["data"][0]["category_id"]'}
        ]
        self.params_case_002_1 = [
            {
                "agent_id": os.environ.get('agent_id')
            },
            ['res["code"]==0', 'res["data"][0]["category_id"]!=None', 'len(res["data"])==21'],
            {'category_id': 'res["data"][0]["category_id"]'}
        ]
        self.params_case_002_2 = [
            {
                "agent_id": os.environ.get('agent_id')
            },
            ['res["code"]==0', 'res["data"][0]["category_id"]!=None', 'len(res["data"])==2'],
            {'category_id': 'res["data"][0]["category_id"]'}
        ]
        self.params_case_002_3 = [
            {
                "agent_id": os.environ.get('agent_id')
            },
            ['res["code"]==0', 'res["data"][0]["category_id"]!=None', 'len(res["data"])==2',
             'res["data"][1]["category_name"]==os.environ.get("category_name_2")'],
            {'category_id': 'res["data"][0]["category_id"]'}
        ]
        self.params_case_002_4 = [
            {
                "agent_id": os.environ.get('agent_id')
            },
            ['res["code"]==0', 'res["data"][0]["category_id"]!=None', 'len(res["data"])==1'],
            {'category_id': 'res["data"][0]["category_id"]'}
        ]
        # </editor-fold>

        # <editor-fold desc = "设置技能是否生效">
        self.params_case_003 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id'),
                "skill_status": 1
            },
            [], {}, {"sleep_time": 10}

        ]
        # </editor-fold>

        # <editor-fold desc = "获取回复">
        self.params_case_004 = [
            {
                "msg_body": {
                    "text": {"content": '相似问测试'}
                },
                "agent_id": os.environ.get('agent_id')
            }, ['res["code"]==0',
                'res["data"]["responses"][0]["msg_body"]["text"]["content"]==os.environ.get("resp_content")'], {}
        ]
        self.params_case_004_1 = [
            {
                "msg_body": {
                    "text": {"content": '相似问测试'}
                },
                "agent_id": os.environ.get('agent_id')
            }, ['res["code"]==0',
                'len(res["data"]["responses"])==5'], {}
        ]
        self.params_case_004_2 = [
            {
                "msg_body": {
                    "text": {"content": '相似问测试'}
                },
                "agent_id": os.environ.get('agent_id')
            }, ['res["code"]==0',
                'res["data"]["responses"][0]["msg_body"]["text"]["content"]=="跟节点回复"'], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "删除技能">
        self.params_case_005 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_id": os.environ.get('skill_id'),
                "skill_one_id": os.environ.get('skill_one_id')
            },
            ['res["code"]==0', 'res["msg"]=="删除技能成功"'], {}
        ]
        self.params_case_005_1 = [
            {
                # 必填项
                "skill_id": os.environ.get('skill_id'),
                "skill_one_id": os.environ.get('skill_one_id')
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
             'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.params_case_005_2 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "skill_one_id": os.environ.get('skill_one_id')
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="skill_id"',
             'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.params_case_005_3 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "skill_id": os.environ.get('skill_id'),
            },
            ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="skill_one_id"',
             'res["data"][0]["msg"]=="field required"'], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "获取技能列表">
        self.params_case_006 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "page_size": 5,
                "page_num": 1
            }
            , ['res["code"]==0', 'len(res["data"]["skills_list"])==0'], {}
        ]

        self.params_case_006_1 = [
            {  # 搜索
                "agent_id": os.environ.get('agent_id'),
                "search": {
                    "skill_name": os.environ.get('skill_name')
                },
                "page_size": 20,
                "page_num": 1
            }, ['res["code"]==0', 'res["data"]["total_num"]==1',
                'res["data"]["skills_list"][0]["skill_name"]==os.environ.get("skill_name")'], {}
        ]
        self.params_case_006_2 = [
            {  # 筛选
                "agent_id": os.environ.get('agent_id'),
                "filters": {
                    "skill_type": [1]
                },
                "page_size": 20,
                "page_num": 1
            }, ['res["code"]==0', 'res["data"]["total_num"]==1',
                'res["data"]["skills_list"][0]["skill_type"]==1'], {}
        ]
        self.params_case_006_3 = [
            {  # 筛选
                "agent_id": os.environ.get('agent_id'),
                "filters": {
                    "skill_type": [4]
                },
                "page_size": 20,
                "page_num": 1
            }, ['res["code"]==0', 'res["data"]["total_num"]==1',
                'res["data"]["skills_list"][0]["skill_type"]==4'], {}
        ]
        self.params_case_006_4 = [
            {  # 筛选
                "agent_id": os.environ.get('agent_id'),
                "filters": {
                    "skill_status": [1]
                },
                "page_size": 20,
                "page_num": 1
            }, ['res["code"]==0', 'res["data"]["total_num"]==1',
                'res["data"]["skills_list"][0]["skill_status"]==1'], {}
        ]
        self.params_case_006_5 = [
            {  # 筛选
                "agent_id": os.environ.get('agent_id'),
                "filters": {
                    "skill_status": [2]
                },
                "page_size": 20,
                "page_num": 1
            }, ['res["code"]==0', 'res["data"]["total_num"]==1',
                'res["data"]["skills_list"][0]["skill_status"]==2'], {}
        ]
        self.params_case_006_6 = [
            {  # 筛选-未实现
                "agent_id": os.environ.get('agent_id'),
                "filters": {
                    "category_id": None
                },
                "page_size": 20,
                "page_num": 1
            }, ['res["code"]==0', 'res["data"]["total_num"]==1',
                'res["data"]["skills_list"][0]["skill_status"]==2'], {}
        ]
        self.params_case_006_7 = [
            {  # 排序
                "agent_id": os.environ.get('agent_id'),
                "sort": {
                    "update_time": "ascend",
                    "answer_count": None
                },
                "page_size": 20,
                "page_num": 1
            }, ['res["code"]==0', 'res["data"]["total_num"]==2',
                'res["data"]["skills_list"][0]["skill_type"]==4'], {}
        ]
        self.params_case_006_8 = [
            {  #
                "agent_id": os.environ.get('agent_id'),
                "sort": {
                    "update_time": None,
                    "answer_count": "ascend"
                },
                "page_size": 20,
                "page_num": 1
            }, ['res["code"]==0', 'res["data"]["total_num"]==2',
                'res["data"]["skills_list"][0]["skill_type"]==1'], {}
        ]
        self.params_case_006_9 = [
            {
                # 分页
                "agent_id": os.environ.get('agent_id'),
                "page_size": 5,
                "page_num": 2
            }
            , ['res["code"]==0', 'len(res["data"]["skills_list"])==2'], {}
        ]
        self.params_case_006_10 = [
            {
                # 分页
                "agent_id": os.environ.get('agent_id'),
                "page_size": 5,
                "page_num": 1
            }
            , ['res["code"]==0', 'len(res["data"]["skills_list"])==5'], {}
        ]
        self.params_case_006_11 = [
            {  # 必填项
                "page_size": 5,
                "page_num": 1
            }
            , ['res["code"]==0', 'len(res["data"]["skills_list"])==5'], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "创建分类节点">
        self.params_case_007 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "category_name": get_str(4),
                "parent_id": os.environ.get('category_id')
            }, ['res["code"]==0', 'res["msg"]=="创建分类成功"', 'res["data"]["category_id"]!=None'],
            {}
        ]
        self.params_case_007_1 = [
            {
                "category_name": get_str(4),
                "parent_id": os.environ.get('category_id')
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.params_case_007_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('category_id')
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_name"',
                'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.params_case_007_3 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "category_name": get_str(4),
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="parent_id"',
                'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.params_case_007_4 = [
            {  # name
                "agent_id": os.environ.get('agent_id'),
                "category_name": get_str(128),
                "parent_id": os.environ.get('category_id')
            }, ['res["code"]==0', 'res["msg"]=="创建分类成功"', 'res["data"]["category_id"]!=None'],
            {}
        ]
        self.params_case_007_5 = [
            {  # name
                "agent_id": os.environ.get('agent_id'),
                "category_name": get_str(129),
                "parent_id": os.environ.get('category_id')
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_name"',
                'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'],
            {}
        ]
        self.params_case_007_6 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "category_name": get_str(4),
                "parent_id": os.environ.get('category_id')
            }, ['res["code"]==0', 'res["msg"]=="创建分类成功"', 'res["data"]["category_id"]!=None'],
            {'category_id': 'res["data"]["category_id"]', 'parent_id': 'res["data"]["parent_id"]',
             'category_name_1': 'res["data"]["category_name"]'}
        ]

        # </editor-fold>

        # <editor-fold desc = "更新分类节点">
        self.params_case_008 = [
            # <<<<<<< HEAD
            {  # 更新名称
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id'),
                "category_name": get_str(5)
            }, ['res["code"]==0'],
            {'category_name_2': 'req["category_name"]'}
        ]
        self.params_case_008_1 = [
            {  # 更新名称
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id'),
                "category_name": get_str(5) + '~!@#$%^&*  < > ?'
            }, ['res["code"]==0'],
            {'category_name_2': 'req["category_name"]'}
        ]
        self.params_case_008_2 = [
            {  # 更新名称
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id'),
                "category_name": None
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_name"',
                'res["data"][0]["msg"]=="none is not an allowed value"'],
            {'category_name_2': 'req["category_name"]'}
        ]
        self.params_case_008_3 = [
            {  # 更新名称
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id'),
                "category_name": get_str(128)
            }, ['res["code"]==0'],
            {'category_name_2': 'req["category_name"]'}
        ]
        self.params_case_008_4 = [
            {  # 更新名称
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id'),
                "category_name": get_str(129)
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_name"',
                'res["data"][0]["msg"]=="ensure this value has at most 128 characters"'],
            {'category_name_2': 'req["category_name"]'}
        ]
        self.params_case_008_5 = [
            {  # 必填项
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id'),
                "category_name": get_str(5)
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'],
            {'category_name_2': 'req["category_name"]'}
        ]
        self.params_case_008_6 = [
            {  # 更新名称
                "agent_id": os.environ.get('agent_id'),
                "category_id": os.environ.get('category_id'),
                "category_name": get_str(5)
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="parent_id"',
                'res["data"][0]["msg"]=="field required"'],
            {'category_name_2': 'req["category_name"]'}
        ]
        self.params_case_008_7 = [
            {  # 更新名称
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
                "category_name": get_str(5)
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_id"',
                'res["data"][0]["msg"]=="field required"'],
            {'category_name_2': 'req["category_name"]'}
        ]
        self.params_case_008_8 = [
            {  # 更新名称
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id'),
            }, ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_name"',
                'res["data"][0]["msg"]=="field required"'],
            {}
        ]

        # </editor-fold>

        # <editor-fold desc = "删除分类节点">
        self.params_case_009 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id')
            }
            , ['res["code"]==0'], {}
        ]
        self.params_case_009_1 = [
            {
                "parent_id": os.environ.get('parent_id'),
                "category_id": os.environ.get('category_id')
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
               'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.params_case_009_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "category_id": os.environ.get('category_id')
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="parent_id"',
               'res["data"][0]["msg"]=="field required"'], {}
        ]
        self.params_case_009_3 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "parent_id": os.environ.get('parent_id'),
            }
            , ['res["code"]==10009', 'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="category_id"',
               'res["data"][0]["msg"]=="field required"'], {}
        ]
        # </editor-fold>
