a = int(input('Price for 1 kg. of sweets = '))

n = int(input('Amount of kilogram = '))
k = float(input('Step = '))

for x in range(1,  int((n - 1) / k + 1) ):
    m = x * k + 1
    print(f'{m:.1f} kg. sweet -> {(m * a):.1f}$')