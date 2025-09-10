# TERMGRAPH – dijagrami kreirani pomoću biblioteke Termgraph
# Kod unositi izravno u terminal, sve osim znaka #

# Horizontalni stupcasti dijagram
#termgraph termgraph_podaci_za_grafove/stupcasti_dijagram.dat --title "Županije 2021 (H)" --color 'red'

# Vertikalni stupcasti dijagram
#termgraph termgraph_podaci_za_grafove/stupcasti_dijagram.dat  --title "Županije 2021 (V)" --color 'red' --vertical

# Grupirani stupcasti dijagram
#termgraph termgraph_podaci_za_grafove/grupirani_stupcasti.dat --title "Županije 2001/2011/2021 Grupirani stupcasti dijagram " --color 'blue','red','yellow' --width 100

# Slozeni stupcasti dijagram
#termgraph termgraph_podaci_za_grafove/slozeni_stupcasti.dat --stacked --title "Spol i godina-Slozeni stupcasti dijagram"

# Horizontalna vremenska vrpca
#termgraph termgraph_podaci_za_grafove/vremenska_vrpca.dat --title "Raspored-Horizontalna vremenska vrpca" --color 'blue' --width 60 --format '{:>3.0f} min'

# Vertikalna vremenska vrpca- nije prikazana u završnome radu jer je neupotrebljiva zbog neurednosti
#termgraph termgraph_podaci_za_grafove/vremenska_vrpca.dat --title "Raspored-Vertikalna vremenska vrpca" --color 'blue' --width 60 --format '{:>3.0f} min' --vertical

# Horizontalni histogram
#termgraph termgraph_podaci_za_grafove/histogram_podaci.dat --histogram --bins 10 --width 60 --title "Dobne skupine 2021-Histogram" --color 'blue'

#vertikalni histogram nije podržan
#termgraph termgraph_podaci_za_grafove/histogram_podaci.dat --histogram --bins 10 --width 60 --title "Dobne skupine 2021 (V)" --vertical
