#set datafile commentschars "!"

set terminal epslatex standalone size 16cm,10cm
datfile = "inspire-annual-doi-hep-th-ac-6-to-10-no-atlas-cms-hep-ph"
set output sprintf("%s.tex",datfile)

set lmargin at screen 0.15
set pointsize 2
set tics scale 2.3
set mytics 5
set xlabel "Year" offset 0,-1
set ylabel "No. of papers"
set xtic rotate by 90 offset 0,-2
set yrange [0 : 100]
set xrange [4 : 26]

set label "medium collaborations (between 6 and 10 people)" at 4.5, 93
set label "hep-th with DOI" at 4.5, 88

set style fill solid 1.0 border lt -1
set style data histograms
#set style histogram rowstacked
plot sprintf("%s.dat",datfile) using 2:xtic(1) notitle lc rgb "red"
