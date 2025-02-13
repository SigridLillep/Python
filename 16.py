"""
Kirjutage Pythoni skript, mis tervitab kasutajat, 
kuvab praeguse töökataloogi, loob uusi katalooge vastavalt kasutaja soovile ning küsib,
 millist kataloogi soovitakse kustutada.

Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel
Skript kuvab kasutajale praeguse töökataloogi tee
Kataloogide loomine:
Skript küsib kasutajalt, mitu kataloogi ta soovib luua
Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, 
nummerdatuna (nt “1”, “2”)
Kataloogi kustutamine:
Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või 
olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne
Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see
Kuva kuupäeva kasutas olevad kataloogid
"""

import os
from datetime import date

print(f"Tere {os.getlogin()}")
print(f"Sinu töökataloogi tee: {os.getcwd()}")

kataloogide_arv = 10                        #annan teada, mitu kausta tahan
kustuta = 5                                 #annan teada, mitmenda kausta kustutada tahan
kuupaev = str(date.today())
print(kuupaev)

try:
    os.mkdir(kuupaev)                                   #loob uue kataloogi
    print(f"Tubli!, {kuupaev} kataloog on loodud!")
    for i in range(1, kataloogide_arv+1):               #loob kataloogi sisse uued kataloogid
        kaust = kuupaev+"/"+str(i)
        os.makedirs(kaust)
except:
    print("Kataloog juba olemas!")


#kustutab kausta:
if os.path.exists(kuupaev+"/"+str(kustuta)):        #kontrollib kas kaust on olemas
    os.rmdir(kuupaev+"/"+str(kustuta))
    print(f"{kustuta} kataloog kustutatud!")
else:
    print(f"{kustuta} kataloogi ei leitud!")

#kuva kataloogi sisu:
dir_list = os.listdir(kuupaev)
print("Kataloogi sisu: ")
for i in dir_list:
    print(i)





