# 作者: 王道 龙哥
# 2025年05月30日10时35分40秒
# xxx@qq.com

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))  # 地址不一样
print(id(b))

b = []
for i in range(10):
    b.append(i)
print(b)

a = [0] * 10  # 初始化10个零
print(a)

a = [x for x in range(10)]  # 初始化一个0-9列表
print(a)
print('-' * 50)
a = [j for i in range(10) for j in range(i)]
print(a)

a2 = [[col * row for col in range(5)] for row in range(5)]
print(a2)

b = [j for i in a2 for j in i]  # 二维变一维
print(b)

# 只要偶数
a = [i for i in range(10) if i % 2 == 0]
print(a)

age = 18
status = "成年人" if age >= 18 else "未成年人"
print(status)  # 输出：成年人

a = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(a)
