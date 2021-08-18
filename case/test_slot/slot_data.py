from data_method import *


class slot_data_class:
    def __init__(self):
        # <editor-fold desc = "获取词槽列表">
        self.params_case_001 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "skill_id_list": [
                    os.environ.get('skill_id')
                ],
                "slot_id_list": [
                    os.environ.get('slot_id')
                ],
                "slot_name": os.environ.get('slot_name'),
                "is_from_text": 0,
                "is_entity_fill": 0,
                "is_intent_fill": 0,
                "is_sentence_fill": 0,
                "page_no": 1,
                "number_per_page": 5
            }, [], {}
        ]
        self.params_case_001_1 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "page_no": 1,
                "number_per_page": 5
            }, ['res["code"]==0'], {}
        ]
        # </editor-fold>

        # <editor-fold desc = "创建词槽">
        self.params_case_002 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==0', 'res["data"]["slot_id"]!=None'], {'slot_id': 'res["data"]["slot_id"]'}

        ]
        self.params_case_002_1 = [
            {   # 必填项
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_002_2 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "is_from_text": 0,
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="slot_name"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_002_3 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="is_from_text"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_002_4 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="is_list"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_002_5 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_list": 0,
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="is_compound"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]

        # </editor-fold>

        # <editor-fold desc = "更新词槽">
        self.params_case_003 = [
            {
                "slot_id": os.environ.get('slot_id'),
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==0'], {}

        ]
        self.params_case_003_1 = [
            {
                # 必填项
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="slot_id"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_003_2 = [
            {
                # 必填项
                "slot_id": os.environ.get('slot_id'),
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_003_3 = [
            {
                # 必填项
                "slot_id": os.environ.get('slot_id'),
                "agent_id": os.environ.get('agent_id'),
                "is_from_text": 0,
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="slot_name"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_003_4 = [
            {
                # 必填项
                "slot_id": os.environ.get('slot_id'),
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_list": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="is_from_text"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_003_5 = [
            {
                # 必填项
                "slot_id": os.environ.get('slot_id'),
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_compound": 0
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="is_list"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_003_6 = [
            {
                # 必填项
                "slot_id": os.environ.get('slot_id'),
                "agent_id": os.environ.get('agent_id'),
                "slot_name": get_str(4),
                "is_from_text": 0,
                "is_list": 0,
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="is_compound"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        # </editor-fold>

        # <editor-fold desc = "删除词槽">
        self.params_case_004 = [
            {
                "agent_id": os.environ.get('agent_id'),
                "slot_id_list": [
                    os.environ.get('slot_id')
                ]
            }, ['res["code"]==0'], {}

        ]
        self.params_case_004_1 = [
            {
                "slot_id_list": [
                    os.environ.get('slot_id')
                ]
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="agent_id"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        self.params_case_004_2 = [
            {
                "agent_id": os.environ.get('agent_id'),
            }, ['res["code"]==10009',
                'res["msg"]=="接口参数验证出错"', 'res["data"][0]["loc"][1]=="slot_id_list"',
                'res["data"][0]["msg"]=="field required"'], {}

        ]
        # </editor-fold>
