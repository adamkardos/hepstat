#set datafile commentschars "!"

set terminal epslatex standalone size 16cm,10cm
datfile = "inspire-annual-doi-hep-ph-ac-2-to-5-no-atlas-cms-hep-th"
set output sprintf("%s.tex",datfile)

set lmargin at screen 0.15
set pointsize 2
set tics scale 2.3
set mytics 5
set xlabel "Year" offset 0,-1
set ylabel "No. of papers"
set xtic rotate by 90 offset 0,-2
set yrange [0 : 4000]
set xrange [4 : 26]

set label "small collaborations (between 2 and 5 people)" at 4.5, 3750
set label "hep-ph with DOI" at 4.5, 3550

set style fill solid 1.0 border lt -1
set style data histograms
#set style histogram rowstacked
plot sprintf("%s.dat",datfile) using 2:xtic(1) notitle lc rgb "red"
