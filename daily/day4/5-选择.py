# 作者: 王道 龙哥
# 2025年05月29日14时38分54秒
# xxx@qq.com

import random
def use_if():
    # 1. 输入用户年龄
    age = int(input("今年多大了？"))

    # 2. 判断是否满 18 岁
    # if 语句以及缩进部分的代码是一个完整的语法块
    if age >= 18:
        print("可以进网吧嗨皮……")
    else:
        print("你还没长大，应该回家写作业！")

    # 3. 思考！- 无论条件是否满足都会执行
    print("这句代码什么时候执行?")


def use_if1():
    holiday_name = "平安夜"

    if holiday_name == "情人节":
        print("买玫瑰")
        print("看电影")
    elif holiday_name == "平安夜":
        print("买苹果")
        print("吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日啊……")


def use_if2():
    # 定义布尔型变量 has_ticket 表示是否有车票
    has_ticket = True

    # 定义整数型变量 knife_length 表示刀的长度，单位：厘米
    knife_length = 20

    # 首先检查是否有车票，如果有，才允许进行 安检
    if has_ticket:
        print("有车票，可以开始安检...")

        # 安检时，需要检查刀的长度，判断是否超过 20 厘米
        # 如果超过 20 厘米，提示刀的长度，不允许上车
        if knife_length >= 20:
            print("不允许携带 %d 厘米长的刀上车" % knife_length)

    # 如果没有车票，不允许进门
    else:
        print("大哥，您要先买票啊")

def use_if3():

    player = int(input("请出拳 石头（1）／剪刀（2）／布（3）："))

    # 电脑 随机 出拳 - 假定电脑永远出石头
    computer =random.randint(1,3)

    # 比较胜负
    # 如果条件判断的内容太长，可以在最外侧的条件增加一对大括号
    # 再在每一个条件之间，使用回车，PyCharm 可以自动增加 8 个空格
    if ((player == 1 and computer == 2) or
            (player == 2 and computer == 3) or
            (player == 3 and computer == 1)):

        print("噢耶！！！电脑弱爆了！！！")
    elif player == computer:
        print("心有灵犀，再来一盘！")
    else:
        print("不行，我要和你决战到天亮！")
# use_if()
# use_if1()
# use_if2()
use_if3()
