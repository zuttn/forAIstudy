# 作者: 王道 龙哥
# 2025年06月02日16时20分46秒
# xxx@qq.com
class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog: Dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        dog.game()


if __name__ == '__main__':
    wangcai = Dog('旺财')
    xiaotianquan = XiaoTianDog('哮天犬')
    xiaoming = Person('小明')
    xiaoming.game_with_dog(wangcai)
    xiaoming.game_with_dog(xiaotianquan)
