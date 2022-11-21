set datafile commentschars "!"

set terminal epslatex standalone size 16cm,10cm
texfile = "inspire-annual-doi-hep-ex.tex"
datfile1 = "inspire-annual-doi-hep-ex-atlas.dat"
datfile2 = "inspire-annual-doi-hep-ex-cms.dat"
set output texfile

set lmargin at screen 0.15
set pointsize 2
set tics scale 2.3
set mytics 5
set xlabel "Year" offset 0,-1
set ylabel "No. of papers"
set xtic rotate by 90 offset 0,-2
set yrange [0 : 150]
set xrange [-1 : 21]

set key at 0, 140 top left
set label "hep-ex papers with DOI" at 0, 120

set style fill solid 1.0 border lt -1
set style data histograms
set style histogram clustered
plot datfile1 using 2:xtic(1) lc rgb "red" title "ATLAS", \
     datfile2 using 2:xtic(1) lc rgb "blue" title "CMS"
