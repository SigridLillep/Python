#19.12.2024
#Sigrid Lillep

"""
Vanusepiiranguga üritus
    Sa oled loomas programmi, mis aitab kontrollida, kas inimesed vastavad vanusepiirangu nõuetele üritusel osalemiseks.
    Programm palub kasutajal sisestada oma vanuse.
    Kui vanus on vähemalt 18 aastat, siis programm annab teada, et kasutaja võib üritusele siseneda.
    Kui vanus on alla 18, siis programm teatab, et üritusele sisenemiseks ei ole piisavalt vana.
    Kasuta if ja else lauseid, et luua see vanusekontrolli programm.
"""
# try:
#     vanus = int(input("Anna oma vanus:"))
#     if vanus >= 18:
#         print("Lubatud!")
#     else:
#         print("Keelatud!")
# #F5 klahviga panen käima
# 
# except:
#     print("Viga sisestuses!")

#alt-3 klahviga sain # märgid ette, et järgmisi ülesandeid teha

"""
Ilmaennustuse rakendus (and)
        Sinu ülesanne on luua lihtne Pythoni programm, mis aitab kasutajal valida sobiva riietuse vastavalt ilmale.
        Kasutaja sisestab temperatuuri (Celsius).
        Kui temperatuur on alla 0 kraadi, peab programm väljastama soovituse kanda talveriideid.
        Kui temperatuur on vahemikus 0 kuni 15 kraadi, peaks programm soovitama kanda kevad-sügis rõivaid.
        Kui temperatuur on üle 15 kraadi, soovitab programm kanda suveriideid.
        Kasuta if, elif ja else lauseid selle ülesande lahendamiseks.
"""

# try:
#     kraadid = 30
#     
#     if kraadid < 0:
#         print("Talveriided")
#     elif kraadid >= 0 and kraadid <= 15:
#         print("Kevad-sügis")
#     else:
#         print("Suvi")
# 
# except:
#     print("Viga sisestuses!")

"""
Matemaatika test (randint)
        Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
        Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”. Kasutaja peab sisestama vastuse.
        Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”,
        kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
        Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.
"""
# import random
# 
# try:
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     vastus = int(input(f"Mis on {arv1} * {arv2} vastus.\nSisesta vastus:"))
#     korrutis = arv1 * arv2
#     print(vastus) #sellega prindib välja ka minu vastuse
#     print(korrutis) "sellega prindib välja ka arvuti vastuse, siis saan kontrollida, mis õige on näiteks
#     if korrutis == vastus:
#         print("Õige vastus!")
#     else:
#         print("Vale vastus, proovi uuesti!")
# except:
#     print("Viga sisestuses!")

"""
Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
        Kirjuta programm, mis simuleerib mündiviskamist. Programm genereerib juhusliku tulemuse – “kiri” või “kull”,
        kasutades random.randint(0,1) funktsiooni. Programmi koostamisel pead importima import random mooduli ja
        kasutama randint() funktsiooni, et valida kahe võimaliku tulemuse vahel. Näiteks, kui randint(0, 1) annab
        tulemuseks 0, siis võib see tähendada “kirja”, ja 1 võib tähendada “kulli”.
        KIRI on 0,
        KULL on 1.
        Seejärel palub programm kasutajal arvata, kumb külg maandub ülespoole.
        Kasuta if lauset, et kontrollida, kas kasutaja arvas õigesti.
        Kui arvas õigesti, siis joonista Turtle abil roheline ring; kui valesti, siis punane ring.
"""
import random
import turtle

try:
    valik = random.randint(0,1)
    arvamus = int(input("Vali kull 1 või kiri 0:"))
    if arvamus >= 0 and arvamus <=1:
        if valik == arvamus:
            print("Arvasid ära!")
            turtle.color("green")
            turtle.circle(50)
        else:
            print("Arvasid valesti!")
            turtle.color("red")
            turtle.circle(50)
        turtle.done()
    else:
        print("Sellist valikut ju polnud!")
    
except:
    print("Viga sisestuses!")
    
    
