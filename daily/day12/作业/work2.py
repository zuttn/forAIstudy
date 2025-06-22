"""
2、练习上课的search，findall,sub等案例
"""
import re

# 寻找阅读次数   阅读次数为 9999
print(re.search(r'\d+', '阅读次数=9999').group())

# 寻找第二匹配的项
def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)       # 和findall区别 ： finditer返回迭代器，带位置信息 ， findall返回列表
    try:
        # 迭代器存在，遍历一次迭代器找到第二个匹配对象
        next(matches)
        second_match = next(matches)
        return second_match.group()
    except Exception:
        return None

# 寻找第二串数字
print(find_second_match(r'\d+', '12uis90ku0'))


# 寻找"python = 9999, c = 7890, c++ = 12345"py、c、c++的阅读次数
matches = re.findall(r'\d+','python = 9999, c = 7890, c++ = 12345')
for match in matches:
    print(f'{int(match)}',end = '  ')
print('')
# 替换前两个apple 变成 orange "apple apple apple apple"
text = "apple apple apple apple"
print(re.sub(r'apple', 'orange', text, count=2))
