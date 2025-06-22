# 作者: 王道 龙哥
# 2025年06月03日09时58分23秒
# xxx@qq.com

import my_module
import traceback
def test1():
    try:
        my_module.test()
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
        print(e.__traceback__.tb_lineno)                        # 发生异常所在的行数


def test2():
    try:
        my_module.test()
    except Exception as e:
        print(f"Exception: {e}")

        # 获取完整 traceback 链
        tb = e.__traceback__

        # 找到最内层的 traceback（也就是异常真正发生的地方）
        while tb.tb_next:
            tb = tb.tb_next

        # 输出异常发生的文件和行号
        print("异常发生的文件:", tb.tb_frame.f_globals["__file__"])
        print("异常发生的行号:", tb.tb_lineno)

        # 如果你还想打印堆栈信息，也可以加：
        print("\n完整堆栈信息：")
        traceback.print_exception(type(e), e, e.__traceback__)

test2()
print('是否到这里')