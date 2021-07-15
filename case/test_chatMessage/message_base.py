from base_case import *


class ChatMessageCase:
    @classmethod
    def __node_base(cls, url, data):
        """
        slot case
        """
        print(f"send data: {data}")
        res = request_data(url, data)
        con = res.content.decode()
        print(f"res: {con}")
        return con

    @classmethod
    def chat_get_response(cls, data):
        """
        获取回复
        """
        url = '/v1/chat/get_response'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def chat_get_hestory(cls, data):
        """
        获取测试数据
        """
        url = '/v1/chat/get_history'
        con = cls.__node_base(url, data)
        return con

    @classmethod
    def chat_reset(cls):
        """
        reset
        """
        data = {
            'agent_id': 'string'
        }
        url = '/v1/chat/reset'
        con = cls.__node_base(url, data)
        return con
