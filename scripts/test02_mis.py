import pytest
from api.api_mis import ApiMis
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
from tool.tool import Tool
log = GetLog.get_logger()
class TestMis:
    # 1、初始化
    def setup_class(self):
        # 获取ApiMis方法
        self.mis = ApiMis()

    # 2、登录  分析用力得步骤
    @pytest.mark.parametrize("account, password", read_yaml('mis_login.yaml'))   # 列表嵌套元素
    def test01_mis_login(self, account, password):
        # 1、调用登陆接口
        r = self.mis.api_mis_login(account, password)
        # 2、提取token   并进行hearder的组装  在common_token()方法中实现的
        Tool.common_token(r)
        # token = r.json().get('data').get('token')       # 因其经常被使用，故抽取出来，封装到工具类中
        try:
            # 3、断言  也在common_assert中封装好
            Tool.common_assert(r)
        except Exception as e:
            # 1、日志
            log.error(e)
            # 2、抛异常
            raise

    # 3、查询
    def test02_mis_search(self):
        # 1、调用查询接口
        r = self.mis.api_mis_search()
        try:
            # 2、断言
            Tool.common_assert(r, status_code=200)    # 响应状态码变了，要传参，且为int型
        except Exception as e:
            # 1、日志
            log.error(e)
            # 2、抛异常
            raise

    # 4、审核
    def test03_mis_audit(self):
        # 1、调用审核接口
        r = self.mis.api_mis_audit()
        try:
            # 2、断言
            Tool.common_assert(r)      # 状态码未改变，无需传参
        except Exception as e:
            # 1、日志
            log.error(e)
            # 2、抛异常
            raise