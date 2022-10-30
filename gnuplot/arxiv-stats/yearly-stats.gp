#set datafile commentschars "!"

set terminal epslatex standalone size 16cm,10cm
set output "yearly-stats.tex"

set lmargin at screen 0.15
set pointsize 2
set tics scale 2.3
set mytics 5
set xlabel "Year" offset 0,-1
set ylabel "No. of papers"
set xtic rotate by 90 offset 0,-2
set yrange [0 : 8000]

set label "hep-ph papers using arXiv" at 0, 7400

set style fill solid 1.0 border lt -1
set style data histograms
#set style histogram rowstacked
plot "arxiv-yearly-stats.txt" using 2:xtic(1) notitle lc rgb "red"
