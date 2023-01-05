import turtle

p = turtle.Pen()
turtle.bgcolor('black')

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray']

sides = int(turtle.numinput('How many sides?', \
    'How many sides do you want? (1-8)', \
    4, 1, 8)) # type: ignore

for x in range(360):
    p.pencolor(colors[x % sides])
    p.forward(x * 3 / sides + x)
    p.left(360 / sides + 1)
    p.width(int(x * sides / 200))
