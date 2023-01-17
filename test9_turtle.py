import turtle

p = turtle.Pen()
turtle.bgcolor('black')
sides = 8
colors = ('blue', 'yellow', 'pink', 'red', 'purple', 'green', 'orange', 'turquoise')
for x in range(1000):
    p.pencolor(colors[x % sides])
    p.forward(x * 3 / sides + 1)
    p.left(360 / sides + 1)
    p.width(int((x * sides) / 200))
