import json

klass12opilased = []
kokku12klass = 0
huvialad = []

with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    students = json.load(file)
    for student in students:
        # print(student["klass"])
        if student["klass"]=="12":
            klass12opilased.append(student["nimi"])
            kokku12klass+=1
            for tegevus in student["tegevused"]:
                if tegevus not in huvialad:
                    huvialad.append(tegevus)
           # hinneteleht
            print("-----------HINNETELEHT-------------")
            print(student["nimi"])
            d = student["hinded"]
            for k, v in d.items():
                print(k, v) 
            print("-----------------------------------")

print("12 klassi õpilased:")
for i in klass12opilased:
    print(i)
print(f" 12 klassis käib kokku {kokku12klass} õpilast")
print("12 klassi õpilaste huvialad:")
for i in huvialad:
    print(i)