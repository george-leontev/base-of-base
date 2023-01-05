import turtle
p = turtle.Pen()
colors = ['red', 'blue', 'yellow', 'green']
for x in range(1000):
  p.pencolor(colors[x % 4])
  p.forward(x)
  p.left(93)
  