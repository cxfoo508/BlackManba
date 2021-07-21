from modules.logger import log
import os
import json
from base_case import *
from case.test_node.node_sort_data import node_sort_class
from case.test_node.node_base import node_base_class
from case.test_node.node_data import node_data_class
from case.test_app.app_sort_data import app_sort_class
from case.test_app.app_data import app_data_class

class PyBase:

    def run(self, creat_data):
        """
        执行case
        """
        data = eval(creat_data)
        # 要执行的func和执行顺序
        sort_data = data['sort']
        # 参数包含入参，断言，注入数据
        param_data = data['params']
        # 遍历并且执行每个func
        for i in range(len(sort_data)):
            object_x = eval(str(param_data[i]).split('.')[0] + '()')
            param_n = str(param_data[i]).split('.')[1]
            param = eval('object_x.' + param_n)
            func = sort_data[i]
            req = param[0]
            # 执行func
            res = eval(f'{func}({req})')
            res = json.loads(res)
            # assert
            for s in param[1]:
                log.info(f'ASSERT:{s},ANSWER:{eval(s)}')
                assert eval(s), res
            # res注入项
            for k, v in param[2].items():
                os.environ[k] = str(eval(v))
                log.info(f"ENVIRON res:{k}={eval(v)}")