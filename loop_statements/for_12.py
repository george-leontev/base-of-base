n = int(input('Amount of factors = '))
product = 1
factor = 1

for x in range(1, n):
    factor = factor + 0.1
    product = product * factor


print(f'Product = {product:.2f}')
print(f'Factor = {factor:.2f}')