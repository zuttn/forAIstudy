# 作者: 王道 龙哥
# 2025年06月09日09时51分17秒
# xxx@qq.com
import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]

for email in email_list:
    ret=re.match(r'\w{4,20}@163\.com$',email)
    if ret:
        print(f'{email} 是163邮箱')
    else:
        print(f'{email} 不是163邮箱')