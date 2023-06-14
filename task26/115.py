f = open('26-115.txt')
n, m = map(int, f.readline().split())
times = []
for el in f.readlines():
    t1, t2 = map(int, el.split())
    times.append((t1, t2))
trains = [0] * (n + 1)
times.sort(key=lambda x: x[0])
k = 0
last = 0
print(times)
for i in range(len(times)):
    for j in range(1, len(trains)):
        if times[i][0] > trains[j]:
            trains[j] = times[i][1]
            k += 1
            last = j
            break
print(k, last)
