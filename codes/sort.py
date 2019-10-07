import random
import sys


def insertion_sort(lst):
    le = len(lst)
    for i in range(1, le):
        k = lst[i]
        while i > 0 and lst[i - 1] > k:
            lst[i] = lst[i - 1]
            i -= 1
        lst[i] = k
    return lst


def selection_sort(lst):
    le = len(lst)
    for i in range(le - 1):
        v = lst[i]
        k = i
        for j in range(i + 1, le):
            if lst[j] < v:
                k = j
                v = lst[j]
        lst[i], lst[k] = lst[k], lst[i]
    return lst


def merge_sort(a):
    def merge(a, p, q, r):
        ll = a[p: q + 1]
        lr = a[q + 1: r + 1]
        j = 0
        k = 0
        for i in range(p, r + 1):
            if j > q - p:
                a[i: r + 1] = lr[k:]
                break
            elif k >= r - q:
                a[i: r + 1] = ll[j:]
                break
            if ll[j] <= lr[k]:
                a[i] = ll[j]
                j += 1
            else:
                a[i] = lr[k]
                k += 1

    def merge_rec(a, p, r):
        if p >= r:
            return a
        q = (p + r) // 2
        merge_rec(a, p, q)
        merge_rec(a, q + 1, r)
        merge(a, p, q, r)
    a = merge_rec(a, 0, len(a) - 1)
    return a


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        sys.exit(1)
    func = globals().get(args[1])
    if not func:
        sys.exit(1)
    lst = list(range(20))
    random.shuffle(lst)
    print(lst)
    func(lst)
    print(lst)
