#termgraph termgraph_podaci_za_grafove/stupcasti_dijagram.dat --delim ',' --title "Županije 2021 (H)" --color 'red'
#termgraph termgraph_podaci_za_grafove/stupcasti_dijagram.dat --delim ',' --title "Županije 2021 (V)" --vertical
#termgraph termgraph_podaci_za_grafove/grupirani_stupcasti.dat --title "Županije 2001/2011/2021 Grupirani stupcasti dijagram " --color 'blue','red','yellow'
#termgraph termgraph_podaci_za_grafove/slozeni_stupcasti.dat --stacked --title "Spol i godina-Slozeni stupcasti dijagram"
#termgraph termgraph_podaci_za_grafove/vremenska_vrpca.dat --title "Raspored-Horizontalna vremenska vrpca" --color 'blue' --width 60 --custom-tick '█' --format '{:>3.0f} min'
#termgraph termgraph_podaci_za_grafove/vremenska_vrpca.dat --title "Raspored-Vertikalna vremenska vrpca" --color 'blue' --width 60 --custom-tick '█' --format '{:>3.0f} min' --vertical
#termgraph termgraph_podaci_za_grafove/histogram_podaci.dat --histogram --bins 10 --width 60 --title "Dobne skupine 2021-Histogram" --color 'blue'
#termgraph termgraph_podaci_za_grafove/histogram_podaci.dat --histogram --bins 10 --width 60 --title "Dobne skupine 2021 (V)" --vertical
#vertikalni histogram nije podržan