import json

with open('users.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    users = data["users"]

    for user in users:
        id = user['id']
        name = f"{user['firstName']} {user.get('maidenName', '')} {user['lastName']}"
        age = user['age']
        gender = user['gender']
        email = user['email']
        phone = user['phone']
        username = user['username']
        password = user['password']
        birthDate = user['birthDate']
        image = user['image']
        bloodGroup = user['bloodGroup']
        height = user['height']
        weight = user['weight']
        eyecolor = user['eyeColor']
        hair = f"{user['hair']['color']}, {user['hair']['type']}"
        ip = user['ip']
        address = f"{user['address']['address']}, {user['address']['city']}, {user['address']['state']}, {user['address']['stateCode']}, {user['address']['postalCode']}, {user['address']['coordinates']['lat']}, {user['address']['coordinates']['lat']}, {user['address']['coordinates']['lng']}, {user['address']['country']}"
        macAddress = user['macAddress']
        university = user['university']
        bank = f"{user['bank']['cardExpire']}, {user['bank']['cardNumber']}, {user['bank']['cardType']}, {user['bank']['currency']}, {user['bank']['iban']}"



        print(f"Name: {name}")
        print(f"Hair: {hair}")
        print(f"Address: {address}")
        print(f"Bank info: {bank}")

    # for user in users: 
    #     kasutaja_valik = int(input("Vali kasutaja ID järgi (1-30):"))
    #     leitud_kasutaja = []
    #     if user['id'] == 30:
    #         leitud_kasutaja = user
    #         print(f"Leidsid kasutaja: {(nimi)}")
    #     else:
    #         print("Sellise ID'ga kasutajat ei leitud!")







