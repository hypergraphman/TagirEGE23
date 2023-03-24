n, v, *a = map(int, open('26-99test.txt').read().split())
a.sort(reverse=True)
print(a)
trucks = []
while a:
    truck = []
    i = 0
    while i < len(a) and sum(truck) < v:
        if sum(truck) + a[i] <= v:
            truck.append(a.pop(i))
        else:
            i += 1
    trucks.append(truck)
print(trucks)
print(len(trucks), sum(trucks[-2]))