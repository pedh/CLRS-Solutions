"""
Sort.
"""

import random


def insertion_sort(array):
    """Insertion sort."""
    length = len(array)
    for i in range(1, length):
        val = array[i]
        while i > 0 and array[i - 1] > val:
            array[i] = array[i - 1]
            i -= 1
        array[i] = val
    return array


def selection_sort(array):
    """Selection sort."""
    length = len(array)
    for i in range(length - 1):
        val = array[i]
        k = i
        for j in range(i + 1, length):
            if array[j] < val:
                k = j
                val = array[j]
        array[i], array[k] = array[k], array[i]
    return array


def merge_sort(array):
    """Merge sort."""
    def merge(array, left, mid, right):
        left_subarray = array[left: mid + 1]
        right_subarray = array[mid + 1: right + 1]
        j = 0
        k = 0
        for i in range(left, right + 1):
            if j > mid - left:
                array[i: right + 1] = right_subarray[k:]
                break
            elif k >= right - mid:
                array[i: right + 1] = left_subarray[j:]
                break
            if left_subarray[j] <= right_subarray[k]:
                array[i] = left_subarray[j]
                j += 1
            else:
                array[i] = right_subarray[k]
                k += 1

    def merge_rec(array, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        merge_rec(array, left, mid)
        merge_rec(array, mid + 1, right)
        merge(array, left, mid, right)

    merge_rec(array, 0, len(array) - 1)
    return array


def main():
    """The main function."""
    array = list(range(20))
    random.shuffle(array)
    print(array)
    insertion_sort(array)
    print(array)
    random.shuffle(array)
    print(array)
    selection_sort(array)
    print(array)
    random.shuffle(array)
    print(array)
    merge_sort(array)
    print(array)


if __name__ == "__main__":
    main()
