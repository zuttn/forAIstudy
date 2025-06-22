# 作者: 王道 龙哥
# 2025年06月04日10时58分15秒
# xxx@qq.com
import random


class Sort:
    def __init__(self, arr_len):
        self.arr = []
        # self.arr =[3, 87, 2, 93, 78, 56, 61, 38, 12, 40]
        self.arr_len = arr_len
        self.arr_random()

    def arr_random(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, 99))

    def bubble(self):
        arr = self.arr
        for i in range(self.arr_len - 1, 0, -1):
            flag = True  # 是否有序,默认有序
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = False  # 发生交换，就没有序
            if flag:
                break

    def select(self):
        arr = self.arr
        # 外层i控制了无序数的起始位置
        for i in range(self.arr_len - 1):
            min_pos = i
            # 一轮遍历就会找到当前的最小值
            for j in range(i + 1, self.arr_len):
                if arr[j] < arr[min_pos]:
                    min_pos = j
            arr[min_pos], arr[i] = arr[i], arr[min_pos]

    def insert(self):
        arr = self.arr
        # 外层控制要插入的序列
        for i in range(1, self.arr_len):
            insert_val = arr[i]
            # 拿insert_val 对有序序列从后往前比
            j = i - 1
            while j >= 0:
                if insert_val < arr[j]:
                    arr[j + 1] = arr[j]
                else:
                    break
                j -= 1
            # 循环外面放入
            arr[j + 1] = insert_val

    def partition(self, left, right):
        arr = self.arr
        k = left
        random_pos = random.randint(left, right)
        arr[random_pos], arr[right] = arr[right], arr[random_pos]  # 避免陷入n平方的时间复杂度
        for i in range(left, right):
            if arr[i] < arr[right]:  # 最右边是分割值
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[right], arr[k] = arr[k], arr[right]  # 交换分割值到对应为止
        return k

    def quick(self, left, right):
        if left < right:  # 确保left小于right
            pivot = self.partition(left, right)
            self.quick(left, pivot - 1)
            self.quick(pivot + 1, right)

    def adjust_max_heap(self, adjust_pos, arr_len):
        arr = self.arr
        dad = adjust_pos
        son = 2 * dad + 1  # 左孩子
        while son < arr_len:  # 确保son小于列表长度
            if son + 1 < arr_len and arr[son + 1] > arr[son]:  # 比较左孩子和右孩子，谁大，谁大谁跟父亲比
                son += 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap(self):
        arr = self.arr
        # 调整为大根堆
        for dad_pos in range(self.arr_len // 2 - 1, -1, -1):
            self.adjust_max_heap(dad_pos, self.arr_len)
        for i in range(self.arr_len - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # 交换根部元素和列表最后一个元素
            self.adjust_max_heap(0, i)  # 把剩余元素继续调整为大根堆

    def __merge(self, low, mid, high):
        arr = self.arr
        arr_b = arr.copy()
        i, j, k = low, mid + 1, low
        while i <= mid and j <= high:
            if arr_b[i] <= arr_b[j]:
                arr[k] = arr_b[i]
                i += 1
            else:
                arr[k] = arr_b[j]
                j += 1
            k += 1
        # 需要把某一个剩下的继续放进去
        while i <= mid:
            arr[k] = arr_b[i]
            i += 1
            k += 1
        while j <= high:
            arr[k] = arr_b[j]
            j += 1
            k += 1

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)  # 排左边一半
            self.merge_sort(mid + 1, high)  # 排右边一半
            self.__merge(low, mid, high)

    def count_sort(self):
        count=[0]*100 #记录所有值出现次数的列表
        for i in self.arr:
            count[i]+=1
        #回填
        k=0
        for val in range(100):#遍历数值范围
            for j in range(count[val]):#对应数值出现了多少次，我们就回填多少次
                self.arr[k]=val
                k+=1

if __name__ == '__main__':
    my_sort = Sort(10)
    print(my_sort.arr)
    # my_sort.bubble()
    # my_sort.select()
    # my_sort.insert()
    # my_sort.quick(0, my_sort.arr_len - 1)
    # my_sort.heap()
    # my_sort.merge_sort(0,my_sort.arr_len - 1)
    my_sort.count_sort()
    print(my_sort.arr)
