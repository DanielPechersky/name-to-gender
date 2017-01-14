#!/usr/bin/env python3
import csv
import sys
import os

os.makedirs(sys.argv[3], exist_ok=True)

genders = {'male': sys.argv[1], 'female':sys.argv[2]}

for gender in genders:
    with open(f'{sys.argv[3]}/{gender}.csv','w') as out:
        writer = csv.DictWriter(out, ('name', 'number'))
        writer.writeheader()
        with open(genders[gender],'r') as in_:
            for in_row in in_:
                name, _frequency, number, _rank = in_row.split('	')
                writer.writerow({'name': name.casefold(), 'number': int(number.replace(',',''))})
