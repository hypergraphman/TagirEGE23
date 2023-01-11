def f(n):
    if n == 0:
        return 0
    if n % 2:
        return f(n // 2)
    return 1 + f(n // 2)

import time
st = time.time()
k = 0
for i in range(1, 1000000000):
    if f'{i:b}'.count('0') == 2:
        k += 1
print(time.time() - st)
print(k)