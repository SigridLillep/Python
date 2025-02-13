"""
PANGAKONTO
Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt. 
Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone:
 deposiit (raha lisamine)
 väljavõte (raha eemaldamine)
Tagastage peale igat toimingut konto jääk.
Funtsiooni parameetrid:
 algne_saldo: algse saldo väärtus
 toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote')
 summa: summa, mida soovitakse lisada või eemaldada
Näide:
Alustades algse saldoga 100, deposiidi toiminguga 50, peaks funktsioon konto_haldur tagastama uue saldo 150.
Väljavõte toiminguga 20 uus saldo oleks siis 130.
"""

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