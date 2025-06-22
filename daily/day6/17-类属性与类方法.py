# 作者: 王道 龙哥
# 2025年06月02日16时25分09秒
# xxx@qq.com
class Tool:
    count = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod #使用classmethod装饰的方法称为类方法
    def show_tool_count(cls):
        print(f'类方法{cls.count}')

    @staticmethod
    def help():
        print('我只是一个帮助')

# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")
print(Tool.count)  # 访问类属性，修改类属性，都通过类名
print(tool1.count)  # 不规范
tool3.count = 99  # 给tool3对象增加了一个count的对象属性，这个不对的
print(tool3.count)

#类方法和静态方法，都使用类名调用
Tool.show_tool_count()
Tool.help()