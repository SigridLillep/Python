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
        company = f"{user['company']['department']}, {user['company']['name']}, {user['company']['title']}"
        company_address = f"{user['company']['address']['address']}, {user['company']['address']['city']}, {user['company']['address']['state']}, {user['company']['address']['stateCode']}, {user['company']['address']['postalCode']}, {user['company']['address']['coordinates']['lat']}, {user['company']['address']['coordinates']['lng']}, {user['company']['address']['country']}"
        ein = user['ein']
        ssn = user['ssn']
        userAgent = user['userAgent']
        crypto = f"{user['crypto']['coin']}, {user['crypto']['wallet']}, {user['crypto']['network']}"
        role = user['role']

        print(f"{id}. {name}")

kasutaja_valik = int(input("Vali kasutaja ID järgi (1-30):"))
    
for user in users:
    if kasutaja_valik == user['id']:
        print(f"Leidsid kasutaja: {user['firstName']} {user.get('maidenName', '')} {user['lastName']}")
    # else: 
    #     print("sellist ID'd pole")
       







