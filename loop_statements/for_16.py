n = int(input('Degree = '))
a = int(input('Number = '))
product = 1

for x in range(1, n + 1):
    product = product * a
    print(product)

print(f'Product = {product}')