a = [list(map(lambda x: int(x) // 8 * 8, x.split())) for x in open('65.txt').readlines()]
b = [[0] * 10 for _ in range(len(a))]
for i in range(len(a)):
    print(a[i])
for i in range(len(a)):
    for j in range(len(a[i])):
        if i != 0 and j != 0:
            b[i][j] = max(b[i][j - 1], b[i - 1][j])
        elif i == 0:
            b[i][j] = b[i][j - 1]
        elif j == 0:
            b[i][j] = b[i - 1][j]
        b[i][j] += a[i][j]
print(b[-1][-1])
