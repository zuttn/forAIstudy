"""
1、练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例
"""
import re

re.match(r'colou*r','colouuuur')   # 匹配成功
re.match(r'colou*r','color')       # 匹配成功
re.match(r'colou*r','colour')      # 匹配成功

print(re.match(r'colou?r','colouuur').group())     # 匹配失败-只能匹配color和colour

print(re.match(r'colo{4,5}ur','coloooour').group())   # 匹配成功
print(re.match(r'colo{4,5}ur','coloooor').group())    # 匹配失败 u缺失
print(re.match(r'colo{4,5}ur','colooour').group())    # 匹配失败 少了o

print(re.match(r'.olour', 'olour').group())       # 匹配失败，空字符

print(re.match(r'[0-9a-zA-Z]', 'oo').group())     # 匹配成功，但只输出o
print(re.match(r'\w.*', '虎wsdj 9。').group())
print(re.match(r'1[3-9]\d{2}', '1523').group())   # 匹配成功

# 匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
print(re.match(r'[a-zA-Z0-9_]{8,20}', '78955656546').group())

# 匹配 hello 开头后跟4-10个字符
print(re.match(r'^hello.{4,10}', 'hello world').group())

# 匹配 <  >
print(re.match(r'^<[^>]*>$', '<sjjas09>').group())

