from typing import List


class Node:

    def __init__(self, 
                 index,
                 key, 
                 parent = None, 
                 leftch = None,
                 rightch = None):
        self.index = index
        self.key = key
        self.parent = parent
        self.leftch = leftch
        self.rightch = rightch

    def is_leaf(self):
        return bool(self.leftch or self.rightch)

    def set_left_child(self, leftch):
        self.leftch = leftch

    def set_right_child(self, rightch):
        self.rightch = rightch


class Tree:

    def __init__(self, size):
        self.storage = [None] * size

    def add_node(self, index, key, lchindex, rchindex):
        this = self.storage[index] or Node(index, key)
        if this.key == -1:
            this.key = key
        if lchindex != -1:
            lchild = self.storage[lchindex] or Node(lchindex, -1)
            this.set_left_child(lchild)
            lchild.parent = this
            self.storage[lchindex] = lchild
        if rchindex != -1:
            rchild = self.storage[rchindex] or Node(rchindex, -1)
            this.set_right_child(rchild)
            rchild.parent = this
            self.storage[rchindex] = rchild
        self.storage[index] = this

    def in_order_traverse(self, local_root = None):
        local_root = local_root or self.storage[0]
        if local_root.leftch: self.in_order_traverse(local_root.leftch)
        print(local_root.key, end=' ')
        if local_root.rightch: self.in_order_traverse(local_root.rightch)

    def pre_order_traverse(self, local_root = None):
        local_root = local_root or self.storage[0]
        print(local_root.key, end=' ')
        if local_root.leftch: self.pre_order_traverse(local_root.leftch)
        if local_root.rightch: self.pre_order_traverse(local_root.rightch)

    def post_order_traverse(self, local_root = None):
        local_root = local_root or self.storage[0]
        if local_root.leftch: self.post_order_traverse(local_root.leftch)
        if local_root.rightch: self.post_order_traverse(local_root.rightch)
        print(local_root.key, end=' ')

def main():
    n_nodes = int(input())
    tree = Tree(n_nodes)
    for i in range(0, n_nodes):
        key, lchidx, rchidx = list(map(int, input().split(' ')))
        tree.add_node(i, key, lchidx, rchidx)
    tree.in_order_traverse()
    print('')
    tree.pre_order_traverse()
    print('')
    tree.post_order_traverse()

main()
        
