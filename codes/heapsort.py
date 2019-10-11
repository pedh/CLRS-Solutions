"""
Heapsort.
"""

import random


def max_heapify(heap, index, heap_size):
    """Max-heapify."""
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and heap[left_index] > heap[index]:
        largest = left_index
    else:
        largest = index
    if right_index < heap_size and heap[right_index] > heap[largest]:
        largest = right_index
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        max_heapify(heap, largest, heap_size)


def build_max_heap(heap, heap_size):
    """Build max heap."""
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(heap, i, heap_size)


def heapsort(heap):
    """Heapsort."""
    heap_size = len(heap)
    build_max_heap(heap, heap_size)
    print(heap)
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heap_size -= 1
        max_heapify(heap, 0, heap_size)


def main():
    """The main function."""
    array = list(range(20))
    random.shuffle(array)
    print(array)
    heapsort(array)
    print(array)


if __name__ == "__main__":
    main()
