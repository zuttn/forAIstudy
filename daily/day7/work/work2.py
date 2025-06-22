"""
2、传递参数file1，通过sys.argv[1]打开文件，读取里边的内容并打印
如果传递的参数是file2，程序同样可以打印file2的文件内容
"""

import sys

file = open(sys.argv[1],'r+',encoding="utf-8")
txt = file.read()
print(txt)
# file.write("go on work hello world")
file.close()