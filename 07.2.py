# Ülesanne07.2
# Kasuta etteantud loendit ja toesta nõutud operatsioonid. 
# Lisa igale tegevusele kommentaar ja vasta täislausega:
# “jaanuar”,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
# Kuva mõõdetava kuu nimetus
# Kuva viimase mõõtmise tulemus
# Kuva ainult temperatuurid
# Leia kuu maksimaalne ja minimaalne temperatuur
# Leia kuu keskmine temperatuur
# Mitu korda esines -20 kraadi
# Eemalda element nr 5
# Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
# Sorteeri temperatuurid nimekirjas kasvavas järjekorras

# ctrl-Ä paneb tervele tekstile # märgid ette

jtemp = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
print (f"Mõõdetav kuu: {jtemp[0]}")
print (f"Viimase mõõtmise tulemus: {jtemp[-1]} kraadi")

maks = -100
mini = 100
summa = 0
kokku = 0
kordused = 0

for t in range(1,len(jtemp)): 
    print(jtemp[t], end=" ") #prindib kõik temperatuurid
    if jtemp[t]>maks:           #max temperatuuri kontroll
        maks = jtemp[t]
    if jtemp[t]<mini:           #min temperatuuri kontroll
        mini = jtemp[t]
    summa+=jtemp[t]
    kokku+=1
    if jtemp[t]== -20:
        kordused+=1

jtemp.pop(5)            # kustutab
jtemp.insert(5,36)      # lisab
#jtemp.sort()

# shift-alt ja nool alla kopeerib rea

print()
print(f"Maksimum temp on: {maks}")
print(f"Miinimum temp on: {mini}")
print(f"Keskmine temp on: {summa/kokku:0.2f}")
print(f"-20 kraadi esineb: {kordused} korda")
print(jtemp)
