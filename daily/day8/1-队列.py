# 作者: 王道 龙哥
# 2025年06月04日09时27分31秒
# xxx@qq.com
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append('zhangsan')
print(queue)
queue.popleft()
print(queue)

queue[0] = 'xiongda'  # 并不是支持了随机访问，内部依靠遍历
print(queue)
