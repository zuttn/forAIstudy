# 作者: 王道 龙哥
# 2025年06月09日10时46分18秒
# xxx@qq.com
import re
ret = re.search(r"\d+", "阅读次数为 9999")
print(ret.group())


def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


# 示例用法
text = "abc123def456ghi789"
pattern = r"\d+"
result=find_second_match(pattern,text)
print(result)
print('-'*50)
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)
print('-'*50)
ret = re.sub(r"\d+", '998', "python = 997")
print(ret)
def add(ret):
    str_num=ret.group()
    return str(int(str_num)+2)


ret = re.sub(r"\d+", add, "python = 666 次")
print(ret)

text = "apple 1 apple 2 apple apple"
pattern = r"apple"
replacement = "orange"

new_text = re.sub(pattern, replacement,text,count=2)
print(new_text) #sub返回的就是替换后的结果

s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月21日18时48分。'
ret_s = re.sub(r'年|月', r'/', s)
ret_s = re.sub(r'日|分', r' ', ret_s)
ret_s = re.sub(r'时', r':', ret_s)
print(ret_s)

# findall 默认拿的是分组内的内容，如果需要全部的匹配内容，需要对分组加?:
com = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
ret = com.findall(ret_s)
print(ret)


ret = re.split(r":| ","info:xiaoZhang 33 shandong")
print(ret)