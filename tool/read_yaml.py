import os

import yaml


# 定义一个函数
from config import BASE_PATH


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + 'data' + os.sep + filename
    # 定义空列表 组装测试数据
    arrs = []
    # 获取文件流
    with open(file_path, 'r', encoding="utf-8") as f:
        # 遍历 调用yaml.saft_load(f).values()方法
        # 字典 列表嵌套字典
        # print(yaml.safe_load(f).values())
        for datas in yaml.safe_load(f).values():
            arrs.append(tuple(datas.values()))
    # 返回 结果
    return arrs


if __name__ == '__main__':
    print(read_yaml('mp_login.yaml'))




















