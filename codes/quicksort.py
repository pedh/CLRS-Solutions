import random


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[r], a[i + 1] = a[i + 1], a[r]
    return i + 1


def quicksort_r(a, p, r):
    if r > p:
        q = partition(a, p, r)
        quicksort_r(a, p, q - 1)
        quicksort_r(a, q + 1, r)


def quicksort(a):
    quicksort_r(a, 0, len(a) - 1)


if __name__ == "__main__":
    a = list(range(20))
    random.shuffle(a)
    print(a)
    quicksort(a)
    print(a)
