# 作者: 王道 龙哥
# 2025年05月30日16时38分12秒
# xxx@qq.com

a, b = 1, 2
print(a, b)
a, b = b, a  # 交换两个变量
print(a, b)


def print_info(name, gender=True,age=None):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    if age:
        print("%s 是 %s 年龄 %d" % (name, gender_text,age))
    else:
        print("%s 是 %s " % (name, gender_text))


print_info('小明',False)
print_info('小明',age=18)