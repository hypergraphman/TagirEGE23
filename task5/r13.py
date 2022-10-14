def alg(n):
    s1 = f'{n:b}'
    s2 = s1 + str(s1.count('1') % 2)
    s2 = s2 + str(s2.count('1') % 2)
    return int(s2, 2)


i = 1
while alg(i) <= 77:
    i += 1
print(i)
