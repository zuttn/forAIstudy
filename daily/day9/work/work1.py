"""
1、完成快速排序，堆排序
"""
import random


class Sort:
    def __init__(self,arr_len):
        self.arr_len = arr_len
        self.arr = [random.randint(0,100) for _ in range(arr_len)]

    def __partition(self, low, high):
        pivot = self.arr[low]
        while low < high:
            while low < high and self.arr[high] >= pivot:
                high-=1
            self.arr[low] = self.arr[high]
            while low < high and self.arr[low] <= pivot:
                low+=1
            self.arr[high] = self.arr[low]
        self.arr[low] = pivot
        return low

    def quick_sort(self,low,high):
        if low < high:  # low == high 时 ， 分割成一个元素 ， 已经有序， 没必要分
            pivot = self.__partition(low,high)
            self.quick_sort(low,pivot-1)
            self.quick_sort(pivot+1,high)

    def __adjust(self, pos , arr_len):
        dad = pos
        son = pos * 2 + 1  # 0-base 数组
        while son < arr_len:
            if son+1 < arr_len and self.arr[son] < self.arr[son+1]:
                son = son + 1
            if self.arr[son] > self.arr[dad]:
                self.arr[son],self.arr[dad] = self.arr[dad],self.arr[son]
            else:
                break  # 已经是大根堆了，不需要调整
            dad = son
            son = dad * 2 + 1

    def heap_sort(self):
        brunch = self.arr_len//2 - 1
        arr_len = self.arr_len   # 用arr_len 而不是 self.arr_len , 防止改变数组的长度
        # 初始化一个大根堆
        while brunch>=0:
            # burnch 要 >=0 因为，根也要调整
            self.__adjust(brunch , arr_len)
            brunch -= 1

        # 排序
        while arr_len>0:
            # arr_len 要 >0  如果是 >=0  arr_len = 0 后 arr_len-1 越界了
            self.arr[0],self.arr[arr_len-1] = self.arr[arr_len-1],self.arr[0]
            print(self.arr[arr_len-1],end=" ")
            arr_len -= 1
            self.__adjust(0 , arr_len)


if __name__ == '__main__':
    tool = Sort(10)
    print(tool.arr)
    tool.heap_sort()