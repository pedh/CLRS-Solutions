"""
Selection.
"""

import random


def insertion_sort(array):
    """Insertion sort."""
    for i in range(1, len(array)):
        val = array[i]
        while i > 0 and array[i - 1] > val:
            array[i] = array[i - 1]
            i -= 1
        array[i] = val


def partition(array, pivot):
    """Selection partition."""
    i = -1
    j = 0
    while j < len(array) - 1:
        if array[j] == pivot:
            array[-1], array[j] = array[j], array[-1]
            continue
        elif array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[-1], array[i + 1] = array[i + 1], array[-1]
    return i + 1


def select(array, i):
    """Selection."""
    if len(array) == 1:
        return array[0]
    medians = list()
    for j in range(0, len(array), 5):
        group = array[j: j + 5]
        insertion_sort(group)
        medians.append(group[(len(group) - 1) // 2])
    pivot = select(medians, (len(medians) - 1) // 2 + 1)
    k = partition(array, pivot)
    if i == k + 1:
        return pivot
    if i < k + 1:
        return select(array[:k], i)
    return select(array[k + 1:], i - k - 1)


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
