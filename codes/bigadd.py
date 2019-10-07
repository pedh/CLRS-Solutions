import copy
import random


MAX_LENGTH = 100
MIN_LENGTH = 10


class BigInt(object):
    def __init__(self, lst):
        self.lst = lst

    def __repr__(self):
        return "".join(str(i) for i in self.lst)

    def __add__(self, au):
        a = copy.deepcopy(self.lst)
        b = copy.deepcopy(au.lst)
        la = len(a)
        lb = len(b)
        n = max(la, lb)
        a += [0] * (n - la)
        b += [0] * (n - lb)
        s = []
        z = 0
        for i in range(n):
            k, z = bitadd(a[i], b[i], z)
            s.append(k)
        if z > 0:
            s.append(z)
        return BigInt(s)

    @property
    def value(self):
        m = 1
        v = 0
        for i in self.lst:
            v += i * m
            m <<= 1
        return v


def bitadd(x, y, z):
    s = x + y + z
    return s % 2, s // 2


def randbit():
    return random.randint(0, 1)


def randbig():
    le = random.randint(MIN_LENGTH, MAX_LENGTH)
    lst = [randbit() for i in range(le)]
    lst[-1] = 1
    return BigInt(lst)


if __name__ == "__main__":
    a = randbig()
    b = randbig()
    c = a + b
    print(a)
    print(b)
    print(c)
    print(a.value)
    print(b.value)
    print(c.value)
    print(a.value + b.value == c.value)
