# 作者: 王道 龙哥
# 2025年06月02日09时51分05秒
# xxx@qq.com

import sys
sys.setrecursionlimit(10000)
def sum_numbers(num):
    """
    递归调试要画图
    :param num:
    :return:
    """
    print(num)

    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return

    sum_numbers(num - 1)


sum_numbers(3)
pass


def f(n):
    if n == 1:
        return 1
    return n + f(n - 1)


print(f(2000))
