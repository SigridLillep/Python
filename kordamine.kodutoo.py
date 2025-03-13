"""
2. broneeringud.json
•	Leia, kui palju on broneeringuid teenusele "Massaaž".
•	Leia kõik broneeringud, mis toimuvad pärast kella 12:00.
•	Leia kliendid, kelle broneeringud on nädalavahetusel.
•	Leia päev, millel on kõige rohkem broneeringuid.
•	Loetle unikaalsed teenused ja mitu korda neid broneeriti.
"""
import requests
import json
massaaž = 0

url = 'https://metshein.com/kordamine/json/broneeringud.json'
fail = 'broneeringud.json'

response = requests.get(url)

if response.status_code == 200:
    with open(fail, 'wb') as f:
        f.write(response.content)
    print(f"Fail {fail} salvestatud")
else:
    print(f"Faili alla laadimine ebaõnnestus: {response.status_code}")

with open('broneeringud.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    broneeringud = data["broneeringud"]

    for broneering in broneeringud:
        id = broneering['broneeringu_id']
        name = broneering['klient']
        kp = broneering['kuupäev']
        teenus = broneering['teenus']
        aeg = broneering['aeg']

        if broneering['aeg']>="12:00":
                print(name)


        


