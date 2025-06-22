# 作者: 王道 龙哥
# 2025年05月30日16时14分24秒
# xxx@qq.com

# 0000 1001  9
# 0000 1010 10
# 0000 0011  3
# 1111 1101  -3
def find_two_number():
    my_list = [1, 1, 3, 8, 3, 9, 8, 10]
    # 分成2堆
    result = 0
    for i in my_list:
        result ^= i

    split_flag = result & -result  # 一个数和自己的负数进行按位与，就可以拿到最低位为1的数
    result1, result2 = 0, 0
    for i in my_list:
        if split_flag & i:
            result1 ^= i
        else:
            result2 ^= i
    print(f'找出出现一次的两个数{result1}，{result2}', )


def count_one_number():
    """
    统计一个数中1的个数
    :return:
    """
    while True:
        number = int(input('请输入1个数'))
        flag = 1
        count = 0  # 统计位上1的数目
        for i in range(64):
            if number & flag:
                count += 1
            flag <<= 1
        print(count)
        # print(bin(number).count('1'))


# find_two_number()
count_one_number()
