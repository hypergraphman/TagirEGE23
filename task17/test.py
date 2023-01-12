a = list(map(int, open('test.txt').readlines()))
print(a)
for i in range(1, len(a)):
    p1, p2 = a[i - 1], a[i]
    print(p1, p2)