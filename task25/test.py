from fnmatch import *


def divs(n):
    s = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            s |= {d, n // d}
    return sorted(s)


for i in range(9995597, 10**7):
    if fnmatch(str(i), '9?*55*7'):
        d = sum(divs(i)) % 21
        print(i, d)
    i -= 1

# 9999557 0
# 9998557 17
# 9997557 12
# 9996557 12
# 9995597 18