# 作者: 王道 龙哥
# 2025年05月29日09时27分48秒
# xxx@qq.com

s1 = 'abc"bcd'
s2 = "abc'def"
s3 = 'abc\'bcd\"'
s4 = 'abc\n123'
s5 = 'abc\\456'
s6 = '''
abc'bcd"def
'''
print(s4)
print(s5)
print(s6)
print('*'*90)
#练习字符转ASCII值

s7='b'
result=chr(ord(s7)-32)
print(ord(result))
print('*'*90)
print('abc'+'hij')

print('*'*90)
# print(123+'abc') #TypeError表示两个对象之间不能做对应的运算
print('haha')