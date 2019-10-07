import random

# Be aware of having a package with the same name
import selection


def kth_quantiles(a, k):
    if k == 1:
        return list()
    n = len(a)
    if not k % 2:
        i = n // 2 if n % 2 else n // 2 - 1
        median = selection.select(a, i + 1)
        selection.partition(a, median)
        return (kth_quantiles(a[:i], k // 2)
                + [median]
                + kth_quantiles(a[i + 1:], k // 2))
    i = (n * k - n - 1) // (2 * k)
    j = n - 1 - i
    left = selection.select(a, i + 1)
    right = selection.select(a, j + 1)
    selection.partition(a, left)
    left_quantiles = kth_quantiles(a[:i], k // 2)
    selection.partition(a, right)
    right_quantiles = kth_quantiles(a[j + 1:], k // 2)
    return left_quantiles + [left, right] + right_quantiles


if __name__ == "__main__":
    n = 99
    k = 10
    a = list(range(1, n + 1))
    random.shuffle(a)
    print(a)
    print(kth_quantiles(a, k))
