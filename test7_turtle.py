import turtle

p = turtle.Pen()
turtle.bgcolor('black')
sides = 6
colors = ['blue', 'yellow', 'green', 'red', 'orange', 'purple']
for x in range(360):
    p.pencolor(colors[x % sides])
    p.forward(x * 3 / sides + x)
    p.left(360 / sides + 1)
    p.width(int((x * sides) / 200))
