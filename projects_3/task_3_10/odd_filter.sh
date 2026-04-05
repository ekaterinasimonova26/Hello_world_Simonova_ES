#!/bin/bash

for ((i=1; i<=20; i++)); do
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
    if [ $i -eq 15 ]; then
        break
    fi
    echo $i
done
