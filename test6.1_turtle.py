import turtle

p = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "blue", "yellow", "green"]
for x in range(1000):
    p.pencolor(colors[x % 4])
    p.circle(x)
    p.left(92)
