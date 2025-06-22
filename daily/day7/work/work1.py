"""
1、通过try进行异常捕捉，确保输入的内容一定是一个整型数，
然后判断该整型数是否是对称数，12321就是对称数，
123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常

1
2 1*10 + 2 = 12
3 12*10 + 3 = 123
"""



def isDuiCheng():
    try:
        num = int(input("输入一个整数"))
    except:
        print("输入的不是整数")
    flag = num
    div = 0
    while flag!=0:
        div = div*10 + flag%10
        # flag = flag/10
        flag = int(flag/10)
    if div==num:
        print(f'{num}是对称数')
    else:
        raise Exception("不是对称数")


try:
    isDuiCheng()
except Exception as e:
    print(e)