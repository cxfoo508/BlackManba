from log.log_method import MyLog
import os
import json
from base_case import *
from case.test_node.node_sort_data import node_sort_class
from case.test_node.node_base import node_base_class
from case.test_node.node_data import node_data_class
log = MyLog(__name__)


class PyBase:

    def run(self, creat_data):
        """
        执行case
        """
        try:
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
                # 执行func
                res = eval(f'{func}({param[0]})')
                res = json.loads(res)
                # assert
                for s in param[1]:
                    assert eval(s), res
                # 注入项
                for k, v in param[2].items():
                    os.environ[k] = str(eval(v))
                    log.info(f"environ:{k}={eval(v)}")
        except BaseException as e:
            log.info(f"{e}")
