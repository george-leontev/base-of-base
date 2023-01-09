a = int(input('Price for 1 kg = '))

n = int(input('Amount of kilogram = '))

for x in range(1, n * 10 + 1):
    m = x / 10
    print(f'{m} kg. sweets -> {m * a}$')