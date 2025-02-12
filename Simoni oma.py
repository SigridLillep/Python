saldo = 100

def summaP():
    summa = float(input("Kui palju raha: "))
    return summa
     #print(summa)
def deposiit():
    summa = summaP()
    tulem = summa + saldo
    print(f"Teie kontojääk on {tulem}€")
def valjavott():
    summa = summaP()
    if summa < saldo:
        jaak = saldo-summa
        print(f"Teie kontojääk on {jaak}€")
    elif summa > saldo:
        print("Sul pole piisavalt raha, mine teeni juurde!")
    else:
        print("Midagi tegid valesti, korigeeri oma sisestust!")

while True:

    print(f"Tere, Olen sinu pank ja sinu konto saldo on {saldo}€ ")

    try:
        valik = str(input("Tee oma valik: 'deposiit', 'valjavott' või 'exit'  "))
        
        if valik == "deposiit":
            print("Valisid raha sisestamise!")
            deposiit()
        elif valik == "valjavott":
            print("Valisid raha valjavotmise")
            valjavott()
        elif valik == "exit":
            print("Valisid lahkumise")
            print("Head päeva Teile!")
            break
        else:
            print("Kirjutasid midagi valesti")
            break
    except:
        print("Sisesta õigesti oma valik!")
    

    tegevus = int(input("Kas sulgen programmi? jah on 1 ja ei on 0: "))
    if tegevus != 0:
        break