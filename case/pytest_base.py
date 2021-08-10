# <editor-fold desc = "import">
import pytest
from case.test_app.app_sort_data import app_sort_class
from case.test_app.app_data import app_data_class
from case.test_intents.intents_base import intents_base_class
from case.test_intents.intents_data import intents_data_class
from case.test_intents.inrents_sort_data import intents_sort_class
from case.test_botfallbackconfig.botfallbackconfig_sort_data import botfallbackconfig_sort_class
from case.test_botfallbackconfig.botfallbackconfig_base import botfallbackconfig_base_class
from case.test_botfallbackconfig.botfallbackconfig_data import botfallbackconfig_data_class
from case.test_botresponse.botreponse_sort_data import botresponse_sort_class
from case.test_botresponse.botresponse_base import botresponse_base_class
from case.test_botresponse.botreponse_data import botreponse_data_class
from case.test_channels.channels_sort_data import channels_sort_class
from case.test_channels.channels_data import channels_data_class
from case.test_channels.channels_base import channels_base_class
from case.test_node.node_data import node_data_class
from case.test_node.node_sort_data import node_sort_class
from case.test_node.node_base import node_base_class
from case.test_entity.entity_sort_data import entity_sort_class
from case.test_entity.entity_data import entity_data_class
from case.test_skills.skills_data import skills_data_class
from case.test_skills.skills_sort_data import skills_sort_class
from case.test_skills.case_base_skills import skills_base_class
from case.test_chatMessage.message_base import ChatMessageCase
from base_case import *
# </editor-fold>


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
        log.info(sort_data)
        # 参数包含入参，param_data，注入数据
        param_data = data['params']
        log.info(param_data)
        # 遍历并且执行每个func
        for i in range(len(sort_data)):
            # 判断参数类型
            param_type = type(param_data[i])
            object_x = eval(str(param_data[i]).split('.')[0] + '()')
            param_n = str(param_data[i]).split('.')[1]
            param = eval('object_x.' + param_n)

            func = sort_data[i]
            req = param[0]
            try:
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
                # 执行功能
                if len(param) == 4:
                    for k, v in param[3].items():
                        if k == 'sleep_time':
                            log.info(f'SLEEP_TIME:{v}')
                            time.sleep(v)
            except BaseException as e:
                log.info(f'CODE ERROR:{e}')
                assert 1 == 2, e