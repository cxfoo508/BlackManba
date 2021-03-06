# coding = utf-8
import os

import pytest

from modules.get_control import process_num, project_name, test_case
from modules.helper import file_path

TEMP_DIR = os.path.join(file_path(), "temp")
#123

def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        if i.endswith("py"):
            continue
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
            print(c_path)


del_file(TEMP_DIR)

case_info = (test_case()).split(' ')
process = process_num()
project = project_name()
run_info = [
    '-s',
    "--html=report/" + project + ".html", "--self-contained-html",]


def pytest_run():
    """
    run case info
    """
    if process == "1":
        run_info.extend(case_info)
    else:
        run_info.extend(case_info)
        run_info.append(process)
    return run_info


pytest.main(pytest_run())
