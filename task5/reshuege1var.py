def alg(n):
    s = f'{n:b}'
    s = s[1:].lstrip('0')
    if not s:
        s = '0'
    return n - int(s, 2)


f = set()
for j in range(10, 1001):
    f.add(alg(j))

print(f)
print(len(f))