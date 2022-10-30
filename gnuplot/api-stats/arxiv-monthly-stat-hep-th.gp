set datafile commentschars "!"

set terminal epslatex standalone size 16cm,10cm
set output "arxiv-monthly-stat-hep-th.tex"

set lmargin at screen 0.15
set pointsize 2
set tics scale 2.3
set mytics 5
set xlabel "Months" offset 0,-3.5
set ylabel "No. of papers"
set xtic rotate by 90 offset 0,-4.2
set yrange [0 to 600]
set key vertical maxrows 5
set key font ",18"
set key at 11.8, 550
set label "hep-th papers on a monthly basis" at -0.5, 550

set style fill solid 1.0 border lt -1
set style histogram clustered
set style data histogram
#set style histogram rowstacked
plot "arxiv-monthly-stat-hep-th.txt"  \
  u 2:xtic(1) t "2015", \
  "" u 3 t "2016", \
  "" u 4 t "2017", \
  "" u 5 t "2018", \
  "" u 6 t "2019", \
  "" u 7 t "2020", \
  "" u 8 t "2021"
 
