"""
1、sort，sorted的各种使用（根据上课的排序代码要自己写一遍）
"""
from operator import itemgetter, attrgetter

my_dict = {'a': 2, 'b': 3, 'c': 1}
print(sorted(my_dict.items(), key=lambda x:x[1]))


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'C', 12),
    ('dave', 'B', 10),
]


# 对第三个排序
print(sorted(student_tuples, key=lambda x:x[2]))            # x表示列表中的任意一项元组，x[2]表示任意元组的第三项
# 先对第二个再对第三个排序
print(sorted(student_tuples, key=lambda x:(x[1],x[2])))
# 不用lambda表达式
print(sorted(student_tuples, key=itemgetter(0)))

print('*' *100)

class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        repr好处可以返回元组类型
        :return:
        """
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('jane', 'B', 19),
    Student('dave', 'D', 10),
]

# 用属性做排序标准
print(sorted(student_objects, key=lambda x:x.grade))
# 用下标做排序标准
print(sorted(student_objects, key=attrgetter('age')))
# 多层排序
print(sorted(student_objects, key=attrgetter('name','grade')))
print(sorted(student_objects, key=lambda x:(x.name, -x.age)))  # 对年龄逆向排序

mydict = { 'Li'   : ['M',7],
           'Zhang': ['E',2],
           'Wang' : ['P',3],
           'Du'   : ['C',2],
           'Ma'   : ['C',9],
           'Zhe'  : ['H',7] }

# mydict.items() ---> 变成元组列表   x[1] 是元组的第二项,是一个列表 ， x[1][0] 是元组内列表的第二列
# 对第二个元组的第二列排序
print(sorted(mydict.items(), key = lambda x:x[1][0]))


gameresult = [
    { "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
    { "name":"David", "wins":3, "losses":5, "rating":57.00 },
    { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
    { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
print(sorted(gameresult, key=lambda x:x['rating']))
# x是一项字典 ， x['rating'] 是这一项字典里的rating
