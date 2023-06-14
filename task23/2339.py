s = set()


def f(v, c):
    if c == 15:
        s.add(v)
        return 
    f(v * 2, c + 1)
    f(v * 2 + 1, c + 1)


f(1, 0)
print(len(s))