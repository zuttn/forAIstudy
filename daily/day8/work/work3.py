"""
3.完成二叉树的层次建树，并实现前序遍历，中序遍历，后序遍历，层序遍历
"""

from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class biTree:
    def __init__(self):
        self.root=None
        self.queue=deque()

    def insert(self,data):

        node = Node(data)
        self.queue.append(node)
        if self.root is None:
            self.root = node
        else:
            if self.queue[0].left is None:
                self.queue[0].left = node
            else:
                self.queue[0].right = node
                self.queue.popleft()

    def pre_order(self,node:Node):
        if node is None:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def mid_order(self,node:Node):
        if node is not None:
            self.mid_order(node.left)
            print(node.data,end=' ')
            self.mid_order(node.right)

    def post_order(self,node:Node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data)

    def level_order(self,node:Node):
        if node is not None:
            self.queue.clear()
            self.queue.append(node)
            while self.queue:
                tm_node = self.queue.popleft()
                print(tm_node.data,end=' ')
                if tm_node.left is not None:
                    self.queue.append(tm_node.left)
                if tm_node.right is not None:
                    self.queue.append(tm_node.right)


if __name__ == '__main__':
    myTree = biTree()
    myTree.insert('有')
    myTree.insert('独')
    myTree.insert('偶')
    myTree.insert('无')
    myTree.level_order(myTree.root)
    print('\n')
    myTree.mid_order(myTree.root)