# 作者: 王道 龙哥
# 2025年06月03日15时28分03秒
# xxx@qq.com
import os

# os.rename('test.txt','test1.txt')

# os.remove('dir1/Readme')

file_list=os.listdir('../../../daily/day7')  # listdir("") 获取指定目录的所有目录
# print(file_list)

# os.mkdir('dir2')
# os.rmdir('dir1')
print(os.getcwd()) # getcwd() 获取当前目录
os.chdir('../../../daily/day7/8-使用包')
print(os.getcwd())