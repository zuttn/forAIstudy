# 作者: 王道 龙哥
# 2025年05月30日14时55分28秒
# xxx@qq.com
num_str = "0123456789"
print(num_str[2:6])  # 左闭右开
print(num_str[2:])
print(num_str[:6])
print(num_str[:])
print(num_str[::2])
print(num_str[1::2])
print(num_str[2:-1])
print(num_str[-2:])
print(num_str[::-1])
print(num_str[:4:-1])  # 步长为负时，开始索引要大于结束索引

str_list = list(num_str)  # 把字符串变为列表
print(str_list)
str_list.reverse()
print(''.join(str_list))
