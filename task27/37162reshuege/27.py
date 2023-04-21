n, *a = map(int, open('27_A.txt'))

k = 89
mx_s = 0
mn_len = float('inf')
for i in range(n):
    for j in range(i, n):
        t = a[i: j + 1]
        s = sum(t)
        if s % k == 0:
            ln = len(t)
            if s > mx_s:
                mx_s = s
                mn_len = ln
            elif s == mx_s:
                mn_len = min(mn_len, ln)
print(mn_len)