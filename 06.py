#19.12.2024
#Sigrid Lillep

"""
    Kasuta Python Turtles’i, et joonistada stseen, kus redel toetub majale 53° nurga all.
    Redeli ülemine ots peaks ulatuma 4,4 meetri kõrgusele maja seinal virtuaalses mõõtkavas.
    Muuda nurgad radiaanideks (radians)
    Redeli kaugus seinast: kasuta tangensfunktsiooni (tan) ja antud nurka, et leida, kui kaugele redeli alumine ots on seinast.
    Valem:
    Kaugus=Kõrgus seinal/tan(Nurk)
     
    Redeli pikkus: kasuta Pythagorase teoreemi, et leida redeli pikkus, kui tead redeli kõrgust seinal ja kaugust seinast.
    Valem:
    Pikkus=(Kõrgus seinal)2+(Kaugus seinast)2
     
    Ümarda vastus 2 komakohta
    Kuva vastused konsoolid
    Kasuta Python Turtles’i, et visualiseerida maantee tõusu, mis 140 meetri jooksul tõuseb 15 meetrit.
    Sinu ülesandeks on arvutada maantee tõusunurk ja näidata, kui suurt tõusu protsentides liiklusmärk enne tõusu kuvaks.
    Tõusunurga arvutamine: Kasuta tangensfunktsiooni inversi (atan), et leida tõusunurk radiaanides, ja teisenda see kraadideks.
    Nurk (kraadides) = atan(tõus/maa) × (180/π).
    Tõusu protsent: Tõusu protsent on (vertikaalne tõus / horisontaalne vahemaa) × 100.
    Ümarda täisarvuti ja kuva vastus konsoolis
"""
import math
import turtle

nurk = 53
korgus = 4.4 #õ tähe asemel harjuta pigem o. komasid ei ole, numbritel käib . vahel

rad = math.radians(nurk)
kaugus = korgus / math.tan(rad)
c = math.sqrt(math.pow(kaugus,2) + math.pow(korgus,2))

print(c)
kordaja = 50
turtle.fd(kaugus*kordaja)
turtle.lt(90)
turtle.fd(korgus*kordaja)
turtle.lt(90+53)
turtle.fd(c*kordaja)


turtle.done()


