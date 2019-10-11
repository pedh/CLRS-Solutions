"""
Weighted median.
"""

import itertools

# Be aware of having a package with the same name
import selection


def weighted_median_r(array, total, expect):
    """Weighted median recursion."""
    length = len(array)
    if length == 1:
        return array[0]
    mid = (length - 1) // 2
    pivot = selection.select(array, mid + 1)
    selection.partition(array, pivot)
    lsum = 0
    for i in array[:mid]:
        lsum += i
    if lsum < expect:
        if lsum + pivot >= expect:
            return pivot
        return weighted_median_r(array[mid + 1:],
                                 total - lsum - pivot,
                                 expect - lsum - pivot)
    return weighted_median_r(array[:mid], total, lsum)


def weighted_median(array):
    """Weighted median."""
    return weighted_median_r(array, 1, 0.5)


def main():
    """The main function."""
    array = [0.09, 0.35, 0.06, 0.11, 0.15, 0.04, 0.2]
    print(array)
    print(weighted_median(array))
    print(list(itertools.accumulate(sorted(array))))


if __name__ == "__main__":
    main()
