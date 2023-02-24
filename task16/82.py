from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 4 == 0:
        return n + f(n / 2 - 1)
    if n > 5 and n % 4 != 0:
        return n + f(n + 2)


for j in range(1, 1000):
    try:
        f(j)
        print(j)
    except:
        pass
