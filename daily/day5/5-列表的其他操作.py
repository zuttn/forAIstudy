# 作者: 王道 龙哥
# 2025年05月30日10时53分44秒
# xxx@qq.com
a = [1, 2, 3, 4, 5]
b = [2, 3, 4]
print(id(a))
# print(a * 2)
# print(a + b)
a += b  # 等价于extend ,和a=a+b是不一样的
print(a)
print(id(a))