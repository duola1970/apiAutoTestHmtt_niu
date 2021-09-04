# 导包
import logging.handlers
import os
# 新建 类
from config import BASE_PATH


class GetLog:
    # 新建 一个日志器变量
    __logger = None
    # 新建获取日志器的方法 -- 保证自始至终获取同一个对象及通过类名.快速获取到类的方法 -- 类方法
    @classmethod
    def get_logger(cls):
        # 判断日志器是否为空
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 修改默认级别  默认警告级别，需要修改为信息级别
            cls.__logger.setLevel(logging.INFO)
            log_path = BASE_PATH + os.sep + 'log' + os.sep + 'hmtt.log'
            # 获取处理器  有控制台，有文件  时间一天一夜 备份数量3  编码格式utf-8
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path, when='midnight', interval=1, backupCount=3, encoding='utf-8')
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt=fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)

        # 返回日志器
        return cls.__logger


if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info('测试信息级别日志')
    log.error('测试错误级别')

    # 日志级别debug、info、warning、error、critical
    # log.debug("调试信息")
    # log.info("普通信息")
    # log.warning("警告信息")
    # log.error("错误信息")
    # log.critical("严重错误信息")

