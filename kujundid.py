import turtle
suurus = 100
t = turtle.Turtle()
t.speed(9)
t.pensize(3)

t.penup()
t.goto(-suurus / 2, 0)
t.pendown()
for i in range(4):
    t.forward(suurus)
    t.left(90)

t.penup()
t.pencolor("red")
t.goto(-suurus / 50, 50)
t.pendown()
for i in range(4):
    t.forward(suurus)
    t.left(90)


t.penup()
t.pencolor("black")
t.goto(-suurus / 2, -200)
t.pendown()
for i in range(4):
    t.forward(suurus)
    t.left(90)

t.penup()
t.pencolor("red")
t.goto(-suurus / 200, -200)
t.left(45)
t.pendown()
for i in range(4):
    t.left(90)
    t.forward(suurus)
    


t.hideturtle()
turtle.done()