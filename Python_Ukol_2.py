#Část 1

import requests
import json

ico = input("Zadej IČO subjektu: ")

web = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO"
web_ico = web.replace("ICO", ico)


#ico Czechitas: 22834958 

response = requests.get(web_ico)
data_ico = response.json()


with open('data_ico.json', mode='w', encoding='utf-8') as file: 
     json.dump(data_ico, file, indent=4, ensure_ascii=False)

print(data_ico["obchodniJmeno"])
print(data_ico["sidlo"]["textovaAdresa"])




#Část 2

import requests
import json

nazev = input("Zadej název subjektu: ")

web_vyhledat = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = f'{{"obchodniJmeno": "{nazev}"}}'
data = data.encode("utf-8")

response = requests.post(web_vyhledat, headers=headers, data=data)
data_nazev = response.json()

with open("data_nazev.json", mode='w', encoding='utf-8') as file:
     json.dump(data_nazev, file, indent=4, ensure_ascii=False)

print(data_nazev["pocetCelkem"])
#print(data_nazev["ekonomickeSubjekty"])

for subjekt in data_nazev.get("ekonomickeSubjekty"):
     obchodni_jmeno_subjektu = subjekt.get("obchodniJmeno")
     ico_subjektu = subjekt.get("ico")
     print(f"{obchodni_jmeno_subjektu}, {ico_subjektu}")
