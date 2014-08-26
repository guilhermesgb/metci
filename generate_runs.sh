#!/bin/bash

mkdir treatments
for i in `seq 0 8`; do
    mkdir treatments/treatment_$i
    for j in `seq 0 9`; do
        mkdir treatments/treatment_$i/run_$j
        python generate_files.py $j treatments/treatment_$i/run_$j 
    done
done
