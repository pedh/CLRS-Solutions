"""
Search.
"""

import random


def binary_search(array, val):
    """Binary search."""
    sorted_array = sorted(array)
    i = 0
    j = len(array) - 1
    while i <= j:
        mid = (i + j) // 2
        if sorted_array[mid] == val:
            return mid
        if sorted_array[mid] < val:
            i = mid + 1
        else:
            j = mid - 1


def linear_search(array, val):
    """Linear search."""
    length = len(array)
    for i in range(length):
        if array[i] == val:
            return i
    return None


def main():
    """The main function."""
    array = list(range(10))
    print(array)
    for _ in range(5):
        val = random.randint(0, 20)
        print(val, binary_search(array, val))
    random.shuffle(array)
    print(array)
    for _ in range(5):
        val = random.randint(0, 20)
        print(val, linear_search(array, val))


if __name__ == "__main__":
    main()
