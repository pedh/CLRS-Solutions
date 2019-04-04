import random


def max_heapify(a, i, hs):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= hs and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= hs and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest, hs)


def build_max_heap(a, hs):
    for i in range(len(a) // 2, -1, -1):
        max_heapify(a, i, hs)


def heapsort(a):
    hs = len(a) - 1
    build_max_heap(a, hs)
    print(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        hs -= 1
        max_heapify(a, 0, hs)


if __name__ == "__main__":
    a = list(range(20))
    random.shuffle(a)
    print(a)
    heapsort(a)
    print(a)
    
