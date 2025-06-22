# 作者: 王道 龙哥
# 2025年06月02日11时01分29秒
# xxx@qq.com

# 两个下划线开头，两个下划线结尾是内置方法
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        print(id(self))

    def run(self):
        print(f'{self.name} run')

    def eat(self):
        print('eat')

    def __del__(self):
        """
        对象被销毁时，会调用的
        :return:
        """
        print(f'{self.name} 被销毁了')

    def __str__(self):
        """
        打印对象时，会把str内的内容给出去
        :return:
        """
        return f'{self.name}:{self.age}'


print(dir(Person))
elephant = Person('大象', 18, 1.75)
elephant.run()
print(id(elephant))
print(dir(elephant))
print('-' * 50)
print(elephant)
print('-' * 50)
del elephant
print('程序结束')
