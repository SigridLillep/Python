def deposiit(algne_saldo, summa): 
    algne_saldo += summa
    return algne_saldo

def väljavõte(algne_saldo, summa):
    if summa > algne_saldo:
        print("Sul ei ole raha, mine tööle!")
    else:
        algne_saldo -= summa
    return algne_saldo

algne_saldo = 100  

while True:
    print(f"Konto jääk: {algne_saldo} €")
    toiming = input("Sisesta toiming (deposiit, väljavõte või lõpeta): ")

    if toiming == "lõpeta":
        print("Programm lõpetatud.")
        break
    elif toiming in ["deposiit", "väljavõte"]:
        try:
            summa = int(input("Sisesta summa: "))
            if summa < 0:
                print("Summa peab olema positiivne!")
            else:
                if toiming == "deposiit":
                    algne_saldo = deposiit(algne_saldo, summa)
                elif toiming == "väljavõte":
                    algne_saldo = väljavõte(algne_saldo, summa)
        except:
            print("Sisesta korrektne arv!")
    else:
        print("Tundmatu toiming!")