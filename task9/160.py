lines = open('9-160.txt').readlines()
k = 0
for line in lines:
    t = sorted(map(int, line.split()))
    if t[-1] < sum(t[:-1]) and t[0] + t[-1] == t[1] + t[2]:
        k += 1
print(k)
