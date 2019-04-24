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


def select_r(a, p, r, i):
    if p == r:
        return a[p]
    q = partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return select_r(a, p, q - 1, i)
    return select_r(a, q + 1, r, i - k)


def select(a, i):
    return select_r(a, 0, len(a) - 1, i)


if __name__ == "__main__":
    n = 20
    a = list(range(1, n + 1))
    random.shuffle(a)
    print(a)
    i = random.randint(1, n)
    print("The %dth element is %d" %(i, select(a, i)))
