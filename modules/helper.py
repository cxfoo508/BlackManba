"""
Create by 吹着风的包子 on 2018/11/20
"""
import os
import argparse
import logging

from dotenv import load_dotenv, find_dotenv

__author__ = "吹着风的包子"


def file_path():
    """
    路径拼写
    :return:
    """
    root_path = os.path.dirname(os.path.abspath(__file__))
    project_path = root_path[: root_path.rfind("manhattan_v2") + len("manhattan_v2")]
    return project_path


def _choose_environ():
    parser = argparse.ArgumentParser(description="This is a PyMOTW sample program")
    parser.add_argument(
        "-env", type=str, dest="environment", help="the running environment", default=""
    )
    args = parser.parse_args()
    environ = args.environment
    return environ


def init():
    if not _choose_environ():
        environ = os.environ.get("ENV")
    else:
        environ = _choose_environ()  # 获取命令行传过来的环境变量
    filename = ".env" if (not environ or environ == "default") else ".env.%s" % environ
    load_dotenv(find_dotenv(filename="env/%s" % filename), verbose=True)
    print("ENV is `%s`" % os.environ.get("ENV"))
    print("Looking for env file %s" % filename)
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.environ.setdefault("ROOT_DIR", root_dir)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("faker").setLevel(logging.WARNING)
