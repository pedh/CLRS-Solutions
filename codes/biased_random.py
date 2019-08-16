import random


def biased_random():
    v = random.randint(1, 4)
    return v >> 2


def unbiased_random():
    while True:
        x = biased_random()
        y = biased_random()
        if x > y:
            return 1
        if x < y:
            return 0


if __name__ == "__main__":
    n = 100
    c = 0
    for _ in range(n):
        v = biased_random()
        if v == 1:
            c += 1
    print(c)
    c = 0
    for _ in range(n):
        v = unbiased_random()
        if v == 1:
            c += 1
    print(c)
