#19.12.2024
#Sigrid Lillep

"""
1. Loo lugudest loend (koos numbrite ja jutumärkidega)
    1. ALIKA – “Bridges”
    2. Anett x Fredi – “Read Between The Lines”
    3. villemdrillem – “leekiv armastus”
    4. Clicherik & Mäx – “PAKSUD”
    5. nublu – “ära ärata”
    6. NOËP – “Move Your Feet”
    7. Trad.Attack! – “Bring It On”
    8. Bedwetters – “It Is What It Is”
    9. Reket – “Panama paberid”
    10. Grete Paia – “Võluväel”
Kuva kasutajale kõik lood massiivist
Küsi millist lugu ta “kuulata” soovib
Kuva kasutaja valitud lugu

"""

nimi = ["ALIKA - Bridges","Anett x Fredi - Read Between The Lines","villemdrillem - Leekiv armastus","nublu - ara arata"]

# for i in nimi:
#     print(i)

for i in range(4):
    print(f"{i+1}. {nimi[i]}")
    
valik = int(input("Millist lugu kuulata soovid (1-4): "))
print(f"Mängin: {nimi[valik-1]}")

