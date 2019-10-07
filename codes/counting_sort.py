import random


def counting_sort(a, k, f):
    c = [0] * k
    b = [0] * len(a)
    for i in a:
        c[f(i)] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    for i in range(len(a) - 1, -1, -1):
        x = f(a[i])
        b[c[x] - 1] = a[i]
        c[x] -= 1
    return b


def counting_sort_in_place(a, k, f):
    c = [0] * k
    for i in a:
        c[f(i)] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    i = len(a) - 1
    while i >= 0:
        x = f(a[i])
        pos = c[x] - 1
        if i > pos:
            i -= 1
        else:
            a[i], a[pos] = a[pos], a[i]
            c[x] -= 1


if __name__ == "__main__":
    a = list(range(20))
    random.shuffle(a)
    print(a)
    b = counting_sort(a, 3, lambda i: i % 3)
    print(b)
    counting_sort_in_place(a, 3, lambda i: i % 3)
    print(a)
