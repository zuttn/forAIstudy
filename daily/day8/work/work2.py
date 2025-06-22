"""
2.实现有5个元素的循环队列
"""

class circle_Queue:
    def __init__(self,maxSize):
        self.front = 0
        self.rear = 0
        self.maxSize = maxSize
        self.arr = [0] * (maxSize+1)

    def enqueue(self,value):
        rear = self.rear
        maxSize = self.maxSize
        front = self.front

        assert (rear+1)%maxSize!=front,'这里满了'
        self.arr[rear] = value
        self.rear = (rear+1)%maxSize

    def dequeue(self):
        if self.front == self.rear:
            raise Exception('队里没元素')
        e = self.arr[self.front]
        self.front = (self.front+1)%self.maxSize
        return e

    def getLen(self):
        return (self.rear - self.front + self.maxSize) % self.maxSize

try:
    cqueue = circle_Queue(5)
    cqueue.enqueue(3)
    cqueue.enqueue(2)
    cqueue.enqueue(1)
    cqueue.enqueue(4)
    for i in range(cqueue.getLen()):
        print(cqueue.dequeue())
except Exception as e:
    print(e)

