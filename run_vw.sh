#!/bin/bash

# a script for running validation

vw -d results/train.vw -c -k -f model --passes 20

vw -t -d results/valid.vw -c -i model -p results/p.txt

python mae.py results/valid.vw results/p.txt

# MAE: 7148.75808773
