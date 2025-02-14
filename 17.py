"""
Pangakonto pangakonto.txt
Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. 
Fail sisaldab eraldi ridadel pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid. 
Skript peab arvutama ja väljastama:
kogu tehingute arvu
positiivsete tehingute arvu
positiivsete tehingute kogusumma
Tulemused tuleb väljastada konsooli
"""
tehingute_arv = 0
tehingute_arv_pos = 0
pos_arv_summa = 0


#loeb andmeid failist:
with open("pangakonto.txt") as fail:
    sisu = fail.readlines()         #see loeb igat rida
    for number in sisu:
        #print(float(number))       #prindib read
        tehingute_arv+=1            #arvutab kokku tehingute arvu
        if float(number) > 0:              
            tehingute_arv_pos+=1            #arvutab kokku positiivsete tehingute arvu
            pos_arv_summa += float(number)  #arvutab kokku positiivsete tehingute arvude summa

print(f"Tehingute arv: {tehingute_arv}")        #prindib tehingute arvu
print(f"Positiivsete tehingute arv: {tehingute_arv_pos}")   #prindib positiivsete tehingute arvu
print(f"Positiivsete arvude summa: {pos_arv_summa:.2f}")        #prindib positiivsete tehingute arvude summa, 2 komakohaga


"""
Palgastatistika palgad.txt
Kirjuta Pythoni skript, mis loeb failist palgad.txt töötajate andmed ja arvutab eraldi:
meeste keskmised töötunnid, töötasu ning palk
naiste keskmised töötunnid, töötasu ning palk
Tulemused prindi konsooli
"""
meeste_palgad = 0
naiste_palgad = 0

with open ("palgad.txt") as fail:
    sisu = fail.readlines()
    for i in sisu:
        #print(i, end="")
        tykeldus = i.split(",")        #komadega eraldamine
        #print(tykeldus[3])              #valin kolmanda algusest (0,1,2,3 - mees või naine
        if tykeldus[3]=="Mees":
            meeste_palgad+=float(tykeldus[6])   #Meeste palgad kokku
        elif tykeldus[3]=="Naine":
            naiste_palgad+=float(tykeldus[6])

print(f"Meeste palgad: {meeste_palgad:.2f}")
print(f"Naiste palgad: {naiste_palgad:.2f}")
