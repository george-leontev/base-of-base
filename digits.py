store: list[int] = []
a: int = int(input('A = '))
s = ''
n = 0
i = 0

while a != 0:
    q = a // 2
    r = a % 2
    a = q
    store.append(r)
    s = str(r) + s
    n = n + r * 10**i
    i += 1



print(f'{s} as a string!')

for _ in range(len(store)):
    print(store.pop(), end='')
print(f' from a store!')

print(f'{n} as a decimal!')
