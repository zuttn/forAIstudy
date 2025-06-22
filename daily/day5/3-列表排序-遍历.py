# 作者: 王道 龙哥
# 2025年05月30日10时31分45秒
# xxx@qq.com

name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]

# 升序，降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)

name_list.reverse() #反转
num_list.reverse()

print(name_list)
print(num_list)
print('-'*50)
for name in name_list:
    print(name)