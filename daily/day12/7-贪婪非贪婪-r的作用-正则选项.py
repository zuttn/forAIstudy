# 作者: 王道 龙哥
# 2025年06月09日11时11分06秒
# xxx@qq.com

import re
s="This is a number 234-235-22-423"
ret=re.match(r".+?(\d+-\d+-\d+-\d+)",s)
print(ret.group(1))

mm = "c:\\a\\b\\c"
print(mm)
ret = re.match(r'c:\\',mm).group()
print(ret)

s='abc123今天天气好'

ret=re.match(r'\w+',s,re.A)
print(ret.group())

ret=re.match('ABC',s,re.I)
print(ret.group())

print('-'*50)
s='abc\nefg'
ret=re.match(r'.+',s,re.S)
print(ret.group())