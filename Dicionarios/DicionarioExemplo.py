usuarios = {}
# print(usuarios)

usuarios = {
    "chaves": ["Chaves do 8", "24/12/2020", "Recep_01"],
    "quico": ["Quico das Flores", "27/12/2020", "Recep_02"],
}
# print(usuarios)

usuarios["florinda"] = ["Florinda das Flores", "27/12/2020", "Recep_02"]
# print(usuarios)

for user in usuarios:
    print(usuarios[user])
    # print(usuarios[user][0])
