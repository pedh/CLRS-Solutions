"""
Quicksort.
"""

import random


def partition(array, left, right):
    """Quicksort partition."""
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[right], array[i + 1] = array[i + 1], array[right]
    return i + 1


def quicksort_r(array, left, right):
    """Quicksort recursion."""
    if right > left:
        pivot_i = partition(array, left, right)
        quicksort_r(array, left, pivot_i - 1)
        quicksort_r(array, pivot_i + 1, right)


def quicksort(array):
    """Quicksort."""
    quicksort_r(array, 0, len(array) - 1)


def main():
    """The main function."""
    array = list(range(20))
    random.shuffle(array)
    print(array)
    quicksort(array)
    print(array)


if __name__ == "__main__":
    main()
