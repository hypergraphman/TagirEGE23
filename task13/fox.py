g = {
    'а': 'б',
    'б': 'д',
    'в': 'аб',
    'г': 'ав',
    'д': 'веж',
    'е': 'илкж',
    'ж': 'вг',
    'и': 'лд',
    'к': 'ж',
    'л': 'к',
}


def f(s, p, e):
    if len(p) > 1 and s == e:
        return 1
    if len(p) != len(set(p)):
        return 0
    return sum([f(x, p + x, e) for x in g[s]])


print(f('д', 'д', 'д'))
