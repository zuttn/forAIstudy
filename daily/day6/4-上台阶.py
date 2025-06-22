# 作者: 王道 龙哥
# 2025年06月02日10时26分13秒
# xxx@qq.com

def step(n):
    # 结束条件
    if n == 1 or n == 2:
        return n
    return step(n - 1) + step(n - 2)


print([step(n) for n in range(1, 8)])

