# pylint: disable=too-few-public-methods

"""
Singly linked list reverse.
"""


class Node:
    """Singly linked list node."""
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    @property
    def data(self):
        """Node data."""
        return self._data

    @property
    def next(self):
        """Next node."""
        return self._next

    @data.setter
    def data(self, value):
        self._data = value

    @next.setter
    def next(self, value):
        self._next = value


class LinkedList:
    """Singly linked list."""
    def __init__(self, head=None):
        self._head = head

    @property
    def head(self):
        """Linked list head."""
        return self._head

    @head.setter
    def head(self, value):
        self._head = value


def print_linked_list(linked_list):
    """Print linked list."""
    curr = linked_list.head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()


def linked_list_reverse(linked_list):
    """Linked list reverse."""
    curr = linked_list.head
    if not curr:
        return linked_list
    nxt = curr.next
    curr.next = None
    while nxt:
        new_nxt = nxt.next
        nxt.next = curr
        curr = nxt
        nxt = new_nxt
    linked_list.head = curr


def main():
    """The main function."""
    head = curr = Node(0)
    for i in range(1, 20):
        curr.next = Node(i)
        curr = curr.next
    linked_list = LinkedList(head)
    print_linked_list(linked_list)
    linked_list_reverse(linked_list)
    print_linked_list(linked_list)


if __name__ == "__main__":
    main()
