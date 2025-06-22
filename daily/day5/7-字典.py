# 作者: 王道 龙哥
# 2025年05月30日11时05分35秒
# xxx@qq.com
# key:value key必须是不可变数据类型，value可以是任意类型
# None 空对象
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}

xiaoming_dict = {"name": "小明"}

# 1. 取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的key不存在，程序会报错！
# print(xiaoming_dict["name123"])
print(xiaoming_dict.get('name123')) #key不存在，不会报错，返回None
# 2. 增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"

# setdefault是新增一个键值对，如果对应的键存在，就啥都不做
xiaoming_dict.setdefault('age', 20)
print(xiaoming_dict)

# 3.删除
# xiaoming_dict.pop('age')
print(xiaoming_dict)

# 4. 统计键值对数量
print(len(xiaoming_dict))

# 5. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}

# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
# 6. 清空字典
xiaoming_dict.clear()

print(xiaoming_dict)
print('-'*50)
# 7.遍历
xiaoming_dict = {"name": "小明",
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k,v in xiaoming_dict.items():

    print(f'{k}--{v}')

card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10086"}
]

for card_info in card_list:

    print(card_info)

dict1={} #效率更高
dict2=dict()