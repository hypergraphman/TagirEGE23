procs = dict()
for line in open('22-0.txt'):
    id, time, relations = line.strip().split('\t')
    time = int(time)
    relations = relations.strip('"').split('; ')
    if relations[0] == '0':
        procs[id] = time
    else:
        procs[id] = time + max([procs[x] for x in relations])
print(max(procs.values()))