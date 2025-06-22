"""
3.新建包，并使用自己建的包
"""

import os

os.rmdir('../../../../daily/day7/作业/my_dir')
os.mkdir('../../../../daily/day7/作业/my_dir')

print('\n这里是我的当前工作目录',os.getcwd())
dir_list = os.listdir('')
print(dir_list)