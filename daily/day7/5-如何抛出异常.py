# 作者: 王道 龙哥
# 2025年06月03日10时42分32秒
# xxx@qq.com
def input_password():

    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    raise Exception('密码长度小于8位')
try:
    input_password()
except Exception as e:
    print(e)