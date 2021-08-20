
class rule_sort_class:
    # <editor-fold desc = "创建节点">
    node_case_003 = {"sort": ["node_base_class.node_create", 'node_base_class.node_list'],
                     'params': ['node_data_class.param_004', 'node_data_class.param_001']}
    node_case_004 = {"sort": ['create_intent', "node_base_class.node_create",
                              'create_intent', "node_base_class.node_create",
                              'node_base_class.node_list'],
                     'params': ["node_data_class.param_007_2", 'node_data_class.param_004_1',
                                "node_data_class.param_007_2", 'node_data_class.param_004_2',
                                'node_data_class.param_001_4']}
    # 多节点 order
    node_case_004_1 = {"sort": ['create_intent', "node_base_class.node_create",
                                'create_intent', "node_base_class.node_create",
                                'create_intent', "node_base_class.node_create",
                                'node_base_class.node_list'],
                       'params': ["node_data_class.param_007_2", 'node_data_class.param_004_1',
                                  "node_data_class.param_007_2", 'node_data_class.param_004_2',
                                  "node_data_class.param_007_2", 'node_data_class.param_004_2_1',
                                  'node_data_class.param_001_5']}
    node_case_005 = {"sort": ["node_base_class.node_create", "node_base_class.node_create",
                              "node_base_class.node_create", "node_base_class.node_create"],
                     'params': ['node_data_class.param_004_3', 'node_data_class.param_004_4',
                                'node_data_class.param_004_5', 'node_data_class.param_004_6']}
    node_case_006 = {"sort": ["node_base_class.node_create", "node_base_class.node_create",
                              ],
                     'params': ['node_data_class.param_004_7', 'node_data_class.param_004_8',
                                ]}
    # 绑定实体
    node_case_007 = {"sort": ['create_intent', "node_base_class.node_create"],
                     'params': ["node_data_class.param_007_2", 'node_data_class.param_004_2_2']}
    # 绑定实体-必填项
    node_case_008 = {"sort": ['create_intent', "node_base_class.node_create"],
                     'params': ["node_data_class.param_007_2", 'node_data_class.param_004_2_3']}
    node_case_009 = {"sort": ['create_intent', "node_base_class.node_create"],
                     'params': ["node_data_class.param_007_2", 'node_data_class.param_004_2_4']}
    # </editor-fold>
    # <editor-fold desc = "删除节点">
    node_case_010 = {"sort": ["node_base_class.node_create", 'node_base_class.node_list',
                              "node_base_class.node_del", 'node_base_class.node_list'
                              ],
                     'params': ['node_data_class.param_004', 'node_data_class.param_001',
                                'node_data_class.param_011', 'node_data_class.param_001_6'
                                ]}
    node_case_011 = {"sort": ['create_intent', "node_base_class.node_create",
                              "node_base_class.node_del", 'node_base_class.node_list'
                              ],
                     'params': ["node_data_class.param_007_2", 'node_data_class.param_004_2_2',
                                'node_data_class.param_011', 'node_data_class.param_001_6'
                                ]}
    node_case_012 = {"sort": ['create_intent', "node_base_class.node_create",
                              "node_base_class.node_del", "node_base_class.node_del",
                              "node_base_class.node_del"
                              ],
                     'params': ["node_data_class.param_007_2", 'node_data_class.param_004_2_2',
                                'node_data_class.param_011_1', 'node_data_class.param_011_2',
                                'node_data_class.param_011_3'
                                ]}
    # </editor-fold>

    # <editor-fold desc = "获取节点列表">
    node_case_001 = {"sort": ["node_base_class.node_list"], 'params': ['node_data_class.param_001']}
    node_case_001_2 = {"sort": ["node_base_class.node_list"], 'params': ['node_data_class.param_001_3']}
    ode_case_013 = {"sort": ['create_intent', "node_base_class.node_create",
                             'create_intent', "node_base_class.node_create",
                             'create_intent', "node_base_class.node_create",
                             'node_base_class.node_list'],
                    'params': ["node_data_class.param_007_2", 'node_data_class.param_004_1',
                               "node_data_class.param_007_2", 'node_data_class.param_004_2',
                               "node_data_class.param_007_2", 'node_data_class.param_004_2_1',
                               'node_data_class.param_001_2']}
    node_case_014 = {"sort": ["node_base_class.node_list"], 'params': ['node_data_class.param_001_7']}
    node_case_015 = {"sort": ["node_base_class.node_list"], 'params': ['node_data_class.param_001_8']}
    # </editor-fold>
    # <editor-fold desc = "获取指定节点">
    node_case_016 = {"sort": ["node_base_class.node_getnode"], 'params': ['node_data_class.param_012_1']}
    ode_case_017 = {"sort": ['create_intent', "node_base_class.node_create",
                             'create_intent', "node_base_class.node_create",
                             'create_intent', "node_base_class.node_create",
                             'node_base_class.node_getnode'],
                    'params': ["node_data_class.param_007_2", 'node_data_class.param_004_1',
                               "node_data_class.param_007_2", 'node_data_class.param_004_2',
                               "node_data_class.param_007_2", 'node_data_class.param_004_2_1',
                               'node_data_class.param_012']}
    node_case_018 = {"sort": ["node_base_class.node_getnode"], 'params': ['node_data_class.param_012_2']}
    node_case_019 = {"sort": ["node_base_class.node_getnode"], 'params': ['node_data_class.param_012_3']}
    # </editor-fold>
    # <editor-fold desc = "获取指定节点的子节点">
    node_case_020 = {"sort": ["node_base_class.node_getchilds"], 'params': ['node_data_class.param_013_3']}
    node_case_021 = {"sort": ['create_intent', "node_base_class.node_create",
                              'create_intent', "node_base_class.node_create",
                              'create_intent', "node_base_class.node_create",
                              'node_base_class.node_getchilds'],
                     'params': ["node_data_class.param_007_2", 'node_data_class.param_004_1',
                                "node_data_class.param_007_2", 'node_data_class.param_004_2',
                                "node_data_class.param_007_2", 'node_data_class.param_004_2_1',
                                'node_data_class.param_013_2']}
    node_case_022 = {"sort": ["node_base_class.node_getchilds"], 'params': ['node_data_class.param_013_4']}
    node_case_023 = {"sort": ["node_base_class.node_getchilds"], 'params': ['node_data_class.param_013_5']}
    node_case_024 = {"sort": ['create_intent', "node_base_class.node_create",
                              'create_intent', "node_base_class.node_create",
                              'create_intent', "node_base_class.node_create",
                              'node_base_class.node_getchilds'],
                     'params': ["node_data_class.param_007_2", 'node_data_class.param_004_1',
                                "node_data_class.param_007_2", 'node_data_class.param_004_2',
                                "node_data_class.param_007_2", 'node_data_class.param_004_2_1',
                                'node_data_class.param_013_6']}
    # </editor-fold>

    # <editor-fold desc = "set_up&&teardown">
    node_set_up = {
        "sort": ["auth_login", "creat_app", "create_intent", "skills_base_class.skill_category_all",
                 "skills_base_class.skill_create", "node_base_class.get_dialog_tree_root_node",
                 'node_base_class.update_dialog_tree_root_node'
                 # , "skills_base_class.skill_change_status",
                 # "agent_train_publish_start", "ChatMessageCase.chat_get_response"
                 ],
        "params": ["node_data_class.param_005", "node_data_class.param_006", "node_data_class.param_007",
                   "skills_data_class.params_case_002",
                   "skills_data_class.params_case_001_1_1", "node_data_class.param_009",
                   "node_data_class.param_010",
                   # "skills_data_class.params_case_003",
                   # "app_data_class.param_agent_start",
                   # "skills_data_class.params_case_004_2"
                   ]
    }
    node_teardown = {
        "sort": ["del_app"],
        "params": ["node_data_class.param_008"]
    }
    # </editor-fold>
    # 所有变量名称集合
    param_list = dir()
    print(param_list)

    @classmethod
    def get_node_list(cls, parm_name=None) -> list:
        """
        返回变量名称集合
        """
        lists = []
        if parm_name is None:
            for i in cls.param_list:
                if "case" in i:
                    lists.append('node_sort_class.' + i)
        else:
            for item in cls.param_list:
                if parm_name == item:
                    lists.append('node_sort_class.' + item)
        return lists


if __name__ == '__main__':
    print(node_sort_class.get_node_list(parm_name="node_case_002"))
