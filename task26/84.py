f = open('26-84.txt')
n = int(f.readline())
*st, = map(int, f.readline().split())
*au, = map(int, f.readline().split())
st.sort(reverse=True)
au.sort(reverse=True)
c = 1
s = cm = 0
for i in range(n):
    while s < n and au[s] >= st[i]:
        s += 1
    if s == n:
        cm += 1
    c = (c * (s - i)) % 100_000_007
print(c, cm)