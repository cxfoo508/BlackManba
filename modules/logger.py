"""
Create by 吹着风的包子 on 2019-02-14
"""
import logging
import os
import sys

from loguru import logger

from modules.helper import file_path

__author__ = "吹着风的包子"

LOG_DIR = os.path.join(file_path(), "log")
TEMP_DIR = os.path.join(file_path(), "temp")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR, exist_ok=True)


def logger_init():
    logger.remove()  # Remove every possibly added handlers, including the default one

    fmt = "{time:YYYY-MM-DD HH:mm:ss:SSSS}|{level}:{message}"
    file_fmt = "/test-log-{time:YYYY-MM-DD}.log"
    logger.add(
        os.path.join(TEMP_DIR) + "/temp.log",
        format=fmt,
        filter=lambda record: "temp" in record["extra"],
    )
    logger.add(
        os.path.join(TEMP_DIR) + "/opt_temp.log",
        format=fmt,
        filter=lambda record: "opt_temp" in record["extra"],
    )
    logger.add(sys.stderr, format=fmt, level="DEBUG")
    logger.add(
        os.path.join(LOG_DIR) + file_fmt, format=fmt, level="DEBUG", retention="10 days"
    )


logger_init()
log = logger
temp_log = logger.bind(temp=True)
opt_temp_log = logger.bind(opt_temp=True)
