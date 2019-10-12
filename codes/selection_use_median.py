"""
Selection use a black-box median subroutine.
"""

import random

# Be aware of having a package with the same name
import selection


def median(array):
    """Black-box median."""
    return selection.select(array, (len(array) + 1) // 2)


def select(array, i):
    """Selection use median."""
    pivot = median(array)
    k = selection.partition(array, pivot)
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
