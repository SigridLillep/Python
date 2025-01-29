import turtle
suurus = 100
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# Maja kast
t.penup()
t.goto(-suurus / 2, 0)
t.pendown()
for i in range(4):
    t.forward(suurus)
    t.left(90)


# Maja katus
t.pencolor("green")
t.penup()
t.goto(-suurus / 2, suurus)
t.pendown()
for i in range(3):
    t.forward(suurus)
    t.left(120)

# Maja uks
uks = suurus / 2
t.pencolor("red")
t.penup()
t.goto(-uks / 2, 0)
t.pendown()
for i in range(4):
    t.forward(uks)
    t.left(90)

t.hideturtle()
turtle.done()