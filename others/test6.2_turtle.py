import turtle

p = turtle.Pen()
turtle.bgcolor("black")
colors = ["blue", "yellow", "green", "red"]
for x in range(1000):
    p.pencolor(colors[x % 4])
    p.forward(x)
    p.left(91)
