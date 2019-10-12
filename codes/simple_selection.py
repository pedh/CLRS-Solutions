"""
Simple selection.
"""

import random


def partition(array, left, right):
    """Selection partition."""
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[right], array[i + 1] = array[i + 1], array[right]
    return i + 1


def select_r(array, left, right, i):
    """Selection recursion."""
    if left == right:
        return array[left]
    pivot_i = partition(array, left, right)
    k = pivot_i - left + 1
    if i == k:
        return array[pivot_i]
    if i < k:
        return select_r(array, left, pivot_i - 1, i)
    return select_r(array, pivot_i + 1, right, i - k)


def select(array, i):
    """Selection."""
    return select_r(array, 0, len(array) - 1, i)


def main():
    """The main function."""
    length = 20
    array = list(range(1, length + 1))
    random.shuffle(array)
    print(array)
    i = random.randint(1, length)
    print("The %dth element is %d" % (i, select(array, i)))


if __name__ == "__main__":
    main()
