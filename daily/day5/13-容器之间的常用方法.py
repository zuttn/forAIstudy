# 作者: 王道 龙哥
# 2025年05月30日16时04分32秒
# xxx@qq.com

a = (1, 2, 3)
b = ('a', 'b', 'c')

result = list(zip(a, b))
print(result)

my_dict = {}
for k, v in result:
    my_dict[k] = v
print(my_dict)

# 字典生成式
my_dict = {k: v for k, v in result}
print(my_dict)

#如何使用enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list2=list(enumerate(seasons))
print(list2)
my_dict={v:k for k,v in list2}
print(my_dict)
