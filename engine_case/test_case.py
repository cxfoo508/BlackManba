# coding = utf-8
import json

import pytest

from engine_case.engine_base_case import *

dialog_data_1 = ["0_/restart", "1_奶粉结块调查", "2_刚开封", "3_包装完好"]  # 对话树
dialog_data_2 = ["0_/restart", "1_奶粉结块调查", "2_刚开封", "3_打开前好像有点漏气"]
dialog_data_3 = ["0_/restart", "1_奶粉结块调查", "2_使用一段时间后", "3_在保质期"]
dialog_data_4 = ["0_/restart", "1_奶粉结块调查", "2_使用一段时间后", "3_过保质期了"]
dialog_data_5 = ["0_/restart", "1_奶粉结块调查", "2_dfgdfgdfg", "3_sdfsdfsdfsdf", "4_sdafasdfadf"]
form_data = ["0_/restart", "1_官网申请试用", "2_小明", "3_COVID-19会引发哪些症状", "4_来也科技", "5_我来自北京", "6_334433@qq.com",
             "7_可以"]  # form
form_data_1 = ["0_/restart", "1_官网申请试用", "2_小王", "3_来也科技", "4_2012-11-11", "5_帝都", "7_334433@qq.com", "10_可以"]  # form
form_data_2 = ["0_/restart", "1_官网申请试用", "2_小王", "3_来也科技", "4_2012-11-11", "5_中国", "6_北京", "7_北京", "8_海淀区",
               "9_13911154620", "10_132201198905082931", "11_334433@qq.com", "12_可以"]


# wulai_data = ["1_restart"]

# def get_data():
# return


@pytest.fixture(params=form_data_2)
def send_data(request):
    return request.param


def test_002_query(send_data):
    """
       对话树-query
       """
    # print(send_data)
    data = send_data.split("_")
    print(data[1])
    res = query(data[1])
    print(res.status_code, res.content.decode())
    res_con = json.loads(res.content.decode())
