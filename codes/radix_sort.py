import random
import string

DEC = 10


def radix_sort(a, k):
    """LSD radix sort"""
    def nth_digit(x, n):
        return x // DEC ** n % DEC

    def counting_sort(a, d):
        c = [0] * DEC
        for i in a:
            c[nth_digit(i, d)] += 1
        for i in range(1, DEC):
            c[i] += c[i - 1]
        b = [None] * len(a)
        for i in range(len(a) - 1, -1, -1):
            di = nth_digit(a[i], d)
            b[c[di] - 1] = a[i]
            c[di] -= 1
        return b
    for i in range(k):
        a = counting_sort(a, i)
    return a


def lexicographic_order(a):
    """MSD radix sort"""
    def lex_r(a, k):
        bts = [[] for _ in range(27)]
        for el in a:
            if not k < len(el):
                bts[0].append(el)
            else:
                bts[ord(el[k]) - ord('a') + 1].append(el)
        for i in range(1, 27):
            if len(bts[i]) > 1:
                bts[i] = lex_r(bts[i], k + 1)
        b = []
        for bt in bts:
            b += bt
        return b
    return lex_r(a, 0)


def random_string():
    return ''.join(random.choice(string.ascii_lowercase)
                   for _ in range(random.randint(1, 10)))


if __name__ == "__main__":
    a = [random.randint(100, 999) for _ in range(20)]
    print(a)
    print(radix_sort(a, 3))
    s = [random_string() for _ in range(100)]
    print(s)
    print(lexicographic_order(s))
