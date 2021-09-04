"""公共变量"""
# 1、请求域名
from tool.read_yaml import read_yaml

host = 'http://ttapi.research.itcast.cn'
# 2、请求信息头
headers = {"Content-Type": "application/json"}
# 3、文章id
article_id = None

# 接受发布文章读取的数据
data = read_yaml('mp_article.yaml')
# 文章标题
title = data[0][0]
# 文章内容
content = data[0][1]
# 文章所属频道id
channel_id = data[0][2]
# 文章所属频道
channel = data[0][3]

