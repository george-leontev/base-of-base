random_numbers = [37, 43, 20, 25, 17, 98]

for number in random_numbers:
    if number > 40:
        print(number)

sum = 0

for number in random_numbers:
    if number < 40:
        sum = sum + number

print(f'Sum = {sum}')

product = 1
for number in random_numbers:
    if number > 40:
        product = product * number

print(f'Product = {product}')

length = len(random_numbers)
sum = 0

for number in random_numbers:
    sum = sum + number

average = sum / length
print(f'Average = {average}')

