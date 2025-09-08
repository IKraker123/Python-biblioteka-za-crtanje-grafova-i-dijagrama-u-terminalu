# Plotext – dijagrami kreirani pomoću biblioteke Plotext

# -----------------------------
# PODACI KOJI SE KORISTE ZA KREIRANJE DIJAGRAMA
# -----------------------------
zupanije = [
    "Zagrebačka","Krapinsko-zagorska","Sisačko-moslavačka","Karlovačka","Varaždinska",
    "Koprivničko-križevačka","Bjelovarska-bilogorska","Primorsko-goranska","Ličko-senjska",
    "Virovitičko-podravska","Požeško-slavonska","Brodsko-posavska","Zadarska",
    "Osječko-baranjska","Šibensko-kninska","Vukovarsko-srijemska","Splitsko-dalmatinska",
    "Istarska","Dubrovačko-neretvanska","Međimurska","Grad Zagreb"
]
zupanije4=["Zagrebačka", "Krapinsko-zagorska", "Sisačko-moslavačka", "Karlovačka", ]
stan2021=[299985,120702,139603,112195]
stan2011=[317606,132892,172439,128899]
stan2001=[309696,142432,185387,141787]

godine = ["2021","2011","2001"]
muskarci = [1_865_129, 2_066_335, 2_135_900]
zene = [2_006_704, 2_218_554, 2_301_560]

stan_2021 = [
    299985,120702,139603,112195,159487,101221,101879,265419,42748,70368,64084,130267,
    159766,258026,96381,143113,423407,195237,115564,105250,767131
]
stan_2011 = [
    317606,132892,172439,128899,175951,115584,119764,296195,50927,84836,78034,158575,
    170017,305032,109375,179521,454798,208055,122568,113804,790017
]
stan_2001 = [
    309696,142432,185387,141787,184769,124467,133084,305505,53677,93389,85831,176765,
    162045,330506,112891,204768,463676,206344,122870,118426,779145
]
dan_predmet=["Pon 08:00-10:00- Primjena_UI_u_poslovanju",
             "Pon 10:00-12:00 - Otkrivanje_znanja_u_podacima",
             "Pon 15:30-17:00 Primjena_UI_u_poslovanju",
             "Uto 10:00-12:00- Komuniciranje_i_virtualni_timovi",
             "Uto 13:00-15:00- Inteligentni_interaktivni_sustavi",
             "Sri 15:00-16:00- Inteligentni_interaktivni_sustavi",
             "Čet 08:00-09:00- Komuniciranje_i_virtualni_timovi",
             "Čet 18:30-20:00- Otkrivanje_znanja_u_podacima"
            ]

godine2021 = [
    42, 5, 78, 14, 33, 27, 63, 9, 56, 48, 21, 72, 38, 3, 61, 44, 12, 85, 7, 95,
    68, 18, 25, 36, 82, 29, 1, 50, 67, 74, 19, 58, 31, 23, 41, 8, 92, 40, 76, 17,
    4, 26, 35, 15, 30, 0, 70, 11, 54, 65, 97, 46, 37, 59, 10, 43, 16, 34, 13, 6,
    80, 45, 28, 84, 2, 20, 39, 71, 53, 49, 87, 57, 47, 32, 98, 64, 90, 51, 75, 93,
    24, 96, 22, 88, 60, 81, 89, 99, 62, 55, 73, 79, 86, 94, 91, 66, 83, 100, 77, 52,
    36, 9, 44, 15, 31, 63, 18, 5, 41, 12, 27, 74, 0, 20, 47, 6, 59, 3, 38, 35, 85, 64,
    10, 25, 28, 14, 21, 8, 97, 43, 11, 83, 19, 24, 80, 90, 13, 4, 7, 2, 33, 99, 37, 1,
    56, 61, 76, 72, 95, 32, 16, 53, 26, 49, 50, 46, 42, 34, 82, 39, 40, 55, 48, 78, 84,
    69, 54, 65, 75, 71, 36, 22, 30, 17, 29, 87, 45, 68, 92, 70, 98, 23, 14, 93, 60, 66,
    91, 67, 89, 79, 73, 58, 96, 62, 88, 57, 25, 6, 8, 19
]
trajanje=[120,120,90,120,120,60,60,90]

# -----------------------------
# DIJAGRAMI
# -----------------------------

import plotext as plt
def vertikalni_barchart():
    plt.bar(zupanije4, stan2021, width =3 / 5)
    plt.title("Broj stanovnika po županijama 2021-vertikalni barchart")
    plt.show()

def horizontalni_barchart():
    plt.bar(zupanije4, stan2021, orientation ="horizontal", width =3 / 5)
    plt.title("Broj stanovnika po županijama 2021-horizontalni barchart")
    plt.show()

def jednostavi_barcahrt():
    plt.simple_bar(zupanije, stan_2021, title='Broj stanovnika po županijama 2021-jednostavni barchart')
    plt.show()

def grupirani_barchart():
    plt.multiple_bar(zupanije4, [stan2021, stan2011, stan2001], labels=["popis 2021", "popis 2011", "popis 2001"], width=1 / 5)
    plt.title("Broj stanovništva po županijama")
    plt.show()

def jednostavni_grupirani():
    plt.simple_multiple_bar(zupanije, [stan_2021, stan_2011, stan_2001], labels=["popis 2021", "popis 2011", "popis 2001"], width=200)
    plt.title("Broj stanovništva po županijama")
    plt.plot_size(100, 40)
    plt.show()

def slozeni_barchart():
    plt.stacked_bar(godine, [muskarci, zene], labels=["muskarci", "zene"])
    plt.title("Omjer žena i muškaraca po popisima")
    plt.show()

def jednostavni_slozeni():
    plt.simple_stacked_bar(godine, [muskarci, zene], labels=["muskarci", "zene"])
    plt.title("Omjer žena i muškaraca po popisima")
    plt.show()

def histogram_vertikalni():
    plt.hist(godine2021, bins=20, color="blue", marker="█", width=2/5)
    plt.title("Raspodjela dobi 2021- Vertikalni histogram")
    plt.xlabel("Godine") #naziv x osi
    plt.ylabel("Broj ljudi") # naziv y osi
    plt.plot_size(520, 40) # radi kada se pokrene u terminalu
    plt.ticks_color('red')# boja okvir i tekst
    plt.ticks_style('bold')
    plt.xlim(0, 100)
    plt.show()

def horizontalni_timeline():# izgleda se kod horizontalne orijentacije automatski sortira redoslijed labela prema abecedi, dok kod vertikalnog barcharta to nije slučaj
        plt.bar(dan_predmet, trajanje, orientation="horizontal", width=0.1, color="cyan", marker="█")
        plt.title("Horizontalna vremenska vrpca")
        plt.xlabel("Minute")
        plt.show()

def jednostavni_timeline():
    plt.simple_bar(dan_predmet, trajanje, width=200, title='Raspored sati od ponedjeljka do četvrtka')
    plt.show()

def vertikalni_timeline():
    plt.bar(dan_predmet, trajanje, width=0.1, color="cyan", marker="█")
    plt.title("Vertikalna vremenska vrpca")
    plt.ylabel("Minute")
    plt.xlabel("Dan i predmet")
    plt.show()

# -----------------------------
# POZIVI (po želji komentiraj/otkomentiraj)
# -----------------------------

#vertikalni_barchart()
#horizontalni_barchart()
#jednostavi_barcahrt()
#grupirani_barchart()
#jednostavni_grupirani()
#slozeni_barchart()
#jednostavni_slozeni()
#histogram_vertikalni()
#horizontalni_timeline()
#jednostavni_timeline()
#vertikalni_timeline()

