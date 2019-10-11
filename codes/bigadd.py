"""
Big integer arithmetic.
"""

import copy
import random


MAX_LENGTH = 100
MIN_LENGTH = 10


class BigInt:
    """Big integer."""

    def __init__(self, lst):
        self.lst = lst

    def __repr__(self):
        return "".join(str(i) for i in self.lst)

    def __add__(self, addend):
        aug_lst = copy.deepcopy(self.lst)
        add_lst = copy.deepcopy(addend.lst)
        len_aug = len(aug_lst)
        len_add = len(add_lst)
        max_len = max(len_aug, len_add)
        aug_lst += [0] * (max_len - len_aug)
        add_lst += [0] * (max_len - len_add)
        sum_lst = []
        carry = 0
        for i in range(max_len):
            bit, carry = bitadd(aug_lst[i], add_lst[i], carry)
            sum_lst.append(bit)
        if carry > 0:
            sum_lst.append(carry)
        return BigInt(sum_lst)

    @property
    def value(self):
        """Actual integer value."""
        base = 1
        val = 0
        for i in self.lst:
            val += i * base
            base <<= 1
        return val


def bitadd(augend, addend, carry):
    """Binary addition."""
    val = augend + addend + carry
    return val % 2, val // 2


def randbit():
    """Generate random bit."""
    return random.randint(0, 1)


def randbig():
    """Generate random big integer."""
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    lst = [randbit() for i in range(length)]
    lst[-1] = 1
    return BigInt(lst)


def main():
    """The main function."""
    augend = randbig()
    addend = randbig()
    result = augend + addend
    print(augend)
    print(addend)
    print(result)
    print(augend.value)
    print(addend.value)
    print(result.value)
    print(augend.value + addend.value == result.value)


if __name__ == "__main__":
    main()
