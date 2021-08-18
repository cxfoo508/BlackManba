class entity_sort_class:
    # <editor-fold desc="set up">
    entity_set_up = {
        "sort": ["auth_login", "creat_app"],
        "params": ["node_data_class.param_005", "node_data_class.param_006"]
    }
    # </editor-fold>

    # <editor-fold desc="创建实体">
    entity_case_001 = {
        "sort": ["create_entity", ],
        "params": ["entity_data_class.parm_entity_001"]
    }
    entity_case_002 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002"]
    }
    # entity_case_003 = {
    #     "sort": ["create_entity"],
    #     "params": ["entity_data_class.parm_entity_003"]
    # }
    entity_case_004 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_004"]
    }
    entity_case_005 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_001_1"]
    }
    entity_case_006 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_001_2"]
    }
    entity_case_007 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_001_3"]
    }
    entity_case_008 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_001_4"]
    }
    entity_case_009 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_001_5"]
    }
    entity_case_010 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_001_6"]
    }
    entity_case_011 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_001_7"]
    }
    entity_case_012 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_001_8"]
    }
    entity_case_013 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002_2"]
    }
    entity_case_014 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002_3"]
    }
    entity_case_015 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002_4"]
    }
    entity_case_016 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002_5"]
    }
    entity_case_017 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002_6"]
    }
    entity_case_018 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002_7"]
    }
    entity_case_020 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002_1"]
    }
    entity_case_021 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_002_2"]
    }
    entity_case_022 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_003_1"]
    }
    entity_case_023 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_003_2"]
    }
    entity_case_024 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_003_3"]
    }
    entity_case_025 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_003_4"]
    }
    entity_case_026 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_003_5"]
    }
    entity_case_027 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_003_6"]
    }
    entity_case_028 = {
        "sort": ["create_entity"],
        "params": ["entity_data_class.parm_entity_003_7"]
    }
    entity_case_028_1 = {
        "sort": ["create_entity", 'get_entity_value_list'],
        "params": ["entity_data_class.parm_entity_001_9", "entity_data_class.parm_entity_008"]
    }
    entity_case_028_2 = {
        "sort": ["create_entity", 'get_entity_value_list'],
        "params": ["entity_data_class.parm_entity_001_10", "entity_data_class.parm_entity_008_5"]
    }
    entity_case_028_3 = {
        "sort": ["create_entity", 'get_entity_value_list'],
        "params": ["entity_data_class.parm_entity_001_11", "entity_data_class.parm_entity_008"]
    }
    entity_case_028_4 = {
        "sort": ["create_entity", 'get_entity_value_list'],
        "params": ["entity_data_class.parm_entity_001_12", "entity_data_class.parm_entity_008_5"]
    }
    # 正则没有实现
    # entity_case_028_5 = {
    #     "sort": ["create_entity", 'get_entity_value_list'],
    #     "params": ["entity_data_class.parm_entity_002_9", "entity_data_class.parm_entity_008"]
    # }
    # entity_case_028_6 = {
    #     "sort": ["create_entity", 'get_entity_value_list'],
    #     "params": ["entity_data_class.parm_entity_002_10", "entity_data_class.parm_entity_008_5"]
    # }
    # entity_case_028_7 = {
    #     "sort": ["create_entity", 'get_entity_value_list'],
    #     "params": ["entity_data_class.parm_entity_002_11", "entity_data_class.parm_entity_008"]
    # }
    # entity_case_028_8 = {
    #     "sort": ["create_entity", 'get_entity_value_list'],
    #     "params": ["entity_data_class.parm_entity_002_12", "entity_data_class.parm_entity_008_5"]
    # }
    # </editor-fold>

    # <editor-fold desc="获取实体类型">
    entity_case_029 = {
        "sort": ['get_entity_type'],
        'params': ['entity_data_class.parm_entity_005']
    }
    # </editor-fold>

    # <editor-fold desc="删除实体">
    entity_case_030 = {
        "sort": ['create_entity', 'del_entity', 'get_entity_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_006',
                   'entity_data_class.parm_entity_007_2']
    }
    entity_case_030_1 = {
        "sort": ['create_entity', 'del_entity'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_006_1',
                   ]
    }
    entity_case_030_2 = {
        "sort": ['create_entity', 'del_entity'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_006_2']
    }
    entity_case_030_3 = {
        "sort": ['create_entity', 'del_entity'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_006_3']
    }
    entity_case_030_4 = {
        "sort": ['create_entity', 'del_entity', 'del_entity','del_entity', 'del_entity', 'del_entity', 'del_entity'],
        'params': ['entity_data_class.parm_entity_001',
                   'entity_data_class.parm_entity_006_4',
                   'entity_data_class.parm_entity_006_5',
                   'entity_data_class.parm_entity_006_6',
                   'entity_data_class.parm_entity_006_7',
                   'entity_data_class.parm_entity_006_8',
                   'entity_data_class.parm_entity_006_9',
                   ]
    }

    # </editor-fold>

    # <editor-fold desc = "获取实体值列表">
    entity_case_031 = {
        "sort": ['create_entity', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001_9', 'entity_data_class.parm_entity_008']
    }
    # </editor-fold>

    # <editor-fold desc = "创建枚举实体值">
    entity_case_032 = {
        "sort": ['create_entity', 'create_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_008_1']
    }
    entity_case_033 = {
        "sort": ['create_entity', 'create_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_1',
                   'entity_data_class.parm_entity_008_2']
    }
    entity_case_034 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value',
                 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_1',
                   'entity_data_class.parm_entity_009_1', 'entity_data_class.parm_entity_009_1',
                   'entity_data_class.parm_entity_008_3']
    }
    entity_case_035 = {
        "sort": ['create_entity', 'create_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_2',
                   'entity_data_class.parm_entity_008_4']
    }
    entity_case_036 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_3',
                   'entity_data_class.parm_entity_009_4', 'entity_data_class.parm_entity_009_5'
                   ]
    }
    entity_case_036_1 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_3',
                   'entity_data_class.parm_entity_009_4', 'entity_data_class.parm_entity_009_5'
                   ]
    }
    entity_case_037 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_6',
                   'entity_data_class.parm_entity_009_7', 'entity_data_class.parm_entity_009_8'
                   ]
    }
    entity_case_038 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_9',
                   'entity_data_class.parm_entity_009_10', 'entity_data_class.parm_entity_009_11']
    }
    entity_case_039 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_12',
                   'entity_data_class.parm_entity_009_13', 'entity_data_class.parm_entity_009_14']
    }
    entity_case_040 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009_15',
                   'entity_data_class.parm_entity_009_16', 'entity_data_class.parm_entity_009_17']
    }
    # </editor-fold>

    # <editor-fold desc = "创建正则实体值">
    entity_case_041 = {
        "sort": ['create_entity', 'create_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_008_1']
    }
    entity_case_042 = {
        "sort": ['create_entity', 'create_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_1',
                   'entity_data_class.parm_entity_008_2']
    }
    entity_case_043 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value',
                 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_1',
                   'entity_data_class.parm_entity_009_1', 'entity_data_class.parm_entity_009_1',
                   'entity_data_class.parm_entity_008_3']
    }
    entity_case_044 = {
        "sort": ['create_entity', 'create_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_2',
                   'entity_data_class.parm_entity_008_4']
    }
    entity_case_045 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_3',
                   'entity_data_class.parm_entity_009_4', 'entity_data_class.parm_entity_009_5'
                   ]
    }
    entity_case_045_1 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_3',
                   'entity_data_class.parm_entity_009_4', 'entity_data_class.parm_entity_009_5'
                   ]
    }
    entity_case_046 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_6',
                   'entity_data_class.parm_entity_009_7', 'entity_data_class.parm_entity_009_8'
                   ]
    }
    entity_case_047 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_9',
                   'entity_data_class.parm_entity_009_10', 'entity_data_class.parm_entity_009_11']
    }
    entity_case_048 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_12',
                   'entity_data_class.parm_entity_009_13', 'entity_data_class.parm_entity_009_14']
    }
    entity_case_049 = {
        "sort": ['create_entity', 'create_entity_value', 'create_entity_value', 'create_entity_value'],
        'params': ['entity_data_class.parm_entity_002', 'entity_data_class.parm_entity_009_15',
                   'entity_data_class.parm_entity_009_16', 'entity_data_class.parm_entity_009_17']
    }
    # </editor-fold>

    # <editor-fold desc = "更新实体">
    entity_case_050 = {
        "sort": ["create_entity", "update_entity", "get_entity_list"],
        "params": ["entity_data_class.parm_entity_001", "entity_data_class.parm_entity_010",
                   "entity_data_class.parm_entity_007_1"]
    }
    entity_case_051 = {
        "sort": ["create_entity", "update_entity", "get_entity_list"],
        "params": ["entity_data_class.parm_entity_001", "entity_data_class.parm_entity_010_1",
                   "entity_data_class.parm_entity_007_1"]
    }
    entity_case_052 = {
        "sort": ["create_entity", "update_entity"],
        "params": ["entity_data_class.parm_entity_001", "entity_data_class.parm_entity_010_2"]
    }
    entity_case_053 = {
        "sort": ["create_entity", "update_entity"],
        "params": ["entity_data_class.parm_entity_001", "entity_data_class.parm_entity_010_3"]
    }
    entity_case_054 = {
        "sort": ["create_entity", "update_entity"],
        "params": ["entity_data_class.parm_entity_001", "entity_data_class.parm_entity_010_4"]
    }
    entity_case_055 = {
        "sort": ["create_entity", "update_entity"],
        "params": ["entity_data_class.parm_entity_001", "entity_data_class.parm_entity_010_5"]
    }
    entity_case_056 = {
        "sort": ["create_entity", "update_entity"],
        "params": ["entity_data_class.parm_entity_001", "entity_data_class.parm_entity_010_6"]
    }
    entity_case_057 = {
        "sort": ["create_entity", "update_entity"],
        "params": ["entity_data_class.parm_entity_001", "entity_data_class.parm_entity_010_7"]
    }
    # </editor-fold>

    # <editor-fold desc = "更新枚举实体值">
    entity_case_057 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011', 'entity_data_class.parm_entity_008_6']
    }
    entity_case_058 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_1', 'entity_data_class.parm_entity_008_6']
    }
    entity_case_059 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_2', 'entity_data_class.parm_entity_008_6']
    }
    entity_case_060 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_3', 'entity_data_class.parm_entity_008_6']
    }
    entity_case_061 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_4', 'entity_data_class.parm_entity_008_6']
    }
    entity_case_062 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_5', 'entity_data_class.parm_entity_008_6']
    }
    entity_case_063 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_6', 'entity_data_class.parm_entity_008_7']
    }
    entity_case_064 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_7', 'entity_data_class.parm_entity_008_7']
    }
    entity_case_065 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_8', 'entity_data_class.parm_entity_008_7']
    }
    entity_case_066 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_9', 'entity_data_class.parm_entity_008_7']
    }
    entity_case_067 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_10', 'entity_data_class.parm_entity_008_7']
    }
    entity_case_068 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_11', 'entity_data_class.parm_entity_008_8']
    }
    entity_case_069 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_12', 'entity_data_class.parm_entity_008_8']
    }
    entity_case_070 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_13', 'entity_data_class.parm_entity_008_8']
    }
    entity_case_071 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_14', 'entity_data_class.parm_entity_008_8']
    }
    entity_case_072 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_15', 'entity_data_class.parm_entity_008_8']
    }
    entity_case_073 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_16', 'entity_data_class.parm_entity_008_8']
    }
    entity_case_074 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_17', 'entity_data_class.parm_entity_008_8']
    }
    entity_case_075 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_18', 'entity_data_class.parm_entity_008_8']
    }
    entity_case_076 = {
        "sort": ['create_entity', 'create_entity_value', 'update_entity_value', 'get_entity_value_list'],
        'params': ['entity_data_class.parm_entity_001', 'entity_data_class.parm_entity_009',
                   'entity_data_class.parm_entity_011_19', 'entity_data_class.parm_entity_008_8']
    }
    # </editor-fold>

    # <editor-fold desc = "获取枚举实体模版">

    entity_case_077 = {
        "sort": ['entity_enum_template'],
        "params": ['entity_data_class.parm_entity_012']
    }
    # </editor-fold>

    # <editor-fold desc = "更新正则实体值">

    # </editor-fold>

    # <editor-fold desc="teardown">
    node_teardown = {
        "sort": ["del_app"],
        "params": ["node_data_class.param_008"]
    }
    # </editor-fold>

    # 所有变量名称集合
    param_list = dir()

    @classmethod
    def get_entity_data_list(cls, parm_name=None) -> list:
        """
        返回变量名称集合
        """
        lists = []
        if parm_name is None:
            for i in cls.param_list:
                if "case" in i:
                    lists.append('entity_sort_class.' + i)
        else:
            for item in cls.param_list:
                if parm_name in item:
                    lists.append('entity_sort_class.' + item)
        return lists
