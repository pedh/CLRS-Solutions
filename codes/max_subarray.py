import math
import random
import time


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
    return llow, rhigh, left_sum + right_sum


def max_subarray_rc(a, low, high):
    if high - low == 0:
        return low, high, a[low]
    mid = (low + high) // 2
    llow, lhigh, lsum = max_subarray_rc(a, low, mid)
    rlow, rhigh, rsum = max_subarray_rc(a, mid + 1, high)
    clow, chigh, csum = max_cross_subarray(a, low, mid, high)
    if lsum >= rsum and lsum >= csum:
        return llow, lhigh, lsum
    if rsum >= lsum and rsum >= csum:
        return rlow, rhigh, rsum
    return clow, chigh, csum


def max_subarray(a):
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
    return low, high, max_sum


def maximum_subarray_linear(a):
    if not a:
        return
    i = low = high = 0
    c = s = a[0]
    for j in range(1, len(a)):
        if c < 0:
            i = j
            c = a[j]
        else:
            c += a[j]
        if c > s:
            s = c
            low = i
            high = j
    return low, high, s


def time_profile(f, *args, **kwargs):
    start = time.time()
    result = f(*args, **kwargs)
    elapsed = time.time() - start
    return elapsed, result


def crossover_point():
    for i in range(2, 100):
        a = [random.randint(-20, 20) for _ in range(i)]
        t1, result = time_profile(max_subarray, a)
        t2, result = time_profile(max_subarray_bf, a)
        if t1 < t2:
            return i


def max_subarray_rc_optimized(a, low, high, n0):
    if high - low == 0:
        return a[low], low, high
    if high - low < n0:
        return max_subarray_bf(a[low: high + 1])
    mid = (low + high) // 2
    llow, lhigh, lsum = max_subarray_rc_optimized(a, low, mid, n0)
    rlow, rhigh, rsum = max_subarray_rc_optimized(a, mid + 1, high, n0)
    clow, chigh, csum = max_cross_subarray(a, low, mid, high)
    if lsum >= rsum and lsum >= csum:
        return llow, lhigh, lsum
    if rsum >= lsum and rsum >= csum:
        return rlow, rhigh, rsum
    return clow, chigh, csum


def max_subarray_optimized(a, n0):
    return max_subarray_rc_optimized(a, 0, len(a) - 1, n0)


def new_crossover_point(n0):
    for i in range(2, 100):
        a = [random.randint(-20, 20) for _ in range(i)]
        t1, result = time_profile(max_subarray_optimized, a, n0)
        t2, result = time_profile(max_subarray_bf, a)
        if t1 < t2:
            return i


def test_crossover():
    n0 = crossover_point()
    print("The crossover point which recursive algotithm "
          "beats brute-force algorithm is:", n0)
    n = 40
    a = [random.randint(-20, 20) for _ in range(n)]
    print(time_profile(max_subarray, a))
    print(time_profile(max_subarray_optimized, a, n0))
    print("The new crossover point is:", new_crossover_point(n0))


if __name__ == "__main__":
    # test_crossover()
    a = [random.randint(-20, 20) for _ in range(20)]
    print(a)
    print(maximum_subarray_linear(a))
