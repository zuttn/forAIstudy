# 作者: 王道 龙哥
# 2025年06月03日09时48分53秒
# xxx@qq.com


try:
    # 提示用户输入一个数字
    num = int(input("请输入数字："))#发生异常后，下面的代码不会得到执行，会直接跳转到expect
    result=8/num
    print(result)
except ValueError:
    print('请输入数字')
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(f'未知异常{e}')
else:
    print('一切正常')
finally:
    print('无论是否有异常都会得到执行')