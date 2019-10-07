import itertools

# Be aware of having a package with the same name
import selection


def weighted_median(a):
    return weighted_median_r(a, 1, 0.5)


def weighted_median_r(a, x, y):
    n = len(a)
    if n == 1:
        return a[0]
    m = (n - 1) // 2
    med = selection.select(a, m + 1)
    selection.partition(a, med)
    lsum = 0
    for i in a[:m]:
        lsum += i
    if lsum < y:
        if lsum + med >= y:
            return med
        return weighted_median_r(a[m + 1:], x - lsum - med, y - lsum - med)
    return weighted_median_r(a[:m], x, lsum)


if __name__ == "__main__":
    a = [0.09, 0.35, 0.06, 0.11, 0.15, 0.04, 0.2]
    print(a)
    print(weighted_median(a))
    print(list(itertools.accumulate(sorted(a))))
