n, k, *a = map(int, open('26-100.txt').read().split())
a.sort(reverse=True)
mx_res = []
for j in range(len(a) - k):
    i = 0
    res = []
    while len(res) < k and i + 1 < len(a):
        if a[i] - a[i + 1] <= 11:
            res.append(a[i])
        i += 1
    if not mx_res or res[-1] >= mx_res[-1]:
        mx_res = res
    a.pop(0)

print(mx_res)