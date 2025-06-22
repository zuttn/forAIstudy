"""
4.完成冒泡排序
"""
import random


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [random.randint(1,99) for _ in range(10)]
bubble_sort(arr)
print(arr)

