#!/bin/bash
declare -a input=("a_example.in" "b_small.in" "c_medium.in" "d_big.in")

for file_name in "${input[@]}"
do
  python3 solution.py "$file_name" "output_$file_name"
done
