import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class Tool:
    # 1、提取token
    @classmethod
    def common_token(cls, response):
        # 因为r在data下面是一个json串   response.text  <str>
        # 提取token
        token = response.json().get('data').get('token')
        # 追加请求信息头
        api.headers['Authorization'] = "Bearer " + token
        log.info('正在提取token，提取后的header值为: {}'.format(api.headers))
        # print('添加token后的headers为：', api.headers)

    # 2、断言
    @classmethod
    def common_assert(cls, response, status_code=201):
        log.info('正在正在调用公共断言方法！')
        # 断言状态码   状态码是int型
        assert status_code == response.status_code
        # 断言响应信息
        assert 'OK' == response.json().get('message')