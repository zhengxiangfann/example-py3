#-*-coding:utf_8 -*-


class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySortTree:

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def serach(self, key):
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry:
                bt = bt.left
            elif key > entry:
                bt = bt.right
            else:
                return entry

    def insert(self, key):
        bt = self._root
        if not bt:
            self._root = BSTNode(key)
            return
        while True:
            entry = bt.data
            if key < entry:
                if bt.left is None:
                    bt.left = BSTNode(key)
                    return
                bt = bt.left
            elif key > entry:
                if bt.right is None:
                    bt.right = BSTNode(key)
                    return
                bt = bt.right
            else:
                bt.data = key
                return

    def delete(self, key):
        p, q = None, self._root # p为q 的父节点
        if not q:
            print('empty tree')
            return
        while q and q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            if not q:
                return

        if not q.left:
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return
        r = q.left
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            slef._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            q.right = q.left

    def __iter__(self):
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.data
            node = node.right


if __name__ == '__main__':
    LIS = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
    bs_tree = BinarySortTree()
    for i in range(len(LIS)):
        bs_tree.insert(LIS[i])

    for i in bs_tree:
        print(i, end=' ')




