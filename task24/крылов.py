with open('24var02.txt') as f:
    s = f.readline()

a = list(map(len, s.split('A')))[1:-1]
mn = sum(a[:34])
cr = mn
for i in range(34, len(a)):
    cr += a[i] - a[i - 34]
    mn = min(cr, mn)
print(mn + 35)

