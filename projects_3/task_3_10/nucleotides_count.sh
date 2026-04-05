#!/bin/bash

printf "%-20s %-8s %-8s %-8s %-8s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do
    [ -f "$file" ] || continue
    if [ ! -s "$file" ]; then
        continue
    fi
    
    sequence=$(grep -v "^>" "$file" | tr -d '\n' | tr -d ' \t\r')
    
    A_count=$(echo "$sequence" | grep -o "A" | wc -l)
    T_count=$(echo "$sequence" | grep -o "T" | wc -l)
    G_count=$(echo "$sequence" | grep -o "G" | wc -l)
    C_count=$(echo "$sequence" | grep -o "C" | wc -l)
    
    printf "%-20s %-8s %-8s %-8s %-8s\n" "$file" "$A_count" "$T_count" "$G_count" "$C_count"
done
