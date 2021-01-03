#!/bin/bash

declare -a FILES=(
    "pi-hole-whitelist.txt"
    "pi-hole-adlists.txt"
)

for file in "${FILES[@]}"; do
    echo "# $file"
    for url in $(cat "$file"); do
        if ! ping -t 2 -q -c 1 $url 2>&1 > /dev/null ; then
            echo "NOK $url"
        else
            echo "OK $url"
        fi
    done
done
# for file in "${FILES[@]}"; do
#     echo "# $file"
#     for url in $(cat "$file"); do
#         if ! curl --max-time 10 --output /dev/null --silent --head --fail "$url"; then
#             echo "NOK $url"
#         else
#             echo "OK $url"
#         fi
#     done
# done
