bob = [
    ['a', 'b'],
    ['c', 'd'],
    ['e', 'f', 'g'],
    ['i'],
    ['j', 'k'],
    ['l', 'm'],
    ['n']
]

for i in bob:
    for j in i:
        print(j)

jim = {
    'a': {'b': 'c'},
    'd': {'e': 'f'},
    'g': {'h': 'i'},
}

for k in jim:
    print(k)
    for k2 in jim[k]:
        print(k2)
        print(
            jim[k][k2]
        )
