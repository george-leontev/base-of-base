n = int(input('Amount of terms = '))
product = 1

for x in range(1, n + 1):
    product = product * x

print(f'Product = {product}')
