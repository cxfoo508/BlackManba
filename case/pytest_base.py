import pytest
from case.test_app.app_sort_data import app_sort_class
from case.test_app.app_data import app_data_class
from case.test_node.node_data import node_data_class
from case.test_node.node_sort_data import node_sort_class
from case.test_entity.entity_sort_data import entity_sort_class
from case.test_entity.entity_data import entity_data_class
from base_case import *


class PyBase:
    @staticmethod
    def run(creat_data):
        """
        执行case
        """
        log.info(f'TEST NAME: ============{creat_data}============')
        data = eval(creat_data)
        # 要执行的func和执行顺序
        sort_data = data['sort']
        # 参数包含入参，断言，注入数据
        param_data = data['params']
        # 遍历并且执行每个func
        for i in range(len(sort_data)):
            # 判断参数类型
            param_type = type(param_data[i])
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
                # 判断是否错误终止：
                assert_type = os.environ.get('assert_type')
                if assert_type == 'False':
                    assert eval(s), res
                else:
                    pytest.assume(eval(s), res)
            # res注入项
            for k, v in param[2].items():
                os.environ[k] = str(eval(v))
                log.info(f"ENVIRON {k}={v}:{k}={eval(v)}")
