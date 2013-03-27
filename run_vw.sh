#!/bin/bash

# a script for running validation

vw -d results/train.vw -c -k -f model --passes 20 --l1 0.0000001

vw -t -d results/valid.vw -c -i model -p results/p.txt --l1 0.0000001

python mae.py results/valid.vw results/p.txt

# MAE: 7148.75808773
