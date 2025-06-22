# 作者: 王道 龙哥
# 2025年06月02日15时11分41秒
# xxx@qq.com
class Women:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 为了类内部使用的属性

    def __secret(self):
        """
        为了类内部其他方法而准备的方法
        :return:
        """
        print(self.__age)

    def boy_friend(self):
        self.__secret()


xiaohong = Women('小红', 18)
xiaohong.boy_friend()

# 私有属性，外部不能直接访问到
# print(xiaohong._Women__age)
