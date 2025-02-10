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

algne_saldo = 100

while True:
    toiming = input("Sisesta toiming (deposiit või väljavõte): ")
    
    if toiming not in ["deposiit", "väljavõte"]:
        print("Tundmatu toiming!")
        continue
        
        
    summa = int(input("Sisesta summa: "))
        
    if toiming == "deposiit":
            algne_saldo += summa
    elif toiming == "väljavõte":
        if summa <= algne_saldo:
            algne_saldo -= summa
        else:
            print("Sul ei ole raha, mine tööle!")

    print("Konto jääk:", algne_saldo)

