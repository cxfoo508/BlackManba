class node_sort_class:
    node_case_001 = {"sort": ["node_base_class.node_list"], 'params': ['node_data_class.param_001']}
    node_case_002 = {"sort": ["node_base_class.node_list"], 'params': ['node_data_class.param_002']}
    node_case_003 = {"sort": ["node_base_class.create_skills", "node_base_class.node_create"],
                     'params': ['node_data_class.param_003', 'node_data_class.param_004']}
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
                    lists.append('node_sort_class.' + i)
        else:
            for item in cls.param_list:
                if parm_name in item:
                    lists.append('node_sort_class.' + item)
        return lists


if __name__ == '__main__':
    eval('node_sort_class.add(1,2)')
