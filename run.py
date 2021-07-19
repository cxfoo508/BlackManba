# coding = utf-8
import pytest
import os
import pytest
from modules.helper import file_path
from modules.get_control import test_case, process_num, project_name


TEMP_DIR = os.path.join(file_path(), "temp")


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

case_info = test_case()
process = process_num()
project = project_name()


def pytest_run():
    if process == "1":
        run_info = [
            case_info,
            "--html=report/" + project + ".html",
            "--self-contained-html",
            "-s",
            "-v",
        ]
    else:
        run_info = [
            case_info,
            "-n",
            process,
            "--html=report/" + project + ".html",
            "--self-contained-html",
            "-s",
            "-v",
        ]
    return run_info

# print(pytest_run())
pytest.main(pytest_run())

