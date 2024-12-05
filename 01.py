# 01.ülesanne
# Lillep 05.12.24

# F5 klahv või roheline nool üleval avab
# see impordib kilpkonna mooduli
import turtle

turtle.speed(0) #reguleeri 1-9
turtle.penup() #tõsta pliiatsit, et ei tuleks üleliigset joont
turtle.goto(-500,300) #liiguta sinna kuhu tahad
turtle.pendown() #pane pliiats uuesti maha, et tuleks kolmnurk
turtle.forward(200) # Liigutame kilpkonna edasi 200 piksli võrra
turtle.left(120) #liigub vasakule 120 piksli võrra
turtle.forward(200)
turtle.left(120)
turtle.forward(200)


# lõpetab kilpkonna, et ei jookseks kokku
turtle.done()