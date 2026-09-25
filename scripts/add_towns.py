#!/usr/bin/env python3
import json

TOWNS = {
    "index.html": ("Kamrup Metropolitan", ["North Guwahati", "Dispur", "Dharapur", "Azara", "Chandrapur"]),
    "best-astrologer-in-rangia.html": ("Kamrup District", ["Amingaon", "Palashbari", "Hajo", "Boko", "Chaygaon", "Sualkuchi", "Mirza", "Bijoynagar", "Changsari"]),
    "best-astrologer-in-nalbari.html": ("Nalbari District", ["Tihu", "Ghograpar", "Mukalmua", "Belsor"]),
    "best-astrologer-in-pathsala.html": ("Bajali District", ["Patacharkuchi", "Choukhuti", "Sarupeta"]),
    "best-astrologer-in-barpeta.html": ("Barpeta District", ["Barpeta Road", "Howli", "Sarthebari", "Sorbhog", "Mandia", "Kalgachia"]),
    "best-astrologer-in-bongaigaon.html": ("Bongaigaon District", ["Abhayapuri", "New Bongaigaon", "Manikpur", "Mererchar"]),
    "best-astrologer-in-dhubri.html": ("Dhubri District", ["Gauripur", "Bilasipara", "Chapar", "Sapatgram", "Golakganj", "Agomoni"]),
    "best-astrologer-in-hatsingimari.html": ("South Salmara-Mankachar District", ["Mankachar", "Kharuabandha", "Sukchar"]),
    "best-astrologer-in-goalpara.html": ("Goalpara District", ["Lakhipur", "Dudhnoi", "Balijana", "Krishnai"]),
    "best-astrologer-in-kokrajhar.html": ("Kokrajhar District", ["Gossaigaon", "Fakiragram", "Dotma", "Salakati"]),
    "best-astrologer-in-kajalgaon.html": ("Chirang District", ["Basugaon", "Bijni", "Dhaligaon"]),
    "best-astrologer-in-mushalpur.html": ("Baksa District", ["Salbari", "Shimla", "Barama", "Nagrijuli"]),
    "best-astrologer-in-tamulpur.html": ("Tamulpur District", ["Goreswar", "Kumarikata", "Nagrijuli"]),
    "best-astrologer-in-tezpur.html": ("Sonitpur District", ["Dhekiajuli", "Rangapara", "Jamugurihat", "Gohpur", "Thelamara"]),
    "best-astrologer-in-biswanath-chariali.html": ("Biswanath District", ["Gohpur", "Pavoi", "Halem", "Helem", "Borgang"]),
    "best-astrologer-in-mangaldai.html": ("Darrang District", ["Kharupetia", "Sipajhar", "Dalgaon", "Duni", "Namkhola"]),
    "best-astrologer-in-udalguri.html": ("Udalguri District", ["Tangla", "Bhergaon", "Rowta", "Harisinga", "Khoirabari"]),
    "best-astrologer-in-nagaon.html": ("Nagaon District", ["Raha", "Kampur", "Dhing", "Doboka", "Samaguri", "Kaliabor"]),
    "best-astrologer-in-morigaon.html": ("Morigaon District", ["Jagiroad", "Bhuragaon", "Mayong", "Moirabari", "Laharighat"]),
    "best-astrologer-in-hojai.html": ("Hojai District", ["Lumding", "Lanka", "Doboka", "Jugijan"]),
    "best-astrologer-in-diphu.html": ("Karbi Anglong District", ["Bokajan", "Howraghat", "Dokmoka", "Manja", "Bakalia"]),
    "best-astrologer-in-hamren.html": ("West Karbi Anglong District", ["Donkamokam", "Baithalangso", "Kheroni"]),
    "best-astrologer-in-haflong.html": ("Dima Hasao District", ["Umrangso", "Maibong", "Mahur", "Harangajao"]),
    "best-astrologer-in-dibrugarh.html": ("Dibrugarh District", ["Naharkatia", "Chabua", "Namrup", "Duliajan", "Moran", "Tingkhong"]),
    "best-astrologer-in-tinsukia.html": ("Tinsukia District", ["Digboi", "Margherita", "Doomdooma", "Makum", "Chapakhowa (Sadiya)", "Jagun", "Borgolai", "Ledo"]),
    "best-astrologer-in-jorhat.html": ("Jorhat District", ["Mariani", "Teok", "Titabor", "Rowriah", "Cinnamara"]),
    "best-astrologer-in-golaghat.html": ("Golaghat District", ["Bokakhat", "Dergaon", "Sarupathar", "Barpathar", "Numaligarh", "Khumtai"]),
    "best-astrologer-in-sivasagar.html": ("Sivasagar District", ["Nazira", "Amguri", "Demow", "Simaluguri", "Gaurisagar"]),
    "best-astrologer-in-sonari.html": ("Charaideo District", ["Moranhat", "Sapekhati", "Mahmora"]),
    "best-astrologer-in-north-lakhimpur.html": ("Lakhimpur District", ["Bihpuria", "Narayanpur", "Dhakuakhana", "Naoboicha"]),
    "best-astrologer-in-dhemaji.html": ("Dhemaji District", ["Silapathar", "Jonai", "Gogamukh", "Machkhowa"]),
    "best-astrologer-in-majuli.html": ("Majuli District", ["Kamalabari", "Jengraimukh", "Bongaon"]),
    "best-astrologer-in-silchar.html": ("Cachar District", ["Lakhipur", "Sonai", "Dholai", "Udharbond", "Borkhola", "Katigorah"]),
    "best-astrologer-in-hailakandi.html": ("Hailakandi District", ["Lala", "Algapur", "Katlicherra", "Panchgram"]),
    "best-astrologer-in-karimganj.html": ("Sribhumi (Karimganj) District", ["Badarpur", "Ram Krishna Nagar", "Nilambazar", "Patherkandi"]),
}

d = json.load(open("cities_data.json", encoding="utf-8"))
missing = []
for slug in d:
    if slug not in TOWNS:
        missing.append(slug)
    else:
        district_label, towns = TOWNS[slug]
        d[slug]["towns"] = towns
        d[slug]["towns_district_label"] = district_label

print("City pages missing town data:", missing)
print("Total city pages with towns added:", sum(1 for v in d.values() if "towns" in v))

json.dump(d, open("cities_data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# Save index.html towns separately (used directly in generate.py)
json.dump({"index.html": TOWNS["index.html"]}, open("index_towns.json", "w", encoding="utf-8"))
print("Done.")
