# 作者: 王道 龙哥
# 2025年06月06日16时11分45秒
# xxx@qq.com
list1 = [1, 3, 2, 4, 5, 3, 2]
# print(sorted(list1))
list1.sort()
print(list1)

# 字典
dict1 = {1: 'D', 3: 'B', 2: 'B', 4: 'E', 5: 'A'}
print(sorted(dict1))

# 字符串
str_list = "This is a test string from Andrew".split()
print(str_list)
print(sorted(str_list))


def compare_function(str1: str):
    return str1.lower()


print(sorted(str_list, key=compare_function))

# 按shift+alt 竖选
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]


def compare_function2(student):
    return student[2]


# lambda表达式是 匿名函数
print(sorted(student_tuples, key=lambda student: student_tuples[2]))


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
    Student('dave', 'B', 10),
]
print('-'*100)
print(sorted(student_objects, key=lambda student: student.age))
print('-'*100)
from operator import itemgetter, attrgetter
print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age'),reverse=True))

# 支持多层排序
print('-'*100)
print(sorted(student_tuples, key=itemgetter(1,2)))
print(sorted(student_objects, key=attrgetter('grade','age')))

print(sorted(student_tuples, key=lambda student: (student[1],student[2])))

#稳定排序
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=itemgetter(0)))

mydict = { 'Li'   : ['M',7],
           'Zhang': ['E',2],
           'Wang' : ['P',3],
           'Du'   : ['C',2],
           'Ma'   : ['C',9],
           'Zhe'  : ['H',7] }
print(sorted(mydict.items(), key=lambda x:x[1][1]))


gameresult = [
    { "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
    { "name":"David", "wins":3, "losses":5, "rating":57.00 },
    { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
    { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
print(sorted(gameresult, key=lambda x:x['rating']))
# x['rating']  :  x是一项字典 ， x['rating'] 是这一项字典里的rating

tuples1=[(3,5),(1,2),(2,4),(3,1),(1,3)]
print(sorted(tuples1,key=lambda x:(x[0],-x[1])))
