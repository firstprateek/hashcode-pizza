#!/bin/bash

for file_path in inputs/*; do
  input_file_name=$(basename $file_path)
  output_file_name=${input_file_name%.*}
  python3 solution.py "$file_path" "outputs/$output_file_name.out"
done
