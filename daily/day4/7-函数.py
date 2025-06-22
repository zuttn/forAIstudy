# 作者: 王道 龙哥
# 2025年05月29日15时31分27秒
# xxx@qq.com

name = "小明"


# 解释器知道这里定义了一个函数
def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)
# 只有在调用函数时，之前定义的函数才会被执行
# 函数执行完成之后，会重新回到之前的程序中，继续执行后续的代码
say_hello()

print(name)

say_hello()

print('-' * 50)


def sum_2_num(num1, num2):
    """
    传递两个参数，无返回值
    :param num1:
    :param num2:
    :return:
    """
    result = num1 + num2

    print("%d + %d = %d" % (num1, num2, result))


sum_2_num(50, 20)


def sum_2_num_return(num1, num2):
    """对两个数字的求和"""

    return num1 + num2


# 调用函数，并使用 result 变量接收计算结果
result = sum_2_num_return(10, 20)

print("计算结果是 %d" % result)
