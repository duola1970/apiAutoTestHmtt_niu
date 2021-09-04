import pytest

import api
from api.api_mp import ApiMp
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
from tool.tool import Tool

log = GetLog.get_logger()


# 统一入口类
class TestMp:
    # 1、初始化
    def setup_class(self):
        # 1、获取 ApiMp对象
        self.mp = ApiMp()

    # 2、登陆接口测试方法    无需结束，因为不需要关闭对象
    @pytest.mark.parametrize("mobile, code", read_yaml('mp_login.yaml'))
    def test01_mp_login(self, mobile, code):
        # 利用ApiMp对象 调用登录接口
        r = self.mp.api_mp_login(mobile, code)
        # 打印输出结果    json()解析数据
        print('登录的结果为：', r.json())

        try:
            # 公共方法 提取token
            Tool.common_token(r)

            # 公共方法 断言
            Tool.common_assert(r)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 3、发布文章接口测试方法
    def test01_mp_article(self, title=api.title, content=api.content, channel_id=api.channel_id):
        # 1、调用发布文章接口   3方法的实现依赖于2，故2、3要一起执行
        r = self.mp.api_mp_article(title, content, channel_id)
        # 2、提取id     审核文章时要使用，所以放入公共参数中
        api.article_id = r.json().get('data').get('id')
        # 3、调用公共方法 断言
        try:
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise
