import re

a = list(map(int, open('17-346.txt').readlines()))
k = 0
mx = 0
for i in range(2, len(a)):
    p1, p2, p3 = a[i - 2], a[i - 1], a[i]
    all_digit = ''.join(str(p1) + str(p2) + str(p3))
    p = 1
    for digit in map(int, all_digit):
        if digit % 2 == 0:
            p *= digit
    if p <= 2 * 10 ** 9 and re.fullmatch(r'11\d*6\d*', str(p)):
        k += 1
        mx = max(p, mx)
print(k, mx)
