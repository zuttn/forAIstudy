# 作者: 王道 龙哥
# 2025年06月02日16时12分51秒
# xxx@qq.com
class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')


class C(A, B):
    pass


c = C()
c.demo()
print(C.__mro__)
# mro 表示寻找对象的过程，C找到的第一个对象是A