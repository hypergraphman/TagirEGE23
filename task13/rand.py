g = {
    'А': 'БЕД',
    'Б': 'ВЗ',
    'В': 'ЖЗ',
    'Ж': 'ЛЗ',
    'З': 'ГЛ',
    'Л': 'К',
    'К': 'З',
    'И': 'ЗКЕ',
    'Е': 'ЗД',
    'Д': 'И',
    'Г': 'БА',
}


def f(s, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) != len(set(p)):
        return 0
    return sum([f(x, p + x) for x in g[s]])


print(f('З', 'З'))
