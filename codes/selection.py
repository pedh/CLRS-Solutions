import random


def insertion_sort(a):
    for i in range(1, len(a)):
        x = a[i]
        while i > 0 and a[i - 1] > x:
            a[i] = a[i - 1]
            i -= 1
        a[i] = x


def partition(a, pivot):
    i = -1
    j = 0
    while j < len(a) - 1:
        if a[j] == pivot:
            a[-1], a[j] = a[j], a[-1]
            continue
        elif a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
        j += 1
    a[-1], a[i + 1] = a[i + 1], a[-1]
    return i + 1


def select(a, i):
    if len(a) == 1:
        return a[0]
    medians = list()
    for j in range(0, len(a), 5):
        group = a[j: j + 5]
        insertion_sort(group)
        medians.append(group[(len(group) - 1) // 2])
    pivot = select(medians, (len(medians) - 1) // 2 + 1)
    k = partition(a, pivot)
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
