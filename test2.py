import turtle
scale = 100
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# Maja kast
t.penup()
t.goto(-scale / 2, 0)
t.pendown()
for i in range(4):
    t.forward(scale)
    t.left(90)


# Maja katus
t.pencolor("green")
t.penup()
t.goto(-scale / 2, scale)
t.pendown()
for i in range(3):
    t.forward(scale)
    t.left(120)

# Maja uks
door_size = scale / 3
t.pencolor("red")
t.penup()
t.goto(-door_size / 2, 0)
t.pendown()
for i in range(4):
    t.forward(door_size)
    t.left(90)

t.hideturtle()
turtle.done()