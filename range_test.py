for x in range(10):
    print(f'x = {x}')
    print('x = ' + str(x))

s = 'Hello' # literal value
y = 23.5

print(f'y = {y}')

s = s + ' world' # concatenation
s = f'{s}!'
print(s)

y = y + 12.5

print(f'y = {y}')

if y > 37:
    print(f'A value of variable is y = {y} and greater than 37.')
else:
    for i in range(5):
        if i < 3:
            print(f'A value of variable is y = {y} and less than 37.')