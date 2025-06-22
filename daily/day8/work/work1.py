"""
1.使用Python的队列deque
"""

from collections import deque

queue = deque()

queue.append('x')
queue.append('y')

print(queue.popleft())
print('-'*50)
for i in range(len(queue)):
    print(queue[i])
queue[0] = 'z'
print(queue)
