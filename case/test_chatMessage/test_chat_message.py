from base_case import *
from case.pytest_base import PyBase
from case.test_chatMessage.message_base import ChatMessageCase


class TestCase(PyBase):
    def setup_class(self):
        self.run('app_sort_class.set_up_login')

    def test001_message(self):
        """
        对话
        """
        text = '员工登记'
        data = {
            "msg_body": {
                "text": {"content": text}
            },
            "agent_id": '0'
        }
        con = ChatMessageCase.chat_get_response(data)

    # def test002_get_history(self):
    #     """
    #     获取测试历史数据
    #     """
    #     data = {
    #         "agent_id": '0'
    #     }
    #     con = ChatMessageCase.chat_get_hestory(data)
    #
    # def test003_reset(self):
    #     """
    #     晴空会话
    #     """
    #     con = ChatMessageCase.chat_reset()
    #     assert '{"code":0,"msg":"","data":{}}' in con, con

# if __name__ == '__main__':
    # pytest.main("-s -v test_chat_message.py::TestCass")
