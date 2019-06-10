import math
import random


def max_subarray(a):
    def max_cross_subarray(a, low, mid, high):
        left_sum = -math.inf
        llow = None
        sum = 0
        for i in range(mid, low - 1, -1):
            sum += a[i]
            if sum > left_sum:
                left_sum = sum
                llow = i
        right_sum = -math.inf
        rhigh = None
        sum = 0
        for i in range(mid + 1, high + 1):
            sum += a[i]
            if sum > right_sum:
                right_sum = sum
                rhigh = i
        return left_sum + right_sum, llow, rhigh
    def max_subarray_rc(a, low, high):
        if high - low == 0:
            return a[low], low, high
        mid = (low + high) // 2
        lsum, llow, lhigh = max_subarray_rc(a, low, mid)
        rsum, rlow, rhigh = max_subarray_rc(a, mid + 1, high)
        csum, clow, chigh = max_cross_subarray(a, low, mid, high)
        if lsum >= rsum and lsum >= csum:
            return lsum, llow, lhigh
        if rsum >= lsum and rsum >= csum:
            return rsum, rlow, rhigh
        return csum, clow, chigh
    return max_subarray_rc(a, 0, len(a) - 1)


def max_subarray_bf(a):
    la = len(a)
    max_sum = -math.inf
    low = high = None
    for i in range(la):
        sum = 0
        for j in range(i, la):
            sum += a[j]
            if sum > max_sum:
                low = i
                high = j
                max_sum = sum
    return max_sum, low, high


def mssl(a):
    low = high = clow = 0
    cur = best = a[0]
    for i in range(1, len(a)):
        if cur <= 0:
            clow = i
            cur = a[i]
        else:
            cur = cur + a[i]
        if cur > best:
            best = cur
            low = clow
            high = i
    return best, low, high


def test():
    a = [random.randint(-20, 20) for _ in range(20)]
    r1 = max_subarray(a)
    r2 = max_subarray_bf(a)
    r3 = mssl(a)
    if not (r1 == r2 == r3):
        print(a, r1, r2, r3)


if __name__ == "__main__":
    for _ in range(100):
        test()

