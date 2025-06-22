# 作者: 王道 龙哥
# 2025年05月30日15时21分36秒
# xxx@qq.com
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


#前面记得加tuple
my_tuple=tuple(x for x in range(10))
print(my_tuple)

print(max('abracadabra'))