# 作者: 王道 龙哥
# 2025年06月09日09时57分23秒
# xxx@qq.com
import re

ret = re.match(r"[1-9]?\d", "0")
print(ret.group())  # 8

ret = re.match(r"[1-9]?\d$", "04")
if ret:
    print(ret.group())
else:
    print('不能匹配')

ret = re.match(r"[1-9]?\d$|100", "100")
if ret:
    print(ret.group())
else:
    print('不能匹配')

print('-' * 60)
email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", "xiaowang@qq.com", 'xiaoming@126.com', 'test@gmail.com']

for email in email_list:
    ret = re.match(r'\w{4,20}@(163|126|qq)\.com$', email)
    if ret:
        print(f'{email} 是邮箱')
    else:
        print(f'{email} 不是邮箱')

# ([^-]*) 代表没有遇到小横杠-就一直进行匹配，一直匹配下去
ret = re.match(r"([^-]+)-(\d+)", "010-12345678")
if ret:
    print(ret.group())
    print(ret.group(1))  # 第一个分组内容
    print(ret.group(2))  # 第二个分组内容

#\num引用分组

# 能够完成对正确的字符串的匹配
ret = re.match(r"<([a-zA-Z]*)>(\w*)</\1>", "<html>hh</html>")
if ret:
    print(ret.group())
    print(ret.group(2))
else:
    print('匹配失败')

labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]

for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)

#给分组起别名
for label in labels:
    ret = re.match(r"<(?P<xiongda>\w*)><(?P<xionger>\w*)>.*</(?P=xionger)></(?P=xiongda)>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)