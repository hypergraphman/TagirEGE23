def f(s, e, alo):
    if s == e and len(alo & {17, 19, 23, 29, 31}) == 3:
        return 1
    if s > e or len(alo & {17, 19, 23, 29, 31}) > 3:
        return 0
    return f(s + 2, e, alo | {s + 2}) + f(s + 3, e, alo | {s + 3})


print(f(15, 34, set()))