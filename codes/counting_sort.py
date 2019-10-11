"""
Counting sort.
"""

import random


def counting_sort_non_stable(array, key_length, key_func):
    """Non-stable counting sort."""
    counts = [0] * key_length
    result = [0] * len(array)
    for i in array:
        counts[key_func(i)] += 1
    for i in range(1, key_length):
        counts[i] += counts[i - 1]
    for i in range(len(array) - 1, -1, -1):
        key = key_func(array[i])
        result[counts[key] - 1] = array[i]
        counts[key] -= 1
    return result


def counting_sort(array, key_length, key_func):
    """Counting sort."""
    counts = [0] * key_length
    for i in array:
        counts[key_func(i)] += 1
    for i in range(1, key_length):
        counts[i] += counts[i - 1]
    i = len(array) - 1
    while i >= 0:
        key = key_func(array[i])
        pos = counts[key] - 1
        if i > pos:
            i -= 1
        else:
            array[i], array[pos] = array[pos], array[i]
            counts[key] -= 1


def main():
    """The main function."""
    array = list(range(20))
    random.shuffle(array)
    print(array)
    result = counting_sort_non_stable(array, 3, lambda i: i % 3)
    print(result)
    counting_sort(array, 3, lambda i: i % 3)
    print(array)


if __name__ == "__main__":
    main()
