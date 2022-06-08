#!/bin/bash

url=$1

/app/modules/binaries/nuclei -l /app/$url-subs -t /app/nuc/ -o /app/results/$url-nuclei.txt

echo "NUCLEI" >> /app/results/$url-output.txt
printf "\n\n" >> /app/results/$url-output.txt

cat /app/results/$url-nuclei.txt | tee -a /app/results/$url-output.txt

printf "\n\n\n" >> /app/results/$url-output.txt
printf "##########################################################################################\n" >> /app/results/$url-output.txt
printf "##########################################################################################" >> /app/results/$url-output.txt
printf "\n\n\n" >> /app/results/$url-output.txt
