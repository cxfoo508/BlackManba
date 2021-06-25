# coding = utf-8
import pytest

if __name__ == '__main__':
    # run_list = ['-s', './Test_Case2.py::test01_app_creat', './Test_Case2.py::test02_app_update',
    #              './Test_Case2.py::test03_app_del']
    # run_list = ['-s', './Test_Case2.py::TestCase::test_auth_systemInfo']
    run_list = ['-s','-v', './case/test_intents/test_case_intents.py::Testcase']
    pytest.main(run_list)
