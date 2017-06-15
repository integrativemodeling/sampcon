names = "1AVX 1SYX 1I2M 2IDO 7CEI"
#names = "1AVX"

do for [file in names]{ 
reset

set terminal pdfcairo enhanced color font "Arial-Bold, 40" size 10,10
set border lw 5 lc rgb "#484848"

stats sprintf("%s.R1H.txt", file) usi 1 prefix "S1"
stats sprintf("%s.R2H.txt", file) usi 1 prefix "S2"

stats sprintf("%s.R1H.txt", file) usi 2 prefix "C1"
stats sprintf("%s.R2H.txt", file) usi 2 prefix "C2"

max(a, b) = (a > b ? a : b)
min(a, b) = (a <= b ? a : b)

minx = min((int(S1_min) - 0  - (5 + int(S1_min))%5), (int(S2_min) - 0  - (5 + int(S2_min))%5))
maxx = max((int(S1_max) + 5  + (5 - int(S1_max))%5), (int(S2_max) + 5  + (5 - int(S2_max))%5))

miny = min((int(C1_max) - 0  - (50 + int(C1_max))%50), (int(C2_max) - 0  - (50 + int(C2_max))%50))
maxy = max((int(C1_max) + 50 + (50 - int(C1_max))%50), (int(C2_max) + 50 + (50 - int(C2_max))%50))

set boxwidth 0.1 absolute
set style fill empty border rgb "#EB7262"
set style fill empty border rgb "#8666FB"

unset key 

set encoding iso_8859_1
set ylabel "Number of Models" tc rgb "#484848" offset 0.0,0.0 font "Arial-Bold, 57"
set xlabel "Score"     	      tc rgb "#484848" offset 0.0,0.0 font "Arial-Bold, 57"

maxy2 = maxy + 55
set yr [0:maxy2] noreverse nowriteback
set xr [minx:maxx] noreverse nowriteback

set pointsize 2

set xtics minx,(maxx-minx)/4,maxx border in scale 0,0 mirror norotate  offset character 0, 0, 0 autojustify tc rgb "#484848"
set format x "%.2f"
set ytics 0, maxy/4, maxy nomirror tc rgb "#484848"

stats sprintf("%s.CD.txt", file) usi 1 prefix "PV"
stats sprintf("%s.CD.txt", file) usi 2 prefix "CD"

tpv=sprintf("%.2f", PV_mean)
tcd=sprintf("%.2f", CD_mean)

set label sprintf("{/:Italic t}-test p-value: %s\nCohen's {/:Italic d}: %s", tpv, tcd) at graph 0.50, 0.95 right font 'Arial-Bold, 40' front tc rgb "#484848"

set key tc rgb "#484848"
set output sprintf("%s.H.pdf", file)
plot sprintf("%s.R1H.txt", file) usi 1:2 w histeps lw 10 lc rgb "#EB7262" title "Sample 1", \
     sprintf("%s.R2H.txt", file) usi 1:2 w histeps lw 10 lc rgb "#000080" title "Sample 2"
set output
}