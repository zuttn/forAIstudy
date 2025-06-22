"""
2、通过自己写的hash函数，实现美女与野兽.txt的单词词频为前10的统计（小说的txt文件在QQ群文件）
输入结果如下（供参考，因为分词方法的差异可以造成不同）：
['to', 245] ['and', 240] ['the', 239] ['she', 151] ['was', 113] ['her', 104] ['he', 103] ['of', 99] ['that', 96] ['a', 93]

"""
import sys
import re

# 思路：把所有字符存到哈希表里面，用拉链法解决冲突，在哈希表里面查找前十长的拉链

MAXSIZE = 100000


def hash_code(str):
    code = 0
    for char in str:
        code = (code * 31 + ord(char)) % MAXSIZE  # 使用31作为乘数进行哈希计算
    return code

def create_hash_table(str_arr):
    hash_table = [None] * MAXSIZE
    # 遍历字符串数组
    for s in str_arr:
        # 如果s对应的哈希值在哈希表中不存在，存入s
        if hash_table[hash_code(s)] is None:
            hash_table[hash_code(s)] = [s]
            # [s] 的意思是，把s作为一个列表存储
        else:
            hash_table[hash_code(s)].append(s)

    return hash_table
def sort_fre(path):
    file = open(path,'r')
    txt = file.read()
    words = re.findall(r'\b\w+\b', txt.lower())
    # 把所有word存入哈希表
    word_hash_table = create_hash_table(words)



sort_fre('Beauty and The Beast.txt')