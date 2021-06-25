# coding = utf-8
import os

import requests

# URL =  "http://172.17.202.22:5015"
URL = "http://39.105.24.211:8080"


# URL = "http://59.110.157.33:5697"


def request_data(url, data=None, check_data=None):
    """
    request
    """
    send_url = url
    token = os.environ.get("token")
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    print(f"{URL}{send_url}")
    request = requests.post(url=f"{URL}{send_url}", json=data, headers=header)
    return request


def creat_app(data):
    """
    创建机器人
    """
    url = "/v1/agent/create"
    res = request_data(url, data)
    return res


def del_app(data):
    """
    删除机器人
    """
    url = "/v1/agent/del"
    con = request_data(url, data)
    return con


def getlist_app(data):
    """
    获取列表机器人
    """
    url = "/v1/agent/list"
    con = request_data(url, data)
    return con


def update_app(data):
    """
    机器人更新
    """
    url = "/v1/agent/update"
    con = request_data(url, data)
    return con


def auth_systemInfo():
    """
    获取系统信息
    """
    url = "/v1/auth/systemInfo"
    res = request_data(url)
    return res


def auth_login(data):
    """
    登陆
    """
    url = "/v1/auth/login"
    res = request_data(url, data)
    return res


def users_userInfo(data=None):
    """
    获取用户信息
    """
    url = '/v1/users/userinfo'
    res = request_data(url, data)
    return res

# 兜底策略

def get_config(data=None):
    """
    获取机器人兜底策略
    """
    url = '/v1/fallback_config/get_config'
    res = request_data(url, data)
    return  res

def update_config(data=None):
    """
    修改机器人兜底策略
    """
    url = '/v1/fallback_config/update_config'
    res = request_data(url, data)
    return res

# 回复
def response_type(data=None):
    """
    获取对话机器人回复类型列表
    """
    url = '/v1/response/response_type'
    res = request_data(url, data)
    return res

def responses_type(data=None):
    """
    获取对话机器人回复集类型列表
    """
    url = '/v1/response/responses_type'
    res = request_data(url, data)
    return res


def responses_mode(data=None):
    """
    获取对话机器人回复集模式列表
    """
    url = '/v1/response/responses_mode'
    res = request_data(url, data)
    return res


def custom_action(data=None):
    """
    获取系统内置自定义动作回复
    """
    url = '/v1/response/custom_action'
    res = request_data(url, data)
    return res


def get_responses(data=None):
    """
    根据ID获取回复集
    """
    url = '/v1/response/get_responses'
    res = request_data(url, data)
    return res


def update_responses(data=None):
    """
    新增或修改回复集
    """
    url = '/v1/response/update_responses'
    res = request_data(url, data)
    return res


def delete_responses(data=None):
    """
    删除回复集
    """
    url = '/v1/response/delete_responses'
    res = request_data(url, data)
    return res

# 实体
def create_entity(data=None):
    """
    创建实体
    """
    url = '/v1/entity/create'
    res = request_data(url, data)
    return res


def create_entity_value(data=None):
    """
    创建实体值
    """
    url = '/v1/entity/value/create'
    res = request_data(url, data)
    return res


def update_entity(data=None):
    """
    更新实体
    """
    url = '/v1/entity/update'
    res = request_data(url, data)
    return res


def update_entity_value(data=None):
    """
    更新实体值
    """
    url = '/v1/entity/value/update'
    res = request_data(url, data)
    return res


def del_entity(data=None):
    """
    删除实体
    """
    url = '/v1/entity/del'
    res = request_data(url, data)
    return res


def del_entity_value(data=None):
    """
    删除实体值
    """
    url = '/v1/entity/value/del'
    res = request_data(url, data)
    return res


def get_entity_list(data=None):
    """
    获取列表
    """
    url = '/v1/entity/list'
    res = request_data(url, data)
    return res


def get_entity_type(data=None):
    """
    获取实体类型列表
    """
    url = '/v1/entity/type'
    res = request_data(url, data)
    return res


def get_entity_value_list(data=None):
    """
    获取实体值列表
    """
    url = '/v1/entity/value/list'
    res = request_data(url, data)
    return res


# ###intent###
def create_intent(data=None):
    """
    创建意图
    """
    url = '/v1/intents/create'
    res = request_data(url, data)
    return res

def get_intents_list(data=None):
    """
    获取意图列表
    """
    url = '/v1/intents/list'
    res = request_data(url, data)
    return res

def edit_intents(data=None):
    """
    编辑意图
    """
    url = '/v1/intents/edit'
    res = request_data(url, data)
    return res

def delete_intents(data=None):
    """
    删除意图
    """
    url = '/v1/intents/delete'
    res = request_data(url, data)
    return res

def intents_detail(data=None):
    """
    意图详情
    """
    url = '/v1/intents/detail'
    res = request_data(url, data)
    return res

# ###skills###
def create_skills(data=None):
    """
    创建技能
    """
    url = '/v1/skills/create'
    res = request_data(url, data)
    return res


def get_skills_list(data=None):
    """
    获取技能列表
    """
    url = '/v1/skills/list'
    res = request_data(url, data)
    return res


def get_skills_detail(data=None):
    """
    获取单个技能设置信息
    """
    print(f"data:{data}")
    url = '/v1/skills/detail'
    res = request_data(url, data)
    res = res.content.decode()
    print(f"res:{res}")
    return res


def get_skills_set_detail(data=None):
    """
    获取单个技能信息
    """
    print(f"data:{data}")
    url = '/v1/skills/detail_set_skill'
    res = request_data(url, data)
    res = res.content.decode()
    print(f"res:{res}")
    return res


def set_skill(data=None):
    """
    设置技能
    """
    print(f"data:{data}")
    url = '/v1/skills/set_skill'
    res = request_data(url, data)
    con = res.content.decode()
    print(f"res:{con}")
    return con


def del_skill(data=None):
    """
    删除技能
    """
    print(f"data:{data}")
    url = '/v1/skills/delete'
    res = request_data(url, data)
    con = res.content.decode()
    print(f"res:{con}")
    return con


def edit_skills(data=None):
    """
    编辑技能
    """
    print(f'data:{data}')
    url = '/v1/skills/edit'
    res = request_data(url, data)
    con = res.content.decode()
    print(f"res:{con}")
    return con


if __name__ == "__main__":
    pass
