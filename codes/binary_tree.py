class Node(object):
    def __init__(self, key, left=None, right=None):
        self._key = key
        self._left = left
        self._right = right

    @property
    def key(self):
        return self._key

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @key.setter
    def key(self, key):
        self._key = key

    @left.setter
    def left(self, left):
        self._left = left

    @right.setter
    def right(self, right):
        self._right = right

    def __repr__(self):
        return "(%s %s %s)" % (self.key, self.left, self.right)


class Stack(object):
    def __init__(self):
        self._a = list()

    def is_empty(self):
        return not bool(self._a)

    def pop(self):
        x = self._a[-1]
        self._a = self._a[:-1]
        return x

    def push(self, x):
        self._a.append(x)


def list_to_tree(a):
    la = len(a)
    if la == 0:
        return None
    if la == 1:
        return Node(a[0])
    m = (len(a) - 1) // 2
    return Node(a[m], list_to_tree(a[:m]), list_to_tree(a[m + 1:]))


def print_tree_pre_order(t):
    if not t:
        return
    print(t.key, end=' ')
    print_tree_pre_order(t.left)
    print_tree_pre_order(t.right)


def print_tree_in_order(t):
    if not t:
        return
    print_tree_in_order(t.left)
    print(t.key, end=' ')
    print_tree_in_order(t.right)


def print_tree_in_post_order(t):
    if not t:
        return
    print_tree_in_post_order(t.left)
    print_tree_in_post_order(t.right)
    print(t.key, end=' ')


def print_tree_in_pre_order_iter(t):
    s = Stack()
    s.push(t)
    while not s.is_empty():
        x = s.pop()
        if x:
            print(x.key, end=' ')
            s.push(x.right)
            s.push(x.left)


def print_tree_in_order_iter(t):
    if not t:
        return
    s = Stack()
    s.push(t)
    while not s.is_empty():
        x = s.pop()
        while x:
            s.push(x)
            x = x.left
        if not s.is_empty():
            x = s.pop()
            print(x.key, end=' ')
            s.push(x.right)


def print_tree_in_order_iter_no_stack(t):
    """Morris Traversal"""
    cur = t
    while cur:
        if not cur.left:
            print(cur.key, end=' ')
            cur = cur.right
        else:
            x = cur.left
            while True:
                if not x.right:
                    x.right = cur
                    cur = cur.left
                    break
                elif x.right == cur:
                    x.right = None
                    print(cur.key, end=' ')
                    cur = cur.right
                    break
                x = x.right


def print_tree_in_pre_order_iter_no_stack(t):
    """Morris Traversal"""
    cur = t
    while cur:
        if not cur.left:
            print(cur.key, end=' ')
            cur = cur.right
        else:
            x = cur.left
            while True:
                if not x.right:
                    x.right = cur
                    print(cur.key, end=' ')
                    cur = cur.left
                    break
                elif x.right == cur:
                    x.right = None
                    cur = cur.right
                    break
                x = x.right


if __name__ == "__main__":
    n = 20
    a = list(range(n))
    print(a, end='\n\n')
    t = list_to_tree(a)
    print(t, end='\n\n')
    print("recursion in pre-order")
    print_tree_pre_order(t)
    print('\n')
    print("recursion in order")
    print_tree_in_order(t)
    print('\n')
    print("recursion in post-order")
    print_tree_in_post_order(t)
    print('\n')
    print("iteration in pre-order")
    print_tree_in_pre_order_iter(t)
    print('\n')
    print("iteration in order")
    print_tree_in_order_iter(t)
    print('\n')
    print("iteration in pre-order without stack")
    print_tree_in_pre_order_iter_no_stack(t)
    print('\n')
    print("iteration in order without stack")
    print_tree_in_order_iter_no_stack(t)
    print('\n')
