class app_sort_class:
    # set_up
    set_up_login = {"sort": ["auth_login"], "params": ['app_data_class.param_login']}

    # <editor-fold desc="创建app">
    # 创建app call test
    app_case_001 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_001', 'app_data_class.param_019']}
    app_case_002 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_002', 'app_data_class.param_019']}
    app_case_003 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_003', 'app_data_class.param_019']}
    app_case_004 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_004', 'app_data_class.param_019']}
    app_case_005 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_005', 'app_data_class.param_019']}
    app_case_006 = {"sort": ["creat_app"],
                    'params': ['app_data_class.param_006']}
    app_case_007 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_006_1', 'app_data_class.param_019']}
    app_case_008 = {"sort": ["creat_app"],
                    'params': ['app_data_class.param_006_2']}
    app_case_009 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_008', 'app_data_class.param_019']}
    app_case_010 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_009', 'app_data_class.param_019']}
    app_case_011 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_010', 'app_data_class.param_019']}
    app_case_011_1 = {"sort": ["creat_app"],
                      'params': ['app_data_class.param_010_1']}
    app_case_012 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_011', 'app_data_class.param_019']}
    app_case_013 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_012', 'app_data_class.param_019']}
    app_case_014 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_013', 'app_data_class.param_019']}
    app_case_015 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_014', 'app_data_class.param_019']}
    app_case_016 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_015', 'app_data_class.param_019']}
    app_case_017 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_016', 'app_data_class.param_019']}
    app_case_018 = {"sort": ["creat_app", "del_app"],
                    'params': ['app_data_class.param_017', 'app_data_class.param_019']}
    # </editor-fold>

    # <editor-fold desc="更新机器人">
    """
    更新机器人
    """
    app_case_019 = {"sort": ["creat_app", "update_app", 'getlist_app', "del_app"],
                    'params': ['app_data_class.param_001', 'app_data_class.up_parm_001',
                               'app_data_class.get_app_lit_001', 'app_data_class.param_019']}
    app_case_019_1 = {"sort": ["creat_app", "update_app", "del_app"],
                    'params': ['app_data_class.param_001', 'app_data_class.up_parm_002',
                               'app_data_class.param_019']}
    app_case_019_2 = {"sort": ["creat_app", "update_app", "del_app"],
                      'params': ['app_data_class.param_001', 'app_data_class.up_parm_003',
                                 'app_data_class.param_019']}
    app_case_019_3 = {"sort": ["creat_app", "update_app", "del_app"],
                      'params': ['app_data_class.param_001', 'app_data_class.up_parm_004',
                                 'app_data_class.param_019']}
    app_case_019_4 = {"sort": ["creat_app", "update_app",'getlist_app', "del_app"],
                      'params': ['app_data_class.param_001', 'app_data_class.up_parm_005',
                                 'app_data_class.get_app_lit_001','app_data_class.param_019']}
    app_case_019_5 = {"sort": ["creat_app", "update_app", "del_app"],
                      'params': ['app_data_class.param_001', 'app_data_class.up_parm_006',
                                 'app_data_class.param_019']}
    app_case_019_6 = {"sort": ["creat_app", "update_app", "getlist_app","del_app"],
                      'params': ['app_data_class.param_001', 'app_data_class.up_parm_007',
                                 "app_data_class.get_app_lit_001",
                                 'app_data_class.param_019']}
    app_case_019_7 = {"sort": ["creat_app", "update_app",  "del_app"],
                      'params': ['app_data_class.param_001',
                                 'app_data_class.up_parm_008',
                                 'app_data_class.param_019']}
    app_case_019_8 = {"sort": ["creat_app", "update_app", "getlist_app", "del_app"],
                      'params': ['app_data_class.param_001', 'app_data_class.up_parm_009',
                                 "app_data_class.get_app_lit_001",
                                 'app_data_class.param_019']}
    app_case_019_9 = {"sort": ["creat_app", "update_app", "getlist_app", "del_app"],
                      'params': ['app_data_class.param_001', 'app_data_class.up_parm_010',
                                 "app_data_class.get_app_lit_001",
                                 'app_data_class.param_019']}
    # </editor-fold>

    # <editor-fold desc="机器人列表">
    """
    获取机器人列表
    """
    app_case_020 = {"sort": ["creat_app", "getlist_app", "del_app"],
                    'params': ['app_data_class.param_001', 'app_data_class.get_app_lit_001',
                               'app_data_class.param_019']}
    app_case_021 = {"sort": ["getlist_app"],
                    'params': ['app_data_class.get_app_lit_002']}
    app_case_022 = {"sort": ["getlist_app"],
                    'params': ['app_data_class.get_app_lit_003']}
    app_case_023 = {"sort": ["getlist_app"],
                    'params': ['app_data_class.get_app_lit_004']}
    app_case_024 = {"sort": ["getlist_app"],
                    'params': ['app_data_class.get_app_lit_005']}
    app_case_025 = {"sort": ["getlist_app"],
                    'params': ['app_data_class.get_app_lit_006']}
    app_case_026 = {"sort": ["getlist_app"],
                    'params': ['app_data_class.get_app_lit_007']}
    app_case_027 = {"sort": ["getlist_app"],
                    'params': ['app_data_class.get_app_lit_008']}
    # </editor-fold>

    # 所有变量名称集合
    param_list = dir()

    @classmethod
    def get_node_list(cls, parm_name=None) -> list:
        """
        返回变量名称集合
        """
        lists = []
        if parm_name is None:
            for i in cls.param_list:
                if "case" in i:
                    lists.append('app_sort_class.' + i)
        else:
            for item in cls.param_list:
                if parm_name in item:
                    lists.append('app_sort_class.' + item)
        return lists


