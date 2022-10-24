from itertools import product


def n_to_p(n, p):
    alf = '0123456789AB'
    r = ''
    while n != 0:
        r = alf[n % p] + r
        n //= p
    return r


def alg(n):
    s1 = int(n[0], 12) + int(n[2], 12)
    s2 = int(n[1], 12) + int(n[3], 12)
    n1, n2 = sorted([s1, s2], reverse=True)
    return n_to_p(n1, 12) + n_to_p(n2, 12)


mx = ''
for num_digits in product('12456B', repeat=4):
    num = ''.join(num_digits)
    if alg(num) == '115':
        mx = max(mx, num)
print(mx)
