# 作者: 王道 龙哥
# 2025年06月03日10时25分39秒
# xxx@qq.com

def demo1():
    num = int(input("请输入数字："))
    return num


def demo2():
    result = demo1()
    print('demo2运行成功')
    return result


if __name__ == '__main__':
    try:
        print(demo2())
        print('主流程里')
    except Exception as e:
        print(e)
