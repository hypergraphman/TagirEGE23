def alg(n):
    d1, d2, d3, d4 = map(int, str(n))
    a = [d1 + d4, d2 + d3]
    return str(min(a)) + str(min(a))
