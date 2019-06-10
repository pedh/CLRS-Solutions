import random


class Node(object):
    def __init__(self, parent, left, right, data):
        self._parent = parent
        self._left = left
        self._right = right
        self._data = data

    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def data(self):
        return self._data

    @parent.setter
    def parent(self, value):
        self._parent = value

    @left.setter
    def left(self, value):
        self._left = value

    @right.setter
    def right(self, value):
        self._right = value

    @data.setter
    def data(self, value):
        self._data = value

    def __repr__(self):
        return "(%s %s %s)" % (self.data, self.left, self.right)


def cartesian_tree_insert(cn, root, x):
    if cn.data < x:
        nn = Node(cn, None, None, x)
        cn.right = nn
        return nn, root
    while cn.parent:
        if cn.parent.data < x:
            nn = Node(cn.parent, cn, None, x)
            cn.parent.right = nn
            cn.parent = nn
            return nn, root
        cn = cn.parent
    nn = Node(None, cn, None, x)
    cn.parent = nn
    return nn, nn


def cartesian_tree(a):
    if len(a) < 1:
        return None
    cn = Node(None, None, None, a[0])
    cta = [cn]
    root = cn
    for x in a[1:]:
        cn, root = cartesian_tree_insert(cn, root, x)
        cta.append(cn)
    return root, cta


def cartesian_tree_lca(n1, n2):
    while n1 and n2:
        if n1 == n2:
            return n1
        elif n1.data > n2.data:
            n1 = n1.parent
        else:
            n2 = n2.parent
    return None


def range_minimum_query(cta, low, high):
    lca = cartesian_tree_lca(cta[low], cta[high])
    return lca.data if lca else lca


if __name__ == "__main__":
    n = 20
    a = list(range(20))
    random.shuffle(a)
    print(a, end='\n\n')
    ct, cta = cartesian_tree(a)
    # print(ct)
    for _ in range(10):
        low = random.randint(0, n - 2)
        high = random.randint(low + 1, n - 1)
        print(low, high)
        print(range_minimum_query(cta, low, high))
        slice = a[low: high + 1]
        print(min(slice), slice, end='\n\n')
