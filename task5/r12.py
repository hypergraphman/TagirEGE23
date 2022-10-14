from itertools import permutations


def alg(n):
    a = []
    for d1, d2 in permutations(str(n), r=2):
        t = int(d1 + d2)
        if 10 <= t <= 99:
            a.append(t)
    return max(a) - min(a)


print(alg(351))
