import random

# Be aware of having a package with the same name
import selection


def median(a):
    return selection.select(a, (len(a) + 1) // 2)


def select(a, i):
    pivot = median(a)
    k = selection.partition(a, pivot)
    if i == k + 1:
        return pivot
    if i < k + 1:
        return select(a[:k], i)
    return select(a[k + 1:], i - k - 1)


if __name__ == "__main__":
    n = 20
    a = list(range(1, n + 1))
    random.shuffle(a)
    print(a)
    i = random.randint(1, n)
    print("The %dth element is %d" % (i, select(a, i)))
