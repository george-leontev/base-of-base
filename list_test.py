from random import random

numbers = []
for x in range(50):
    r = int(random() * 100)
    numbers.append(r)

for number in numbers:
    if number % 2 == 1:
        print(number)