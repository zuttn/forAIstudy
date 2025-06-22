# 作者: 王道 龙哥
# 2025年06月04日09时55分32秒
# xxx@qq.com
from collections import deque


class Node:
    def __init__(self, ele=-1, left=None, right=None):
        self.ele = ele
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.queue = deque()  # 初始化一个空的队列

    def insert(self, ele):
        """
        往树中放一个元素
        :param ele:
        :return:
        """
        new_node = Node(ele)  # 初始化一个结点对象
        self.queue.append(new_node)
        if self.root is None:  # 树根为空
            self.root = new_node
        else:
            # 判断父亲的左孩子是否为空
            if self.queue[0].left is None:
                self.queue[0].left = new_node
            else:
                self.queue[0].right = new_node
                self.queue.popleft()  # 父结点满了，出队，因为完全二叉树有右孩子=父节点满了，保证每次都让有左右孩子的节点出队

    def pre_order(self, node: Node):
        """
        前序遍历就是深度优先遍历
        :param node:
        :return:
        """
        if node:
            print(node.ele, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def mid_order(self, node: Node):
        if node:
            self.mid_order(node.left)
            print(node.ele, end=' ')
            self.mid_order(node.right)

    def last_order(self,node: Node):
        if node:
            self.last_order(node.left)
            self.last_order(node.right)
            print(node.ele, end=' ')

    def level_order(self):
        queue=[]
        queue.append(self.root)
        while queue:
            node=queue.pop(0)
            print(node.ele,end=' ') #打印出队元素值
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 10):
        tree.insert(i)  # 树的结点插入
    tree.pre_order(tree.root)
    print('\n------------------------')
    # tree.mid_order(tree.root)
    # print('\n------------------------')
    # tree.last_order(tree.root)
    # print('\n------------------------')
    # tree.level_order()
