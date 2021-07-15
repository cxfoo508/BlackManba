# coding = utf-8
import pytest

if __name__ == '__main__':
<<<<<<< HEAD
    run_list = ['-s', '-v', './Test_Case2.py::TestCase::test01_app_creat']
    # run_list = ['-s','-v', './case/test_intents/test_case_intents.py::Testcase']
=======
    run_list = ['-s', '-v', '--html=report.html', '--capture=sys', './case']
>>>>>>> d23da11 (fix:增加日志，优化框架)
    pytest.main(run_list)
