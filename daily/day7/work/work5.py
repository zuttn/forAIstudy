"""
5.完成栈的编写
"""

class Stack:
    def __init__(self,content):
        self.top = -1
        self.content = content
        self.arr = [0 for _ in range(int(content))]

    def push(self,object):
        if self.top+1 >= self.content:
            return False
        else:
            self.arr[self.top] = object
            self.top += 1
            return True

    def pop(self):
        if self.top < 0:
            return False
        else:
            print(self.arr[self.top-1])
            self.arr[self.top] = None
            self.top -= 1
            return True

if __name__ == '__main__':
    stack = Stack(5)
    stack.push(31)
    stack.push(42)
    stack.pop()