class skills_sort_class:
    skills_set_up = {
        "sort": ["auth_login", "creat_app"],
        "params": ["node_data_class.param_005", "node_data_class.param_006"]
    }
    # <editor-fold desc = "创建技能">
    skills_case_001 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_change_status", "agent_train_publish_start",
                 "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001", "skills_data_class.params_case_003",
                   "app_data_class.param_agent_start",
                   "skills_data_class.params_case_004"
                   ]
    }
    skills_case_001_2 = {
        # 全部回复
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_change_status", "agent_train_publish_start",
                 "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_1_2", "skills_data_class.params_case_003",
                   "app_data_class.param_agent_start",
                   "skills_data_class.params_case_004_1"
                   ]
    }
    skills_case_001_3 = {
        # 随机回复
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_change_status", "agent_train_publish_start",
                 "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_1_3", "skills_data_class.params_case_003",
                   "app_data_class.param_agent_start",
                   "skills_data_class.params_case_004_2"
                   ]
    }
    skills_case_001_1 = {
        # 对话树-root
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create", "node_base_class.get_dialog_tree_root_node",
                 'node_base_class.update_dialog_tree_root_node', "skills_base_class.skill_change_status",
                 "agent_train_publish_start", "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_1_1", "node_data_class.param_009",
                   "node_data_class.param_010", "skills_data_class.params_case_003", "app_data_class.param_agent_start",
                   "skills_data_class.params_case_004_2"
                   ]
    }
    skills_case_001_2 = {
        # 对话树-成功结束
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create", "node_base_class.get_dialog_tree_root_node",
                 'node_base_class.update_dialog_tree_root_node', 'node_base_class.update_dialog_tree_complete_node',
                 "skills_base_class.skill_change_status",
                 "agent_train_publish_start", "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_1_1", "node_data_class.param_009",
                   "node_data_class.param_010", 'node_data_class.param_010_1', "skills_data_class.params_case_003",
                   "app_data_class.param_agent_start",
                   "skills_data_class.params_case_004_2"
                   ]
    }

    skills_case_002 = {
        # 必填项
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_1"
                   ]
    }

    skills_case_003 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_2"
                   ]
    }

    skills_case_004 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_3"
                   ]
    }

    skills_case_005 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_4"
                   ]
    }
    skills_case_006 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_5"
                   ]
    }
    skills_case_007 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_6"
                   ]
    }
    skills_case_008 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_7"
                   ]
    }
    skills_case_009 = {
        # 回复类型-image 不支持
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_change_status", "agent_train_publish_start",
                 "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_8", "skills_data_class.params_case_003",
                   "app_data_class.param_agent_start",
                   "skills_data_class.params_case_004"
                   ]
    }
    skills_case_010 = {
        # 回复类型-text特殊符号
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_change_status", "agent_train_publish_start",
                 "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_11", "skills_data_class.params_case_003",
                   "app_data_class.param_agent_start",
                   "skills_data_class.params_case_004"
                   ]
    }
    skills_case_011 = {
        # 回复类型-语音 不支持
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_change_status", "agent_train_publish_start",
                 "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_10", "skills_data_class.params_case_003",
                   "app_data_class.param_agent_start",
                   "skills_data_class.params_case_004"
                   ]
    }
    skills_case_012 = {
        # none
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_12"
                   ]
    }
    skills_case_013 = {
        # none
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_13"
                   ]
    }
    skills_case_014 = {
        # none
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_14"
                   ]
    }
    skills_case_015 = {
        # none
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_15"
                   ]
    }
    skills_case_016 = {
        # none
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_16"
                   ]
    }
    skills_case_017 = {
        # none
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_17"
                   ]
    }
    skills_case_018 = {
        # none
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_18"
                   ]
    }
    # </editor-fold>

    # <editor-fold desc = "删除技能">
    skills_case_019 = {
        # 训练生效后删除
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_change_status", "agent_train_publish_start",
                 "skills_base_class.skill_delete", 'skills_base_class.skill_list'
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001", "skills_data_class.params_case_003",
                   "app_data_class.param_agent_start", "skills_data_class.params_case_005",
                   "skills_data_class.params_case_006"
                   ]
    }
    skills_case_020 = {
        # 为生效训练删除
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_delete", 'skills_base_class.skill_list'
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001",
                   "skills_data_class.params_case_005",
                   "skills_data_class.params_case_006"
                   ]
    }
    skills_case_021 = {
        # 必填项
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_delete",
                 "skills_base_class.skill_delete",
                 "skills_base_class.skill_delete",
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001",
                   "skills_data_class.params_case_005_1",
                   "skills_data_class.params_case_005_2",
                   "skills_data_class.params_case_005_3",
                   ]
    }
    # </editor-fold>

    # <editor-fold desc = "获取技能列表">
    skills_case_022 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create", "skills_base_class.skill_create",
                 "skills_base_class.skill_change_status", "skills_base_class.skill_list",
                 "skills_base_class.skill_list",
                 "skills_base_class.skill_list",
                 "skills_base_class.skill_list",
                 "skills_base_class.skill_list",
                 "skills_base_class.skill_list",
                 "skills_base_class.skill_list"
                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001", "skills_data_class.params_case_001_1_1",
                   "skills_data_class.params_case_003", "skills_data_class.params_case_006_1",
                   "skills_data_class.params_case_006_2", "skills_data_class.params_case_006_3",
                   "skills_data_class.params_case_006_4", "skills_data_class.params_case_006_5",
                   "skills_data_class.params_case_006_7", "skills_data_class.params_case_006_8",
                   ]
    }
    skills_case_023 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create", "skills_base_class.skill_create",
                 "skills_base_class.skill_create",
                 "skills_base_class.skill_create", "skills_base_class.skill_create",
                 "skills_base_class.skill_create", "skills_base_class.skill_create",
                 "skills_base_class.skill_list", "skills_base_class.skill_list"

                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001", "skills_data_class.params_case_001_1_1",
                   "skills_data_class.params_case_001_1_1",
                   "skills_data_class.params_case_001_1_1", "skills_data_class.params_case_001_1_1",
                   "skills_data_class.params_case_001_1_1", "skills_data_class.params_case_001_1_1",
                   "skills_data_class.params_case_006_9", "skills_data_class.params_case_006_10"

                   ]
    }
    skills_case_024 = {
        "sort": ["create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create", "skills_base_class.skill_list"

                 ],
        "params": ["node_data_class.param_007", "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001","skills_data_class.params_case_006_11"

                   ]
    }
    # </editor-fold>
    # 所有变量名称集合
    param_list = dir()
    print(param_list)

    @classmethod
    def get_skills_data(cls, parm_name=None) -> list:
        """
        返回变量名称集合
        """
        print(__name__)
        lists = []
        if parm_name is None:
            for i in cls.param_list:
                if "case" in i:
                    lists.append('skills_sort_class.' + i)
        else:
            for item in cls.param_list:
                if parm_name in item:
                    lists.append('skills_sort_class.' + item)
        return lists
