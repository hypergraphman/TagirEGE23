comds = []


def f(st, fin, s):
    if st == fin:
        comds.append(s)
        return 1
    if st > fin:
        return 0
    return f(st + 1, fin, s + '1') + f(st * 2, fin, s + '2')


print(f(1, 14, '0'))

k = 0
for s in comds:
    if s.count('111') or s.count('222'):
        k += 1
print(26 - k)