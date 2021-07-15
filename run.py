# coding = utf-8
import pytest
if __name__ == '__main__':


    run_list = ['-s', '-v', '--html=report.html', '--capture=sys', './case']
    pytest.main(run_list)
