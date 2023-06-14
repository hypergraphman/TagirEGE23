s = set()


def f(v, c):
    if c == 8:
        s.add(v)
        return
    f(v + 1, c + 1)
    f(v + 5, c + 1)
    f(v * 3, c + 1)


f(1, 0)
print(s)
c = 0
for el in s:
    if 1000 <= el <= 1024:
        c += 1
print(c)