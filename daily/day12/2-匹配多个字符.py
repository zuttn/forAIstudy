# 作者: 王道 龙哥
# 2025年06月09日09时40分58秒
# xxx@qq.com
import re
ret = re.match("[A-Z][a-z]*","M")
print(ret.group())

ret = re.match("[A-Z][a-z]*","MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*","Aabcdef")
print(ret.group())

names = ["name1", "_name", "2_name", "__name__"]
for name in names:
    ret=re.match(r'[_a-zA-Z]\w*',name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 非法" % name)

print('-'*50)
# 需求：匹配出，0到99之间的数字
ret = re.match("[1-9]?[0-9]","7")
print(ret.group())

ret = re.match(r"[1-9]?\d","33")
print(ret.group())

ret = re.match(r"[1-9]?\d","09")
print(ret.group())

print('-'*50)
ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
print(ret.group())
#默认是贪婪的
ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
print(ret.group())