import turtle
p = turtle.Pen()
turtle.bgcolor('black')
colors = ['yellow', 'red', 'blue', 'green']
your_name = turtle.textinput('Enter your name', 'What is your name?')
for x in range(1000):
    p.pencolor(colors[x % 4])
    p.penup()
    p.forward(x * 4)
    p.pendown()

    p.write(your_name, font = ('Arial', int((x + 4) / 4),'bold'))
    p.left(92)