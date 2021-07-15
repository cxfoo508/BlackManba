import datetime
import logging
import sys


class MyLog:

    def __init__(self, logname='mulogger'):
        file_name = datetime.datetime.now().strftime('%Y%m%d.log')
        path = '/Users/chengxinfei/PycharmProjects/MyCode/log'
        self.my_log = logging.getLogger(logname)
        self.my_log.setLevel(logging.INFO)
        rf_handler = logging.StreamHandler(sys.stderr)  # 默认是sys.stderr
        rf_handler.setLevel(logging.DEBUG)
        rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))

        f_handler = logging.FileHandler(f'{path}/{file_name}')
        f_handler.setLevel(logging.INFO)
        f_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

        self.my_log.addHandler(rf_handler)
        self.my_log.addHandler(f_handler)

    def debug(self, data):
        self.my_log.debug(data)

    def info(self, data):
        self.my_log.info(data)

    def error(self, data):
        self.my_log.error(data)

    def warning(self, data):
        self.my_log.warning(data)

    def critical(self, data):
        self.my_log.critical(data)


if __name__ == '__main__':
    log = MyLog()
    log.info(112233445555656)
