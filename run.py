# coding = utf-8
import pytest

if __name__ == '__main__':
    run_list = ['-s', '-v', './Test_Case2.py::TestCase::test01_app_creat']
    # run_list = ['-s','-v', './case/test_intents/test_case_intents.py::Testcase']
    pytest.main(run_list)
