"""
2. broneeringud.json
•	Leia, kui palju on broneeringuid teenusele "Massaaž".
•	Leia kõik broneeringud, mis toimuvad pärast kella 12:00.
•	Leia kliendid, kelle broneeringud on nädalavahetusel.
•	Leia päev, millel on kõige rohkem broneeringuid.
•	Loetle unikaalsed teenused ja mitu korda neid broneeriti.
"""

import requests
from datetime import datetime

url = 'https://metshein.com/kordamine/json/broneeringud.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    massaaž = 0
    parast12 = 0
    #print(data)
    for broneering in data['broneeringud']:
        #print(broneering['teenus'])
        if broneering['teenus'] == "Massaaž":
            massaaž += 1
        
        broneeringu_aeg = datetime.strptime(broneering['aeg'], "%H:%M")
        if broneeringu_aeg.hour >= 12:
            parast12 += 1
        
        #Kliendid, kelle broneering on nädalavahetusel:
        kp = datetime.strptime(broneering['kuupäev'], '%Y-%m-%d').strftime('%A')
        if kp == "Sunday" or kp == "Saturday":
            print(broneering["klient"])

else:
    print("Päring ebaõnnestus, staatuskood:", response.status_code)

print(f"Broneeringuid teenusele massaaž on {massaaž} tükki")
print(f"Pärast 12:00 toimub {parast12} broneeringut")
