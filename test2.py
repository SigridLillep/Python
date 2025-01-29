import turtle
suurus = 100
turtle.speed(3)
turtle.pensize(3)

# Maja kast
turtle.penup()
turtle.goto(-suurus / 1, 0)
turtle.pendown()
for i in range(4):
    turtle.forward(suurus)
    turtle.left(90)


# Maja katus
turtle.pencolor("green")
turtle.penup()
turtle.goto(-suurus / suurus,suurus)
turtle.pendown()
for i in range(2):
    turtle.left(120)
    turtle.forward(suurus)
    

# Maja uks
uks = suurus / 2
turtle.pencolor("red")
turtle.penup()
turtle.goto(-uks / 2, 0)
turtle.pendown()
turtle.setheading(0)
for i in range(3):
    turtle.left(90)
    turtle.forward(uks)


turtle.hideturtle()
turtle.done()
    
    




