import random


def good_chips(tr):
    cl = len(tr)
    gcs = list(range(cl))
    while gcs:
        gu = random.choice(gcs)
        gc = 0
        new_gcs = []
        for g in gcs:
            if tr[g][gu] == 1:
                gc += 1
            else:
                new_gcs.append(g)
        if gc > len(gcs) // 2:
            return tr[gu]
        gcs = new_gcs


def test_result(chips):
    cl = len(chips)
    return [chips if c == 1 else [random.randint(0, 1) for _ in range(cl)] for c in chips]
    
    
if __name__ == "__main__":
    cl = 100
    bad = random.randint(0, cl // 2 - 1)
    good = cl - bad
    chips = [0] * bad + [1] * good
    random.shuffle(chips)
    print(chips)
    tr = test_result(chips)
    print(good_chips(tr))
    
