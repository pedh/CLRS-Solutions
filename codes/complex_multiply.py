import random


def cm(a, b, c, d):
    s1 = (a - b) * (c + d)
    s2 = (a + b) * (c - d)
    s3 = b * c
    p1 = (s1 + s2) / 2
    p2 = (s1 - p1) + 2 * s3
    return p1, p2


if __name__ == "__main__":
    a, b, c, d = (random.randint(-10, 10) for _ in range(4))
    print(a, b, c, d)
    p1, p2 = cm(a, b, c, d)
    print(p1, p2)
    print(a * c - b * d, a * d + b * c)
