# 作者: 王道 龙哥
# 2025年06月06日10时53分37秒
# xxx@qq.com

BLACK = 0
RED = 1


class RedBlackTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None  # 父亲
        self.color = RED


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = RedBlackTreeNode(value)
        # 通过二叉查找树原理，先把new_node放入树中
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node:
                parent = current_node  # 存new_node的父亲
                if new_node.value > current_node.value:
                    current_node = current_node.right
                else:
                    current_node = current_node.left

            if new_node.value > parent.value:  # 父节点比new_node小
                parent.right = new_node  # 放到父节点的右边
            else:
                parent.left = new_node  # 放到父节点的左边
            new_node.p = parent  # 新结点的p 指向parent
        self.fix_insert(new_node)  # 修正

    def fix_insert(self, node):
        pass

    def pre_order(self, node: RedBlackTreeNode, parent, direction):
        if node:
            print(
                f'{node.value}{'R' if node.color == RED else 'B'} 是{parent.value if parent else '根'} {direction + '孩子' if direction else ''}')
            self.pre_order(node.left, node, 'L')
            self.pre_order(node.right, node, 'R')


if __name__ == '__main__':
    my_tuple = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    rbtree = RedBlackTree()
    for i in my_tuple:
        rbtree.insert(i)
    rbtree.pre_order(rbtree.root, None, '')
