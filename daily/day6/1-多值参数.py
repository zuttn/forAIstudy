# 作者: 王道 龙哥
# 2025年06月02日09时28分38秒
# xxx@qq.com


def demo1(*args, **kwargs):
    print(args)
    # a,b,c,d = args

    print(kwargs)
    # 一个*：把输入的多个数，变成元组
    # 两个*：以key=val的形式输入数）
def demo(num, *args, **kwargs):
    """
    多值参数
    :param num:
    :param args:
    :param kwargs:
    :return:
    """
    print(num)
    print(args)
    print(kwargs)
    print('-' * 50)  # 打印50个-

    # *args就是对元组拆包，**kwargs就是对字典拆包，不能用demo1（args，kwargs），识别不出来
    demo1(*args, **kwargs)


def demo2(num=3):
    pass


# 没有带形参名字，叫positional 参数，带了形参名字的，叫keyword参数
demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)

# 练习keyword参数报错

my_dict = {'num': 4}  # 字典形式的参数，输出的时候用**my_dict拆包，表现为 num=4
demo2(**my_dict)
