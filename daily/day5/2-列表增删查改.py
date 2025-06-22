# 作者: 王道 龙哥
# 2025年05月30日09时50分55秒
# xxx@qq.com

name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
print(name_list[0])

#查值，返回下标
print(name_list.index('wangwu'))

# 2.修改
name_list[2]='王五'

print(name_list)

# 3. 增加
# append 方法可以向列表的末尾追加数据
name_list.append('王小二')
print(name_list,id(name_list))
name_list.insert(0,'小美美')
print(name_list,id(name_list))

# extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)
print(name_list)

# 4.删除
# remove 方法可以从列表中删除指定的数据
name_list.remove("王五")
print(name_list)
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
print(name_list)
# pop 方法可以指定要删除元素的索引
name_list.pop(3)
print(name_list,id(name_list))
# clear 方法可以清空列表
# name_list.clear()
# print(name_list,id(name_list))

#删除
del name_list[1]
print(name_list)

# 5.统计
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("lisi")
print("lisi出现了 %d 次" % count)

