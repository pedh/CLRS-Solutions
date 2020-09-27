"""
Binary tree.
"""


class Node:
    """Binary tree node."""
    def __init__(self, key, left=None, right=None, p=None):
        self._key = key
        self._left = left
        self._right = right
        self._p = p

    @property
    def key(self):
        """The key of the node."""
        return self._key

    @property
    def left(self):
        """The left child node."""
        return self._left

    @property
    def right(self):
        """The right child node."""
        return self._right

    @property
    def p(self):
        """The parent of the node"""
        return self._p

    @key.setter
    def key(self, key):
        self._key = key

    @left.setter
    def left(self, left):
        self._left = left

    @right.setter
    def right(self, right):
        self._right = right

    @p.setter
    def p(self, p):
        self._p = p

    def __repr__(self):
        return "(%s %s %s)" % (self.key, self.left, self.right)


class Stack:
    """LIFO Stack."""
    def __init__(self):
        self._lst = list()

    def is_empty(self):
        """Empty stack or not."""
        return not bool(self._lst)

    def pop(self):
        """Pop an element out from the top of the stack."""
        val = self._lst[-1]
        self._lst = self._lst[:-1]
        return val

    def push(self, val):
        """Push an element in the top of the stack."""
        self._lst.append(val)


def list_to_tree(lst, p=None):
    """Convert a list into a binary tree."""
    length = len(lst)
    if length == 0:
        return None
    if length == 1:
        return Node(lst[0], p=p)
    mid = (length - 1) // 2
    node = Node(lst[mid], p=p)
    node.left = list_to_tree(lst[:mid], p=node)
    node.right = list_to_tree(lst[mid + 1:], p=node)
    return node


def print_tree_pre_order(node):
    """Recursively binary tree pre-order traversal."""
    if not node:
        return
    print(node.key, end=' ')
    print_tree_pre_order(node.left)
    print_tree_pre_order(node.right)


def print_tree_in_order(node):
    """Recursively binary tree in-order traversal."""
    if not node:
        return
    print_tree_in_order(node.left)
    print(node.key, end=' ')
    print_tree_in_order(node.right)


def print_tree_in_post_order(node):
    """Recursively binary tree post-order traversal."""
    if not node:
        return
    print_tree_in_post_order(node.left)
    print_tree_in_post_order(node.right)
    print(node.key, end=' ')


def print_tree_in_pre_order_iter(node):
    """Iteratively binary tree pre-order traversal."""
    stack = Stack()
    stack.push(node)
    while not stack.is_empty():
        current = stack.pop()
        if current:
            print(current.key, end=' ')
            stack.push(current.right)
            stack.push(current.left)


def print_tree_in_order_iter(node):
    """Iteratively binary tree in-order traversal."""
    if not node:
        return
    stack = Stack()
    stack.push(node)
    while not stack.is_empty():
        current = stack.pop()
        while current:
            stack.push(current)
            current = current.left
        if not stack.is_empty():
            prev = stack.pop()
            print(prev.key, end=' ')
            stack.push(prev.right)


def print_tree_in_order_iter_no_stack(node):
    """Morris Traversal."""
    cur = node
    while cur:
        if not cur.left:
            print(cur.key, end=' ')
            cur = cur.right
        else:
            prev = cur.left
            while True:
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                    break
                elif prev.right == cur:
                    prev.right = None
                    print(cur.key, end=' ')
                    cur = cur.right
                    break
                prev = prev.right


def print_tree_in_pre_order_iter_no_stack(node):
    """Morris Traversal."""
    cur = node
    while cur:
        if not cur.left:
            print(cur.key, end=' ')
            cur = cur.right
        else:
            prev = cur.left
            while True:
                if not prev.right:
                    prev.right = cur
                    print(cur.key, end=' ')
                    cur = cur.left
                    break
                elif prev.right == cur:
                    prev.right = None
                    cur = cur.right
                    break
                prev = prev.right


def print_tree_in_order_iter_no_stack_with_parent(node):
    """Iteratively binary tree in-order traversal with parent, but no stack."""
    cur = node
    left_done = False
    while cur:
        if not left_done:
            while cur.left:
                cur = cur.left
            left_done = True
        print(cur.key, end=' ')
        if cur.right:
            cur = cur.right
            left_done = False
        else:
            while cur.p and cur == cur.p.right:
                cur = cur.p
            cur = cur.p


def main():
    """The main function."""
    length = 20
    lst = list(range(length))
    print(lst, end='\n\n')
    tree = list_to_tree(lst)
    print(tree, end='\n\n')
    print("recursion in pre-order")
    print_tree_pre_order(tree)
    print('\n')
    print("recursion in order")
    print_tree_in_order(tree)
    print('\n')
    print("recursion in post-order")
    print_tree_in_post_order(tree)
    print('\n')
    print("iteration in pre-order")
    print_tree_in_pre_order_iter(tree)
    print('\n')
    print("iteration in order")
    print_tree_in_order_iter(tree)
    print('\n')
    print("iteration in pre-order without stack")
    print_tree_in_pre_order_iter_no_stack(tree)
    print('\n')
    print("iteration in order without stack")
    print_tree_in_order_iter_no_stack(tree)
    print('\n')
    print("iteration in order using parent, without stack")
    print_tree_in_order_iter_no_stack_with_parent(tree)
    print('\n')


if __name__ == "__main__":
    main()
