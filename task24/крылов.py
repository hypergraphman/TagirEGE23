with open('24var02.txt') as f:
    s = f.readline()

find = 'AB'
ln = 21
a = list(map(len, s.split(find)))[1:-1]
mn = sum(a[:ln - 1])
cr = mn
for i in range(ln - 1, len(a)):
    cr += a[i] - a[i - (ln - 1)]
    mn = min(cr, mn)
print(mn + ln * len(find))

