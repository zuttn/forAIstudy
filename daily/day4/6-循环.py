# 作者: 王道 龙哥
# 2025年05月29日14时57分26秒
# xxx@qq.com

def use_while():
    # 1. 定义重复次数计数器
    i = 1
    total = 0
    # 2. 使用 while 判断条件
    while i <= 100:
        if i % 2 == 0:
            total += i
        i += 1

    print(f'total={total}')


def use_break():
    # 1. 定义重复次数计数器
    i = 1
    total = 0
    # 2. 使用 while 判断条件
    while i <= 100:
        if total > 2000:
            break
        total += i
        i += 1

    print(f'total={total},i={i}')  # 64没有加到2016中


def use_continue():
    # 1. 定义重复次数计数器
    i = 1
    total = 0
    # 2. 使用 while 判断条件
    while i <= 100:
        if i % 2 == 1:  # 如果是奇数，continue
            i += 1  # continue之前确保自增
            continue
        total += i
        i += 1

    print(f'total={total}')


def use_two_level_while():
    row = 1

    while row <= 9:

        # 假设 python 没有提供字符串 * 操作
        # 在循环内部，再增加一个循环，实现每一行的 星星 打印
        col = 1

        while col <= row:
            print(f'{col}*{row}={col * row}', end='\t')
            col += 1
        # 每一行星号输出完成后，再增加一个换行
        print()

        row += 1


def use_for():
    my_list = [4, 5, 6]
    for i in my_list:
        print(i, end=' ')
    print()
    print('-' * 50)
    i = 0
    while i < len(my_list):
        print(my_list[i], end=' ')
        i += 1
    print()


def use_for_else():
    for i in range(10):
        if i == 15:
            break  # 不是从break出来的，就会打印没找到
    else:
        print('没找到')
    print()


# use_while()
# use_break()
# use_continue()
# use_two_level_while()
# use_for()
use_for_else()
