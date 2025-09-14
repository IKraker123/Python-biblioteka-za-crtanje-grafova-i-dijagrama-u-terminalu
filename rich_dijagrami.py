# RICH – dijagrami kreirani pomoću biblioteke Rich

from rich.console import Console
from rich.table import Table
from rich.text import Text


console = Console()

# -----------------------------
# PODACI KOJI SE KORISTE ZA KREIRANJE DIJAGRAMA
# -----------------------------
popis_2021 = {
    "Zagrebačka": 299_985, "Krapinsko-zagorska": 120_702, "Sisačko-moslavačka": 139_603,
    "Karlovačka": 112_195, "Varaždinska": 159_487, "Koprivničko-križevačka": 101_221,
    "Bjelovarska-bilogorska": 101_879, "Primorsko-goranska": 265_419, "Ličko-senjska": 42_748,
    "Virovitičko-podravska": 70_368, "Požeško-slavonska": 64_084, "Brodsko-posavska": 130_267,
    "Zadarska": 159_766, "Osječko-baranjska": 258_026, "Šibensko-kninska": 96_381,
    "Vukovarsko-srijemska": 143_113, "Splitsko-dalmatinska": 423_407, "Istarska": 195_237,
    "Dubrovačko-neretvanska": 115_564, "Međimurska": 105_250, "Grad Zagreb": 767_131
}

popis_2011 = {
    "Zagrebačka": 317_606, "Krapinsko-zagorska": 132_892, "Sisačko-moslavačka": 172_439,
    "Karlovačka": 128_899, "Varaždinska": 175_951, "Koprivničko-križevačka": 115_584,
    "Bjelovarska-bilogorska": 119_764, "Primorsko-goranska": 296_195, "Ličko-senjska": 50_927,
    "Virovitičko-podravska": 84_836, "Požeško-slavonska": 78_034, "Brodsko-posavska": 158_575,
    "Zadarska": 170_017, "Osječko-baranjska": 305_032, "Šibensko-kninska": 109_375,
    "Vukovarsko-srijemska": 179_521, "Splitsko-dalmatinska": 454_798, "Istarska": 208_055,
    "Dubrovačko-neretvanska": 122_568, "Međimurska": 113_804, "Grad Zagreb": 790_017
}

popis_2001 = {
    "Zagrebačka": 309_696, "Krapinsko-zagorska": 142_432, "Sisačko-moslavačka": 185_387,
    "Karlovačka": 141_787, "Varaždinska": 184_769, "Koprivničko-križevačka": 124_467,
    "Bjelovarska-bilogorska": 133_084, "Primorsko-goranska": 305_505, "Ličko-senjska": 53_677,
    "Virovitičko-podravska": 93_389, "Požeško-slavonska": 85_831, "Brodsko-posavska": 176_765,
    "Zadarska": 162_045, "Osječko-baranjska": 330_506, "Šibensko-kninska": 112_891,
    "Vukovarsko-srijemska": 204_768, "Splitsko-dalmatinska": 463_676, "Istarska": 206_344,
    "Dubrovačko-neretvanska": 122_870, "Međimurska": 118_426, "Grad Zagreb": 779_145
}

muskarci_zene = {
    "2001": {"Muškarci": 2_135_900, "Žene": 2_301_560},
    "2011": {"Muškarci": 2_066_335, "Žene": 2_218_554},
    "2021": {"Muškarci": 1_865_129, "Žene": 2_006_704},
}

raspored = {
    "Pon": [
        {"poc": "08:00", "kraj": "10:00", "predmet": "Primjena umjetne inteligencije u poslovanju"},
        {"poc": "10:00", "kraj": "12:00", "predmet": "Otkrivanje znanja u podacima"},
        {"poc": "15:30", "kraj": "17:00", "predmet": "Primjena umjetne inteligencije u poslovanju"},
    ],
    "Uto": [
        {"poc": "10:00", "kraj": "12:00", "predmet": "Komuniciranje i virtualni timovi u organizaciji"},
        {"poc": "13:00", "kraj": "15:00", "predmet": "Inteligentni interaktivni sustavi"},
    ],
    "Sri": [
        {"poc": "15:00", "kraj": "16:00", "predmet": "Inteligentni interaktivni sustavi"},
    ],
    "Čet": [
        {"poc": "08:00", "kraj": "09:00", "predmet": "Komuniciranje i virtualni timovi u organizaciji"},
        {"poc": "18:30", "kraj": "20:00", "predmet": "Otkrivanje znanja u podacima"},
    ]
}

podaci_za_histogram = [
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

# -----------------------------
# POMOĆNE FUNKCIJE
# -----------------------------
def skaliranje_vrijednosti(vrijednosti, width=40):
    m = max(vrijednosti) if vrijednosti else 1
    return [max(0, int(v / m * width)) for v in vrijednosti]


def ispis_naslova(naslov):
    console.rule(f"[bold]{naslov}")

paleta_boja = [
    "red", "green", "yellow", "blue", "magenta", "cyan", "bright_red",
    "bright_green", "bright_yellow", "bright_blue", "bright_magenta", "bright_cyan"
]

# -----------------------------
# DIJAGRAMI
# -----------------------------

def vertikalni_stupcasti():
    podaci = list(popis_2021.items())
    nazivi = [k for k,_ in podaci]
    vrijednosti = [v for _,v in podaci]
    duljina_grafa = skaliranje_vrijednosti(vrijednosti, width=20)
    tablica = Table(title="Broj stanovnika po županijama – 2021 (vertikalni)")
    for _ in nazivi:
        tablica.add_column(justify="center")
    H = max(duljina_grafa) or 1
    for row in range(H, 0, -1):
        cells = []
        for idx, b in enumerate(duljina_grafa):
            boja = paleta_boja[idx % len(paleta_boja)]
            cells.append(f"[{boja}]█[/{boja}]" if b >= row else " ")
        tablica.add_row(*cells)
    tablica.add_row(*[Text("·", style="dim") for _ in nazivi])
    tablica.add_row(*[Text(k[:7], style="bold") for k in nazivi])
    console.print(tablica)

def horizontalni_stupcasti():
    podaci = sorted(popis_2021.items(), key=lambda kv: kv[1], reverse=True)
    tablica = Table(title="Broj stanovnika po županijama – 2021 (horizontalni)")
    tablica.add_column("Županija")
    tablica.add_column("Broj", justify="right")
    tablica.add_column("Graf", justify="left")
    max_sirina = 120
    m = max(v for _, v in podaci)
    for idx, (k, v) in enumerate(podaci):
        n = int(v / m * max_sirina)
        boja = paleta_boja[idx % len(paleta_boja)]
        tablica.add_row(k, f"{v:,}".replace(",", "."), f"[{boja}]" + "█" * n +
                        f"[/{boja}]")
    console.print(tablica)


def grupirani_stupcasti():
    nazivi = list(popis_2021.keys())
    tablica = Table(title="Broj stanovnika po županijama – grouped (2001, 2011, 2021)")
    tablica.add_column("Županija")
    for y in ["2001", "2011", "2021"]:
        tablica.add_column(y, justify="right")
        tablica.add_column(f"Graf {y}", justify="left")
    max_sirina = 35
    for idx, k in enumerate(nazivi):
        v2001, v2011, v2021 = popis_2001[k], popis_2011[k], popis_2021[k]
        lokalni_max = max(v2001, v2011, v2021)
        b2001 = f"[{paleta_boja[0]}]" + "█" * int(v2001 / lokalni_max * max_sirina) + f"[/{paleta_boja[0]}]"
        b2011 = f"[{paleta_boja[4]}]" + "█" * int(v2011 / lokalni_max * max_sirina) + f"[/{paleta_boja[4]}]"
        b2021 = f"[{paleta_boja[8]}]" + "█" * int(v2021 / lokalni_max * max_sirina) + f"[/{paleta_boja[8]}]"
        tablica.add_row(k, f"{v2001:,}".replace(",", "."), b2001,
                         f"{v2011:,}".replace(",", "."), b2011,
                         f"{v2021:,}".replace(",", "."), b2021)
    console.print(tablica)


def slozeni_stupcasti():
    tablica = Table(title="Spol po godinama – složeni stupčasti dijagram")
    tablica.add_column("Godina", justify="center")
    tablica.add_column("Muškarci", justify="right")
    tablica.add_column("Žene", justify="right")
    tablica.add_column("Graf", justify="left")
    max_sirina = 100
    max_ukupno = max((d["Muškarci"] + d["Žene"]) for d in muskarci_zene.values())
    for godina in ["2001", "2011", "2021"]:
        m = muskarci_zene[godina]["Muškarci"]
        z = muskarci_zene[godina]["Žene"]
        linija_m = f"[blue]" + "█" * int(m / max_ukupno * max_sirina) + "[/blue]"
        linija_z = f"[magenta]" + "█" * int(z / max_ukupno * max_sirina) + "[/magenta]"
        tablica.add_row(
            godina,
            f"{m:,}".replace(",", "."),
            f"{z:,}".replace(",", "."),
            linija_m + linija_z
        )
    console.print(tablica)
    legenda = f"[blue]█[/blue] Muškarci   [magenta]█[/magenta] Žene"
    console.print(legenda, justify="center")

def vertikalni_timeline():
    console.rule("Raspored – vertikalna vremenska vrpca")
    predmet_boje = {}
    boja_idx = 0
    for dan, stavke in raspored.items():
        console.print(f"[bold underline]{dan}[/]")
        for sati in range(6, 20):
            sat_oznaka = f"{sati:02}:00"
            predmeti_u_satu = []
            for it in stavke:
                sh, sm = map(int, it["poc"].split(":"))
                eh, em = map(int, it["kraj"].split(":"))
                if sh*60+sm <= sati*60 < eh*60+em:
                    if it["predmet"] not in predmet_boje:
                        predmet_boje[it["predmet"]] = paleta_boja[boja_idx % len(paleta_boja)]
                        boja_idx += 1
                    boja = predmet_boje[it["predmet"]]
                    predmeti_u_satu.append(f"[{boja}]{it['predmet']}[/{boja}]")
            console.print(f"{sat_oznaka} │ {' | '.join(predmeti_u_satu)}")
        console.print()


def horizontalni_timeline():
    tablica = Table(title="Raspored – horizontalna vremenska vrpca")
    tablica.add_column("Dan")
    tablica.add_column("Vrijeme")
    tablica.add_column("Predmet")
    predmet_boje = {}
    boja_idx = 0
    for dan, stavke in raspored.items():
        for it in stavke:
            if it["predmet"] not in predmet_boje:
                predmet_boje[it["predmet"]] = paleta_boja[boja_idx % len(paleta_boja)]
                boja_idx += 1
            boja = predmet_boje[it["predmet"]]
            tablica.add_row(dan, f"{it['poc']}–{it['kraj']}", f"[{boja}]{it['predmet']}[/{boja}]")
    console.print(tablica)

def horizontalni_histogram(broj_intervala = 10):
    gmin, gmax = min(podaci_za_histogram), max(podaci_za_histogram)
    if gmin == gmax: gmin, gmax = gmin - 1, gmax + 1
    korak = (gmax - gmin + 1) / broj_intervala
    duljina = [0] * broj_intervala
    for g in podaci_za_histogram:
        i = int((g - gmin) // korak)
        duljina[i if i < broj_intervala else broj_intervala - 1] += 1
    oznake = [f"{int(gmin + i*korak)}-{int(gmin + (i+1)*korak - 1)}" for i in range(broj_intervala)]
    sirina_oznake = max(map(len, oznake))
    max_sirina=120
    sirina_grafa = max(10, max_sirina - sirina_oznake - 1 - 16)
    # inace se koristi sirina_grafa = max(10, console.size.width - sirina_oznake - 1 - 16), ali radi preglednosti slike se ogranicila sirina
    boje = paleta_boja
    suma_ele = sum(duljina) or 1
    max_broj = max(duljina) or 1
    console.rule("Histogram dobi")
    for i, (lab, broj_vrijednosti) in enumerate(zip(oznake, duljina)):
        n = round(broj_vrijednosti / max_broj * sirina_grafa)
        postotak = broj_vrijednosti / suma_ele * 100
        graf = Text("█" * n, style=boje[i % len(boje)])
        console.print(f"{lab:<{sirina_oznake}} ", graf, f" {broj_vrijednosti:>5}  {postotak:5.2f}%", sep="")


def vertikalni_histogram(broj_intervala = 10, visina=20):
    gmin, gmax = min(podaci_za_histogram), max(podaci_za_histogram)
    if gmin == gmax: gmin, gmax = gmin - 1, gmax + 1
    korak = (gmax - gmin + 1) / broj_intervala
    duljina = [0] * broj_intervala
    for v in podaci_za_histogram:
        i = int((v - gmin) // korak)
        duljina[i if i < broj_intervala else broj_intervala - 1] += 1
    oznake = [f"{int(gmin + i*korak)}-{int(gmin + (i+1)*korak - 1)}" for i in range(broj_intervala)]
    max_broj = max(duljina) or 1
    graf = [round(c / max_broj * visina) for c in duljina]
    v = max(graf) or 1
    boje = paleta_boja
    razine = {max(1, round(p * v)) for p in (0, .25, .5, .75, 1)}
    y_oznaka = lambda lvl: f"{round(lvl / v * max_broj):>5}" if lvl in razine else "     "
    tablica = Table(title="[bold]Histogram dobi[/bold]", box=None)
    tablica.add_column(justify="right", no_wrap=True, min_width=5)
    for oznaka_x in oznake:
        tablica.add_column(justify="center", no_wrap=True, min_width=max(3, len(oznaka_x)))
    for lvl in range(v, 0, -1):
        red = [y_oznaka(lvl)]
        for i, h in enumerate(graf):
            red.append(f"[{boje[i % len(boje)]}]█[/{boje[i % len(boje)]}]" if h >= lvl else " ")
        tablica.add_row(*red)
    tablica.add_row("  0", *[Text(lbl, style="bold") for lbl in oznake])
    console.print(tablica)



# -----------------------------
# POZIVI (po želji komentiraj/otkomentiraj)
# -----------------------------
#ispis_naslova("VERTIKALNI STUPČASTI DIJAGRAM")
#vertikalni_stupcasti()

#ispis_naslova("HORIZONTALNI STUPČASTI DIJAGRAM")
#horizontalni_stupcasti()

#ispis_naslova("GRUPIRANI STUPČASTI DIJAGRAM")
#grupirani_stupcasti()

#ispis_naslova("Složeni stupčasti dijagram (SPOL)")
#slozeni_stupcasti()

#ispis_naslova("VREMENSKA VRPCA – HORIZONTALNA")
#horizontalni_timeline()

#ispis_naslova("VREMENSKA VRPCA – VERTIKALNA")
#vertikalni_timeline()

#ispis_naslova("HISTOGRAM horizontalni")
#horizontalni_histogram()

#ispis_naslova("HISTOGRAM vertikalni")

#vertikalni_histogram()
