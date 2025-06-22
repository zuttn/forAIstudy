# 作者: 王道 龙哥
# 2025年06月03日16时29分51秒
# xxx@qq.com
import os
#会把字符串的内容作为代码来执行
print(eval("1+1"))

file=open('project.txt', encoding='utf8')
txt=file.read()
project_dict=eval(txt)
file.close()

print(eval("__import__('os').system('ls')"))