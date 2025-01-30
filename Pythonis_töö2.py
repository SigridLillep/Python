# 2.5 ÕUNAD
# Lumivalgekesel oli 14 õuna ja ta tahtis neid pöialpoistega jagada. Ta sai aru, et kui kõik seitse pöialpoissi tahavad õunu ja ta annaks kõigile kaks õuna, 
# jääks ta ise üldse ilma. Nüüd otsustas ta õunu jagada nii, et küsib, mitu pöialpoissi tahab õunu, ja seejärel loosib iga soovija korral, kas anda talle üks või kaks õuna. 
# Koostada programm, mis
# küsib kasutajalt, mitu pöialpoissi tahab õunu (võib eeldada, et sisestatakse täisarv lõigust [0; 7]);
# leiab ja väljastab eraldi ridadele, mitu õuna saab iga pöialpoiss (programm genereerib iga kord juhuslikult arvu 1 või 2);
# leiab ja väljastab eraldi reale, mitu õuna jääb Lumivalgekesele.

import random

ounad = 14
poialpoiss = int(input("Mitu pöialpoissi tahab õuna: "))

for i in range(poialpoiss):
    suv_oun = random.randint(1,2)
    print(suv_oun)
    ounad -= suv_oun

print(f"Lumivalgekesele jäi {ounad} õuna!")



# 2.2 MURELIKUD LAPSEVANEMAD
# Jänesevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja süsteemi, 
# kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. 
# Paarituarvulistel ringidel porgandeid juurde ei saa. 

# Koostada programm, mis
# küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil saadavate porgandite koguarvu;
# väljastab saadavate porgandite koguarvu ekraanile.
# Näiteks, kui kasutaja sisestas 6, siis summa on 12, sest 2 + 4 + 6 = 12. Kui kasutaja sisestas 7, siis on summa samuti 12, sest 2 + 4 + 6 = 12.

porgandid = 0
ringide_arv = 6


while ringide_arv >= 0:
    if ringide_arv % 2 == 0:
        porgandid += ringide_arv
    ringide_arv-=1
    

print(porgandid)



# 2.1 ÄRATUS
# Otil on hommikuti raske tõusta ja tal on äratuskell, mis äratab teda teatud arv kordi koos tervitustekstiga. Koostada programm, mis
# küsib kasutajalt, mitu korda äratus heliseb ning
# väljastab sama arv kordi ekraanile Tõuse ja sära!.

# kordade_arv = int(input("Kordade arv: "))

# for i in range(kordade_arv):
#     print("Tõuse ja sära!")