# 3.4 Jukebox
# Ada tahab valida plaadiautomaadist laulu ja uurib, milliseid laule masin mängib. Muusikapalad on kirjas failis, kus iga laul on eraldi real.
# Programmi testimiseks kasutatakse järgmisi faile, mida võite salvestada või koostada ise mõne tekstiredaktoriga (nt Notepad):
# jukebox.txt
# 80ndad.txt
# eesti_muusika.txt 
# edm.txt
# Koostada programm, mis
# küsib kasutajalt failinime (kasutaja sisestab failinime koos laiendiga, nt jukebox.txt);
# loeb sisestatud nimega failist andmed;
# näitab kõiki laule koos järjekorranumbritega (alates 1);
# küsib kasutajalt, mitmendat laulu ta soovib (kasutaja sisestab alati täisarvu);
# väljastab ekraanile vastavalt valitud arvule muusikapala







# 3.3 Sissetulekud
# Failis konto.txt on kirjas ujukomaarvudena pangakonto tehingud (kus positiivsed arvud on sissetulekud ja negatiivsed arvud on väljaminekud). 
# Iga arv on eraldi real. Tekstifaili kasutamiseks programmi sees peab fail asuma programmifailiga samas kaustas.
# Koostada programm, mis
# loeb failist nimega konto.txt andmed;
# väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud. 
# Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks nagu failis. 

fail = open("konto.txt", encoding="UTF-8")

for kirje in fail:
    if float(kirje) > 0:
        print(float(kirje), end="\n")

fail.close()



# 3.1 Ülikooli vastuvõetud
# Ülikooli I õppeastmesse (bakalaureuseõpe jm) võetakse igal aastal vastu sadu inimesi. Viimastel aastatel vastuvõetud inimeste arvud on aastate kaupa failis rebased.txt, 
# kus esimesel real on 2011. aastal vastuvõetute arv, teisel real 2012. aastal vastuvõetute arv kuni viimasel real on 2019. aastal vastuvõetute arv. 
# Koostada programm, mis
# loeb failist registreeritud vastuvõetute andmed aastate järgi järjendisse;
# Failist järjendisse saab lugeda järgmise programmijupi abil:
    # fail = open("rebased.txt", encoding="UTF-8")
    # vastuvõetud = []
    # for rida in fail:
    #     vastuvõetud.append(int(rida))
    # fail.close()
# küsib kasutajalt aastat
# võib eeldada, et sisestatakse täisarv, mis kuulub lõiku [2011; 2019].
# väljastab, mitu inimest sel aastal vastu võeti.

fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []

for rida in fail:
    vastuvoetud.append(int(rida))

fail.close()

aasta = input("Lisa aasta 2011-2019: ")
print(vastuvoetud[int(aasta[3])-1])
