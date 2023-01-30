import turtle

p = turtle.Pen()
turtle.bgcolor('black')
sides = 2
colors = ('blue', 'red')
for x in range(350):
    p.pencolor(colors[x % sides])
    p.forward(x * 3 / sides + 1)
    p.left(360 / sides + 1)
    p.width(int((x * sides) / 200))
    p.left(90)
