"""
K-th quantiles.
"""

import random

# Be aware of having a package with the same name
import selection


def kth_quantiles(array, k):
    """K-th quantiles."""
    if k == 1:
        return list()
    length = len(array)
    if not k % 2:
        mid = length // 2 if length % 2 else length // 2 - 1
        pivot = selection.select(array, mid + 1)
        selection.partition(array, pivot)
        return (kth_quantiles(array[:mid], k // 2)
                + [pivot]
                + kth_quantiles(array[mid + 1:], k // 2))
    low = (length * k - length - 1) // (2 * k)
    high = length - 1 - low
    left = selection.select(array, low + 1)
    right = selection.select(array, high + 1)
    selection.partition(array, left)
    left_quantiles = kth_quantiles(array[:low], k // 2)
    selection.partition(array, right)
    right_quantiles = kth_quantiles(array[high + 1:], k // 2)
    return left_quantiles + [left, right] + right_quantiles


def main():
    """The main function."""
    length = 100
    k = 10
    array = list(range(1, length))
    random.shuffle(array)
    print(array)
    print(kth_quantiles(array, k))


if __name__ == "__main__":
    main()
