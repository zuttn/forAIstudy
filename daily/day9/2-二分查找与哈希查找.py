# 作者: 王道 龙哥
# 2025年06月05日16时12分15秒
# xxx@qq.com

def bsearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1


MAXKEY = 10


def elf_hash(hash_str:str)->int:
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


if __name__ == '__main__':
    # arr = [3, 10, 21, 29, 33, 55, 74, 84, 84, 91]
    # print(bsearch(arr, 74))
    str_list = ["xiongda", "lele", "hanmeimei", "wangdao", "fenghua","fenghua"]
    hash_table=[None]*MAXKEY  #初始化一个哈希表
    for i in str_list:
        if hash_table[elf_hash(i)] is None:
            hash_table[elf_hash(i)]=[i] #第一次放入
        else:
            hash_table[elf_hash(i)].append(i) #哈希冲突后拉链法解决
    print(hash_table)
