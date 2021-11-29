#!/bin/bash

### CONFIGURE VAR
OUTFILE="output.csv"
URL=https://www.google.com/
N=3

while getopts u:n: flag
do
    case "${flag}" in
        u) URL=${OPTARG};;
        n) N=${OPTARG};;
    esac
done

#### START TESTING SCRIPT

echo -e "\n\n[Method1] CURL TEST"
echo "Testing $URL, Output to $OUTFILE"
for i in $(seq 1 1 $N)
do
    echo "$i of $N"
    curl $URL \
        -H "Cache-Control: no-cache, no-store, must-revalidate" \
        -H "Pragma: no-cache" \
        -H "Expires: 0" \
        -w "@curl-format.txt" -o /dev/null -s >> $OUTFILE
done

echo -e "\n\n[Method2] APACHE BECH"
ab -n $N $URL

###  END TESTING SCRIPT