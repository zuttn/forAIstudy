"""
2、完成二分查找，哈希查找
"""

import random
MAXKEY = 10
class Search:
    def __init__(self,arr_len):
        self.arr_len = arr_len
        self.arr = ['1','3','4','5','5','7','8','10','11','19','20']

    def bi_search(self,n):
        arr = self.arr
        arr_len = self.arr_len
        low = 0
        high = arr_len - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > n:
                high = mid - 1
            elif arr[mid] < n:
                low = mid + 1
            elif arr[mid] == n:
                return mid + 1
            else:
                return -1



    def elf_hash(self,hash_str: str) -> int:
        """
        返回的是哈希值
        :param hash_str:
        :return:
        """
        h = 0
        g = 0
        for i in hash_str:
            h = (h << 4) + ord(i)
            g = h & 0xf0000000
            if g:
                h ^= g >> 24
            h &= ~g
        return h % MAXKEY

    def create_hash(self):
        hash_table = [None] * MAXKEY
        for i in self.arr:
            if hash_table[self.elf_hash(i)] is None:
                hash_table[self.elf_hash(i)] = [i]
            else:
                hash_table[self.elf_hash(i)].append(i)
        return hash_table


    def hash_search(self,str,hash_table):
        hash_code = self.elf_hash(str)   # 拿到哈希值
        # 在哈希表里面查找到这个str的哈希值就进链表里面查看看有没有
        if hash_table[hash_code] is not None:
            for i in hash_table[hash_code]:
                if i == str:
                    return hash_code
            else:
                return -1



search_tool = Search(10)
# index = search_tool.bi_search(10)
# print(index)

hash_table = search_tool.create_hash()
print(hash_table)
print(search_tool.hash_search('10',hash_table))

