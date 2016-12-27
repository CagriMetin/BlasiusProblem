#!/bin/bash

foamLog log.icoFoam >/dev/null

gnuplot -persist > /dev/null 2>&1 << EOF
        set logscale y
        set title "Residual vs. time"
        set xlabel "time"
        set ylabel "Residual"
        plot "logs/Ux_0" with lines,\
             "logs/Uy_0" with lines,\
             "logs/p_0" with lines
call "save_plot" "output_filename" "size 1600,900" 
EOF
