# 作者: 王道 龙哥
# 2025年05月29日10时38分06秒
# xxx@qq.com

def use_cal():
    """
    算术运算符
    :return:
    """
    result = 5 / 2
    print(result)
    result1 = 5 // 2  # 整除
    print(result1)
    print(9 % 2)  # 取模  ===取余
    print(2 ** 3)


def use_compare():
    """
    比较运算符
    :return:
    """
    print(3 > 5)


def use_logic():
    """
    逻辑运算符
    :return:
    """
    print(3 and 5)
    print(3 or 5)
    # 短路运算
    True and print('你可以看到我')
    False and print('你看不到我')

    True or print('你看不到我')
    False or print('你可以看到我')

    if not '':
        print('看得到')


def use_bit():
    """
    位运算
    :return:
    """
    print(5 & 7)
    print(5 | 7)
    print(~5)
    print(5 << 1)  # 乘2
    print(-5 << 1)
    print(5 >> 1)  # 除2
    print(-5 >> 1)  # 减1除2
    print(5 ^ 7)


def use_xor():
    """
    任何数和自身异或值是 0
    任何数和0异或得到的是  自身
    :return:
    """
    my_list = [5, 3, 3, 6, 5]
    result = 0
    for element in my_list:
        result ^= element
    print(result)


# use_cal()
# use_compare()
# use_logic()
# use_bit()
use_xor()