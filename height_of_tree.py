class Node:
    def __init__(self, val, parent=None, depth=1):
        self.val = val
        self.parent = parent
        self.children = []
        self.depth = depth

    def sink_down(self, parent_depth):
        self.depth = parent_depth + 1
        for child in self.children:
            child.sink_down(self.depth)

    def __repr__(self):
        return str((self.val, self.depth))

def calc_height(n, tree):
    tree_dict = {}
    max_depth = 0
    for leaf_val, leaf_parent in enumerate(tree):
        if leaf_val not in tree_dict:
            node = Node(leaf_val)
            tree_dict[leaf_val] = node
        if leaf_parent != -1:
            if leaf_parent not in tree_dict:
                node = Node(leaf_parent)
                tree_dict[leaf_parent] = node
            tree_dict[leaf_val].parent = tree_dict[leaf_parent]
            tree_dict[leaf_parent].children.append(tree_dict[leaf_val])
            tree_dict[leaf_val].sink_down(tree_dict[leaf_parent].depth)
        max_depth = max(max_depth, tree_dict[leaf_val].depth)
    return max(tree_dict.items(), key=lambda tup: tup[1].depth)[1].depth if tree_dict else max_depth

def main():
    n = int(input())
    tree = list(map(int, input().split(' ')))
    print(calc_height(n, tree))

def test():
    assert calc_height(10, [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]) == 4
    assert calc_height(0, []) == 0
    assert calc_height(1, [-1]) == 1
    assert calc_height(10, [-1, 7, 5, 5, 2, 0, 0, 0, 2, 0]) == 4
    assert calc_height(5, [4, -1, 4, 1, 1]) == 3
    assert calc_height(5, [-1, 0, 4, 0, 3]) == 4

main()