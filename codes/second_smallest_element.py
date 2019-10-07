import math
import random


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def second_smallest_element(a):
    ln = len(a)
    if ln < 2:
        return
    nodes = [Node(i) for i in a]
    while ln > 1:
        new_nodes = list()
        for i in range(0, ln - 1, 2):
            left = nodes[i]
            right = nodes[i + 1]
            value = left.value
            if right.value < value:
                value = right.value
            new_nodes.append(Node(value, left, right))
        if ln % 2:
            node = nodes[-1]
            new_nodes.append(Node(node.value, node))
        nodes = new_nodes
        ln = len(nodes)
    node = nodes[0]
    nv = node.value
    sv = math.inf
    while node.left and node.right:
        if node.left.value == nv:
            if node.right.value < sv:
                sv = node.right.value
            node = node.left
        else:
            if node.left.value < sv:
                sv = node.left.value
            node = node.right
    return sv


if __name__ == "__main__":
    a = list(range(20))
    random.shuffle(a)
    print(a)
    print("second smallest element is %d" % second_smallest_element(a))
