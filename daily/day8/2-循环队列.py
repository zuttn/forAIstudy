# 作者: 王道 龙哥
# 2025年06月04日09时38分10秒
# xxx@qq.com
class CircleQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [0] * max_size
        self.front = 0
        self.rear = 0

    def enqueue(self, element):
        # 判断队列是否满了
        if (self.rear + 1) % self.max_size == self.front:
            print('队列满了')
            return
        self.arr[self.rear]=element #元素放入
        self.rear=(self.rear+1)%self.max_size #rear加1

    def dequeue(self):
        # 判断队列是否为空
        if self.front==self.rear:
            print('队列为空')
            return
        element=self.arr[self.front] #拿元素
        self.front=(self.front+1)%self.max_size
        return element

if __name__ == '__main__':
    c = CircleQueue(5)
    c.enqueue(1)
    c.enqueue(2)
    c.enqueue(3)
    c.enqueue(4)
    c.enqueue(5)
    print(c.dequeue())