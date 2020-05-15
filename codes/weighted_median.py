"""
Weighted median.
"""

import itertools
import random

# Be aware of having a package with the same name
import selection


def weighted_median_r(array, expect):
    """Weighted median recursion."""
    length = len(array)
    if length == 1:
        return array[0]
    mid = (length - 1) // 2
    pivot = selection.select(array, mid + 1)
    selection.partition(array, pivot)
    lsum = sum(array[:mid])
    if lsum < expect:
        if lsum + pivot >= expect:
            return pivot
        return weighted_median_r(array[mid + 1:],
                                 expect - lsum - pivot)
    return weighted_median_r(array[:mid], expect)


def weighted_median(array):
    """Weighted median."""
    return weighted_median_r(array, 0.5)


def main():
    """The main function."""
    array = [0.09, 0.35, 0.06, 0.11, 0.15, 0.04, 0.2]
    print(array)
    print(weighted_median(array))
    sorted_array = sorted(array)
    print(list(zip(sorted_array, itertools.accumulate(sorted_array))))


if __name__ == "__main__":
    main()
