class app_sort_class:
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


if __name__ == '__main__':
    eval('node_sort_class.add(1,2)')
