import requests

import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiMp:
    # 1、初始化文件
    def __init__(self):
        """用来组合参数"""
        # 1、定义登陆接口的url
        self.url_login = api.host + "/mp/v1_0/authorizations"
        log.info('正在初始化自媒体登录url: {}'.format(self.url_login))
        # 2、发布文章url
        self.url_article = api.host + "/mp/v1_0/articles"
        log.info('正在初始化自媒体发布url: {}'.format(self.url_article))

    # 2、登陆接口
    def api_mp_login(self, mobile, code):
        """
        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象，响应数据、状态码等
        """
        # 1、定义登陆的请求数据
        data = {'mobile': mobile, 'code': code}
        log.info('正在调用自媒体登录接口，请求数据: {}'.format(data))
        # 2、调用post请求方法  返回相应对象（包括：有断言需要的数据，如状态码等）
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3、发布文章接口
    def api_mp_article(self, title, content, channel_id):
        """
        :param title: 文章标题
        :param content: 文章内容
        :param channel_id: 频道id
        :param cover: 封面 0：为自动
        :return: 返回响应对象
        """
        # 1、定义请求数据
        data = {'title': title, 'content': content, 'channel_id': channel_id, 'cover': {'type': 0, 'images': []}}
        log.info('正在调用自媒体发布文章接口，请求数据: {}'.format(data))
        # 2、调用post请求方法
        return requests.post(url=self.url_article, json=data, headers=api.headers)
