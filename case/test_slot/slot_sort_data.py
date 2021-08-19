class slot_sort_class:
    # <editor-fold desc="获取词槽列表">
    slot_case_001 = {
        "sort": ['SlotCaseBase.slot_list'],
        "params": ['slot_data_class.params_case_001_1']

    }
    # </editor-fold>

    # <editor-fold desc="创建词槽">
    slot_case_002 = {
        "sort": ['SlotCaseBase.slot_create', 'SlotCaseBase.slot_update',
                 'SlotCaseBase.slot_del', 'SlotCaseBase.slot_list'],
        "params": ['slot_data_class.params_case_002', 'slot_data_class.params_case_003',
                   'slot_data_class.params_case_004', 'slot_data_class.params_case_001_1'],
    }
    slot_case_002_1 = {
        "sort": ['SlotCaseBase.slot_create', 'SlotCaseBase.slot_create', 'SlotCaseBase.slot_create',
                 'SlotCaseBase.slot_create', 'SlotCaseBase.slot_create'],
        "params": ['slot_data_class.params_case_002_1', 'slot_data_class.params_case_002_2',
                   'slot_data_class.params_case_002_3', 'slot_data_class.params_case_002_4',
                   'slot_data_class.params_case_002_5', ],
    }
    # </editor-fold>

    # <editor-fold desc="更新词槽">
    slot_case_003_1 = {
        "sort": ['SlotCaseBase.slot_create', 'SlotCaseBase.slot_update', 'SlotCaseBase.slot_update',
                 'SlotCaseBase.slot_update',
                 'SlotCaseBase.slot_update', 'SlotCaseBase.slot_update', 'SlotCaseBase.slot_update'],
        "params": ['slot_data_class.params_case_002', 'slot_data_class.params_case_003_1',
                   'slot_data_class.params_case_003_2',
                   'slot_data_class.params_case_003_3', 'slot_data_class.params_case_003_4',
                   'slot_data_class.params_case_003_5', 'slot_data_class.params_case_003_6'],
    }
    # </editor-fold>

    # <editor-fold desc = "删除词槽">
    slot_case_004 = {

        "sort": ['SlotCaseBase.slot_del', 'SlotCaseBase.slot_del'],
        "params": ['slot_data_class.params_case_004_1', 'slot_data_class.params_case_004_2'],
    }
    # </editor-fold>

    # 所有变量名称集合
    param_list = dir()
    print(param_list)

    @classmethod
    def get_slot_list(cls, parm_name=None) -> list:
        """
        返回变量名称集合
        """
        lists = []
        if parm_name is None:
            for i in cls.param_list:
                if "case" in i:
                    lists.append('slot_sort_class.' + i)
        else:
            for item in cls.param_list:
                if parm_name == item:
                    lists.append('slot_sort_class.' + item)
        return lists
