n, *a = map(int, open('26.txt'))
a.sort()
boom = 3
k = 0
s = a[-1]
cur_len = 1
i = 1
while i < len(a):
    if a[-i] == a[-i - 1]:
        cur_len += 1
        if cur_len == boom:
            k += 1
            i += 1
            cur_len = 1
    else:
        cur_len = 1
    i += 1
    s += a[-i]
print(s, k)
# 45760673 802