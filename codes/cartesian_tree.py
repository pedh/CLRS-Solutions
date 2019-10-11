"""
Cartesian tree.
"""

import random


class Node:
    """Cartesian tree node."""
    def __init__(self, parent, left, right, data):
        self._parent = parent
        self._left = left
        self._right = right
        self._data = data

    @property
    def parent(self):
        """The parent node."""
        return self._parent

    @property
    def left(self):
        """The left child node."""
        return self._left

    @property
    def right(self):
        """The right child node."""
        return self._right

    @property
    def data(self):
        """The data of the node."""
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


def cartesian_tree_insert(cur, root, val):
    """Insert an element into the cartesian tree."""
    if cur.data < val:
        new = Node(cur, None, None, val)
        cur.right = new
        return new, root
    while cur.parent:
        if cur.parent.data < val:
            new = Node(cur.parent, cur, None, val)
            cur.parent.right = new
            cur.parent = new
            return new, root
        cur = cur.parent
    new = Node(None, cur, None, val)
    cur.parent = new
    return new, new


def cartesian_tree(array):
    """Generate a cartesian tree from an array of elements."""
    if not array:
        return None
    cur = Node(None, None, None, array[0])
    nodes = [cur]
    root = cur
    for val in array[1:]:
        cur, root = cartesian_tree_insert(cur, root, val)
        nodes.append(cur)
    return root, nodes


def cartesian_tree_lca(node1, node2):
    """Lowest common ancestor of two nodes."""
    while node1 and node2:
        if node1 == node2:
            return node1
        if node1.data > node2.data:
            node1 = node1.parent
        else:
            node2 = node2.parent
    return None


def range_minimum_query(nodes, low, high):
    """Range minimum query using cartesian tree."""
    lca = cartesian_tree_lca(nodes[low], nodes[high])
    return lca.data if lca else None


def main():
    """The main function."""
    length = 20
    array = list(range(length))
    random.shuffle(array)
    print(array, end='\n\n')
    tree, nodes = cartesian_tree(array)
    print(tree)
    for _ in range(10):
        low = random.randint(0, length - 2)
        high = random.randint(low + 1, length - 1)
        print(low, high)
        print(range_minimum_query(nodes, low, high))
        sub = array[low: high + 1]
        print(min(sub), sub, end='\n\n')


if __name__ == "__main__":
    main()
