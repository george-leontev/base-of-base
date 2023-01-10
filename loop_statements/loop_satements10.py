a = int(input('Number A ='))
b = int(input('Number B = '))
product = 1

for n in range(a, b + 1):
    print(n)
    product = product * n

print(product)