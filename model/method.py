class method_class:
    @classmethod
    def get_node_list(cls, param_list, parm_name=None):
        lists = []
        if parm_name is None:
            for i in param_list:
                if "case" in i:
                    lists.append(i)
        else:
            for item in param_list:
                if parm_name in item:
                    lists.append(item)
        return lists
