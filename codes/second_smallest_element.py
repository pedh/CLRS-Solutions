"""
Second smallest element.
"""

import math
import random

# Be aware of having a package with the same name
import binary_tree


Node = binary_tree.Node


def second_smallest_element(array):
    """Second smallest element"""
    length = len(array)
    if length < 2:
        return None
    nodes = [Node(i) for i in array]
    while length > 1:
        new_nodes = list()
        for i in range(0, length - 1, 2):
            left = nodes[i]
            right = nodes[i + 1]
            key = left.key
            if right.key < key:
                key = right.key
            new_nodes.append(Node(key, left, right))
        if length % 2:
            node = nodes[-1]
            new_nodes.append(Node(node.key, node))
        nodes = new_nodes
        length = len(nodes)
    node = nodes[0]
    key = node.key
    second_smallest = math.inf
    while node.left and node.right:
        if node.left.key == key:
            if node.right.key < second_smallest:
                second_smallest = node.right.key
            node = node.left
        else:
            if node.left.key < second_smallest:
                second_smallest = node.left.key
            node = node.right
    return second_smallest


def main():
    """The main function."""
    array = list(range(20))
    random.shuffle(array)
    print(array)
    print("second smallest element is %d" % second_smallest_element(array))


if __name__ == "__main__":
    main()
