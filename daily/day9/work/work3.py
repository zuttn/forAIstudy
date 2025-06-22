"""
3、完成归并排序，计数排序，位图
"""
import random


class Sort:
    def __init__(self,arr_len):
        self.arr_len = arr_len
        self.arr = [random.randint(-100,100) for i in range(arr_len)]

    def __merge(self, low, mid, high):
        i, j = low, mid + 1
        idx = low
        arr = self.arr
        # 初始化一个临时数组
        temple_arr = arr.copy()
        # 赋值 ， 每次赋值 idx++ ， 赋值数下标++
        while i <= mid and j <= high:
            # 循环保证下标不越界
            if temple_arr[i] < temple_arr[j]:
                arr[idx] = temple_arr[i]
                idx += 1
                i += 1
            else:
                arr[idx] = temple_arr[j]
                idx += 1
                j += 1

        # 把剩下的继续赋值
        while i <= mid:
            arr[idx] = temple_arr[i]
            idx += 1
            i += 1
        while j <= high:
            arr[idx] = temple_arr[j]
            idx += 1
            j += 1

    def merge_sort(self, low, high):
        if low < high:  # low == high 时， 已经有序 ， 不需要low<=high
            mid = (low + high)//2
            self.merge_sort(low, mid)       # 排左边
            self.merge_sort(mid+1 , high)   # 排右边
            self.__merge(low, mid, high)    # 合并

    def count_sort(self):
        min_val = min(self.arr)       # min_val < 0 时 ，i-min_val大于0 ； min_val > 0 时， i-min_val 更大于0
        max_val = max(self.arr)
        count = [0] * (max_val-min_val+1)    # 默认出现次数为0
        for i in range(self.arr_len):
            # 扫描arr中的每个数，存到计数数组里面，数作为数组下标，出现次数作为数组内容
                count[self.arr[i]-min_val] += 1

        # 回写 : 扫描count，扫描到count[i]>0，arr[0] = count[i] count[i]--
        arr_idx = 0
        for val in range(min_val,max_val+1):          # 扫描数值范围
            for _ in range(count[val - min_val]):     # count[val - min_val] > 0 ：代表数字val出现过 ， 把 val 回写
                self.arr[arr_idx] = i
                arr_idx += 1


my_tool = Sort(10)
print(my_tool.arr)
# my_tool.merge_sort(0 ,9)
my_tool.count_sort()
print(my_tool.arr)