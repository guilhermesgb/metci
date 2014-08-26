#!/bin/bash

for i in `seq 0 8`; do
    for j in `seq 1 9`; do
        if (($i % 3 == 0)); then
            ALG=list
        fi
        if (($i % 3 == 1)); then
            ALG=hashmap
        fi
        if (($i % 3 == 2)); then
            ALG=binarytree
        fi      
        python dictionary.py $ALG treatments/treatment_$i/run_$j/dict.txt treatments/treatment_$i/run_$j/lookup.txt > treatments/treatment_$i/run_$j/result
    done
done
