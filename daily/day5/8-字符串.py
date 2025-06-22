# 作者: 王道 龙哥
# 2025年05月30日14时35分32秒
# xxx@qq.com
str1 = "Hello Python"
for i in str1:
    print(i,end='')
print()

print(len(str1))
print(str1[4])
print(str1.count('ll'))
print(str1.index('Py'))
print('-'*50)
print('hello123'.isalnum())
print('hello'.isalpha())
print('123'.isdecimal())

print('-----查找与替换---------')
print('hello123'.find('123',0))

print('hello world'.replace('llo','LLO'))

print('-----拆分与连接---------')
str_list='你好 今天 是个 好天气'.split()
print(str_list)
str_list1='你好,今天,是个,好天气'.split(',')
print(str_list1)
str_list2='hello\nworld\ntoday'
print(str_list2.splitlines())
result=''.join(str_list)
print(result)