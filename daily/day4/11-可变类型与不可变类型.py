# 作者: 王道 龙哥
# 2025年05月29日16时32分46秒
# xxx@qq.com


def change(num):
    print(f'num地址{id(num)}')
    num = 5
    print(f'num修改后的地址{id(num)}')


a = 10
print(f'change之前{id(a)}')
change(a)
print(f'change之后{id(a)}')

print('-' * 50)
my_list = [1, 2, 3]


def change_list(num_list):
    print(f'id(num_list)={id(num_list)}')
    num_list[0]=10
    print(f'修改后 id(num_list)={id(num_list)}')


print(f'change_list之前{my_list},id={id(my_list)}')
change_list(my_list)
print(f'change_list之后{my_list},id={id(my_list)}')
