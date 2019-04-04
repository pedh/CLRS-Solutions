import random


def count_sort(a, k, f):
    c = [0] * k
    b = [0] * len(a)
    for i in a:
        c[f(i)] += 1
    for i in range(1, k):
        c[i] = c[i] + c[i - 1]
    for i in range(len(a) - 1, -1, -1):
        x = f(a[i])
        b[c[x] - 1] = a[i]
        c[x] -= 1
    return b


if __name__ == "__main__":
    a = list(range(20))
    random.shuffle(a)
    print(a)
    b = count_sort(a, 3, lambda i: i % 3)
    print(b)

