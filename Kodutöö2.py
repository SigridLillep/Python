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

    print("Uus saldo:", algne_saldo)

"""
KILPKONN
Kirjuta programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. 
Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, 
valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
Näide:
Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
Mitu kujundit soovid joonistada? 5
[Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, 
jättes sisendi tühjaks.
"""
