"""
Generate unbiased random from biased random.
"""

import random


def biased_random():
    """Biased random generator."""
    val = random.randint(1, 4)
    return val >> 2


def unbiased_random():
    """Unbiased random generator."""
    while True:
        rand1 = biased_random()
        rand2 = biased_random()
        if rand1 > rand2:
            return 1
        if rand1 < rand2:
            return 0


def main():
    """The main function."""
    length = 100
    count = 0
    for _ in range(length):
        val = biased_random()
        if val == 1:
            count += 1
    print(count)
    count = 0
    for _ in range(length):
        val = unbiased_random()
        if val == 1:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
