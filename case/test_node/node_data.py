import os


class node_data_class:
    # agent_name
    def __init__(self):
        self.param_001 = [{
            "agent_id": os.environ.get("agent_id"),
            "search_opt": {
                "node_id_list": [
                    "string"
                ]
            },
            "is_details_required": 0,
            "page_no": 1,
            "number_per_page": 0
        }, '{"code":0,"msg":"","data":{"agent_id"']
