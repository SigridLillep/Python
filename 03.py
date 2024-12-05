#3.ülesanne
#05.12.2024

import turtle

#3.1
nimi = "Sigrid" #sõne, string, lühend str
vanus = 35 #int, integer, täisarv
keskmine_hinne = 6.5 #komaarv, float
#plussiga saan stringid kokku
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne))
#komaga saan mitu asja printida
print(nimi,",",vanus,"aastat vana ja keskmine hinne on",keskmine_hinne)
#lause vormindamine lünkadena
print(f"{nimi} on {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}")

#3.2
toode = "porgand"
kogus = 3
hind = 5.35
print("Soovin"+" "+toode+"eid"+" "+str(kogus)+", "+"mille tüki hind on"+" "+str(hind)+" "+"eurot")

#3.7
kylje_pikkus = 100
nurk = 120
varv = "red"

turtle.speed(5)
turtle.color(varv)
#kolmnurk 1
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)

#kolmnurk 2
turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()

turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)

#kolmnurk 3
turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()

turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)


turtle.done()

