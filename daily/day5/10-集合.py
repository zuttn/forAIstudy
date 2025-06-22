# 作者: 王道 龙哥
# 2025年05月30日15时05分47秒
# xxx@qq.com
a=[1,2,3]
b=a.copy()
print(b)
a[0]=10
print(b)
print(a)

set1=set() #初始化空集合
print(type(set1))

my_set={'apple', 'banana', 'orange', 'cherry'}
print(my_set)
print('apple' in my_set)

my_set.discard('apple')
print(my_set)
