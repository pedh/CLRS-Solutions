"""
Maximum subarray.
"""

import math
import random
import time


def max_cross_subarray(array, low, mid, high):
    """Maximum subarray cross the middle."""
    left_max_sum = -math.inf
    llow = None
    left_sum = 0
    for i in range(mid, low - 1, -1):
        left_sum += array[i]
        if left_sum > left_max_sum:
            left_max_sum = left_sum
            llow = i
    right_max_sum = -math.inf
    rhigh = None
    right_sum = 0
    for i in range(mid + 1, high + 1):
        right_max_sum += array[i]
        if right_sum > right_max_sum:
            right_max_sum = right_sum
            rhigh = i
    return llow, rhigh, left_max_sum + right_max_sum


def max_subarray_rc(array, low, high):
    """Maximum subarray recursion."""
    if high - low == 0:
        return low, high, array[low]
    mid = (low + high) // 2
    llow, lhigh, lsum = max_subarray_rc(array, low, mid)
    rlow, rhigh, rsum = max_subarray_rc(array, mid + 1, high)
    clow, chigh, csum = max_cross_subarray(array, low, mid, high)
    if lsum >= rsum and lsum >= csum:
        return llow, lhigh, lsum
    if rsum >= lsum and rsum >= csum:
        return rlow, rhigh, rsum
    return clow, chigh, csum


def max_subarray(array):
    """Maximum subarray."""
    return max_subarray_rc(array, 0, len(array) - 1)


def max_subarray_bf(array):
    """Maximum subarray brute-force."""
    length = len(array)
    max_sum = -math.inf
    low = high = None
    for i in range(length):
        curr_sum = 0
        for j in range(i, length):
            curr_sum += array[j]
            if curr_sum > max_sum:
                low = i
                high = j
                max_sum = curr_sum
    return low, high, max_sum


def maximum_subarray_linear(array):
    """Maximum subarray linear."""
    if not array:
        return None, None, None
    i = low = high = 0
    curr = max_sum = array[0]
    for j in range(1, len(array)):
        if curr < 0:
            i = j
            curr = array[j]
        else:
            curr += array[j]
        if curr > max_sum:
            max_sum = curr
            low = i
            high = j
    return low, high, max_sum


def time_profile(func, *args, **kwargs):
    """Time profile helper."""
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    return elapsed, result


def crossover_point():
    """Get crossover point of recursion solution and brute-force."""
    for i in range(2, 100):
        array = [random.randint(-20, 20) for _ in range(i)]
        time1, _ = time_profile(max_subarray, array)
        time2, _ = time_profile(max_subarray_bf, array)
        if time1 < time2:
            return i
    return None


def max_subarray_rc_optimized(array, low, high, cpoint):
    """Maximum subarray recursion optimized."""
    if high - low == 0:
        return array[low], low, high
    if high - low < cpoint:
        return max_subarray_bf(array[low: high + 1])
    mid = (low + high) // 2
    llow, lhigh, lsum = max_subarray_rc_optimized(array, low, mid, cpoint)
    rlow, rhigh, rsum = max_subarray_rc_optimized(array, mid + 1, high, cpoint)
    clow, chigh, csum = max_cross_subarray(array, low, mid, high)
    if lsum >= rsum and lsum >= csum:
        return llow, lhigh, lsum
    if rsum >= lsum and rsum >= csum:
        return rlow, rhigh, rsum
    return clow, chigh, csum


def max_subarray_optimized(array, cpoint):
    """Maximum subarray optimized."""
    return max_subarray_rc_optimized(array, 0, len(array) - 1, cpoint)


def new_crossover_point(cpoint):
    """Get new crossover point."""
    for i in range(2, 100):
        array = [random.randint(-20, 20) for _ in range(i)]
        time1, _ = time_profile(max_subarray_optimized, array, cpoint)
        time2, _ = time_profile(max_subarray_bf, array)
        if time1 < time2:
            return i
    return None


def test_crossover():
    """Test crossover."""
    cpoint = crossover_point()
    print("The crossover point which recursive algotithm "
          "beats brute-force algorithm is:", cpoint)
    array = [random.randint(-20, 20) for _ in range(40)]
    print(time_profile(max_subarray, array))
    print(time_profile(max_subarray_optimized, array, cpoint))
    print("The new crossover point is:", new_crossover_point(cpoint))


def main():
    """The main function."""
    # test_crossover()
    array = [random.randint(-20, 20) for _ in range(20)]
    print(array)
    print(maximum_subarray_linear(array))


if __name__ == "__main__":
    main()
