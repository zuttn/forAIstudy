# 作者: 王道 龙哥
# 2025年06月03日16时22分19秒
# xxx@qq.com

import sys

print(sys.argv)

# print(sys.argv[1])

file=open(sys.argv[1],encoding='utf8')
print(file.read())
file.close()