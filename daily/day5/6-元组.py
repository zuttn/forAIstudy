# 作者: 王道 龙哥
# 2025年05月30日10时58分41秒
# xxx@qq.com

#不可变数据类型，只读的
info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 1. 取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("zhangsan"))

# 2. 统计计数
print(info_tuple.count("zhangsan"))
# 统计元组中包含元素的个数
print(len(info_tuple))

info_list=list(info_tuple)
print(info_list)
info_tuple=tuple(info_list)
print(info_tuple)

#不要犯错
info_tuple=(1,)
print(type(info_tuple))
for i in info_tuple:
    print(i)