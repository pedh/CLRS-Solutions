class Node(object):
    def __init__(self, data, next_node=None):
        self._data = data
        self._nxt = next_node

    @property
    def data(self):
        return self._data

    @property
    def nxt(self):
        return self._nxt

    @data.setter
    def data(self, value):
        self._data = value

    @nxt.setter
    def nxt(self, value):
        self._nxt = value


class LinkedList(object):
    def __init__(self, head=None):
        self._head = head

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value


def print_linked_list(ll):
    x = ll.head
    while x:
        print(x.data, end=' ')
        x = x.nxt
    print()


def linked_list_reverse(ll):
    x = ll.head
    if not x:
        return ll
    y = x.nxt
    x.nxt = None
    while y:
        ny = y.nxt
        y.nxt = x
        x = y
        y = ny
    ll.head = x


if __name__ == "__main__":
    head = x = Node(0)
    for i in range(1, 20):
        x.nxt = Node(i)
        x = x.nxt
    ll = LinkedList(head)
    print_linked_list(ll)
    linked_list_reverse(ll)
    print_linked_list(ll)
