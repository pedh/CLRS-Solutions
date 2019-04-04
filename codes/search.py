import random
import sys


def binary_search(lst, x):
    lst = sorted(lst)
    i = 0
    j = len(lst) - 1
    while i < j:
        mid = (i + j) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            i = mid + 1
        else:
            j = mid - 1


def linear_search(lst, x):
    le = len(lst)
    for i in range(le):
        if lst[i] == x:
            return i


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        sys.exit(1)
    func = globals().get(args[1])
    if not func:
        sys.exit(1)
    lst = list(range(10))
    random.shuffle(lst)
    print(lst)
    for i in range(5):
        x = random.randint(0, 20)
        print(x, func(lst, x))
