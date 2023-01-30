colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray']

acc_str = ''

for index, color in enumerate(colors):
    acc_str = f'{acc_str}{color}{", " if index + 1 < len(colors) else ""}'

print(f'Colors = {acc_str}')

random_numbers = [1, 2, 3, 5, 6, 7]
sum = 0
product = 1

for number in random_numbers:
    print(number)
#reassign a value of the variable
    sum = sum + number
    product = product * number

print(f'Sum = {sum}')
print(f'Product = {product}')