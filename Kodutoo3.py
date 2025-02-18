import json

with open('users.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    users = data["users"]

for user in users:
    nimi = f"{user['id']}. {user['firstName']} {user.get('maidenName', '')} {user['lastName']}"
    print(nimi)



