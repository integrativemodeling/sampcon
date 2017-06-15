names = "1AVX 1SYX 1I2M 2IDO 7CEI"
#names = "1AVX"

do for [file in names]{ 
reset
set terminal pdfcairo enhanced color font "Arial-Bold, 40" size 10,10
set border lw 5 lc rgb "#484848"

stats sprintf("%s.CP.txt", file) usi 1 prefix "P1"
stats sprintf("%s.ZH.txt", file) usi 1 prefix "D1"
stats sprintf("%s.ZH.txt", file) usi 2 prefix "M1"

max(a, b) = (a > b ? a : b)
min(a, b) = (a <= b ? a : b)

maxx = (int(D1_max) + 5  + (5 - int(D1_max))%5)
maxy = (int(M1_max) + 25 + (25 - int(M1_max))%25)
set xr [0:maxx] noreverse nowriteback
set yr [0:maxy] noreverse nowriteback

set linetype 5 dashtype 2 lw 10
set arrow nohead from  P1_max,0 to P1_max,maxy  lt 5 lc rgb "red"

unset key 
set pointsize 2
set xtics 0,maxx/4,maxx border in scale 0,0 mirror norotate  offset character 0, 0, 0 autojustify tc rgb "#484848"
set xtics   ()
set ytics 0, maxy/4, maxy  nomirror tc rgb "#484848"
set format x "%.1f"

set encoding iso_8859_1
set ylabel "Number of Models" tc rgb "#484848" offset 0,0 font "Arial-Bold, 57"
set xlabel "Distance to nearest \nIMP cluster centroid model ({\305})" tc rgb "#484848" offset 0,0 font "Arial-Bold, 48"

set key tc rgb "#484848"
set output sprintf("%s_Zdock.pdf", file)
plot sprintf("%s.ZH.txt", file) usi 1:2 w histeps lw 10 lc rgb "#111111" notitle

set output
}