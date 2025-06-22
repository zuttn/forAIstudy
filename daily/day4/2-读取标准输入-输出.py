# 作者: 王道 龙哥
# 2025年05月29日09时45分33秒
# xxx@qq.com

def use_input():
    a=input('请输入:')
    # print(int(a)+5)  #ValueError,给了不对的值类型

    # print(float(a))
    print(int(float(a))) #小数字符串要变为整数，要这样


def use_print():
    name='小明'
    student_no=1001
    price=3.5
    weight,money=1.4,2.6
    scale=0.12
    print("我的名字叫 %s，请多多关照！" % name)
    print("我的学号是 %06d" % student_no)
    print("苹果单价 %.2f 元／斤，购买 %.02f 斤，需要支付 %.02f 元" % (price, weight, money))
    print("数据比例是 %.02f%%" % (scale * 100))
    print('-'*100)
    print(f"我的名字叫 {name}，请多多关照！") #大括号
    print(f"苹果单价 {price:.2f}元／斤 购买 {weight} 斤")

# use_input()

use_print()