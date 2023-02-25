with open('k7c-5.txt') as f:
    s = f.readline()
k = 0
for c1, c2, c3, c4, c5 in zip(s, s[1:], s[2:], s[3:], s[4:]):
    if c1 != c2 != c3 != c4 != c5:
        k += 1
print(k)