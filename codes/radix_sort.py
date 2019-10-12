"""
Radix sort.
"""

import random
import string

DEC = 10


def radix_sort(array, k):
    """LSD radix sort."""

    def kth_digit(num, k):
        return num // DEC ** k % DEC

    def counting_sort(array, k):
        count_lst = [0] * DEC
        for i in array:
            count_lst[kth_digit(i, k)] += 1
        for i in range(1, DEC):
            count_lst[i] += count_lst[i - 1]
        result = [None] * len(array)
        for i in range(len(array) - 1, -1, -1):
            digit = kth_digit(array[i], k)
            result[count_lst[digit] - 1] = array[i]
            count_lst[digit] -= 1
        return result

    for i in range(k):
        array = counting_sort(array, i)
    return array


def lexicographic_order(array):
    """MSD radix sort."""

    def lex_r(array, k):
        buckets = [[] for _ in range(27)]
        for elem in array:
            if not k < len(elem):
                buckets[0].append(elem)
            else:
                buckets[ord(elem[k]) - ord('a') + 1].append(elem)
        for i in range(1, 27):
            if len(buckets[i]) > 1:
                buckets[i] = lex_r(buckets[i], k + 1)
        result = []
        for bucket in buckets:
            result += bucket
        return result
    return lex_r(array, 0)


def random_string():
    """Generate random string."""
    return ''.join(random.choice(string.ascii_lowercase)
                   for _ in range(random.randint(1, 10)))


def main():
    """The main function."""
    array = [random.randint(100, 999) for _ in range(20)]
    print(array)
    print(radix_sort(array, 3))
    str_array = [random_string() for _ in range(100)]
    print(str_array)
    print(lexicographic_order(str_array))


if __name__ == "__main__":
    main()
