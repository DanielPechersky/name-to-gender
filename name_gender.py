#!/usr/bin/env python3
import csv
import sys
from glob import glob
from collections import namedtuple

name = sys.argv[2].casefold()

categories = []
category_tuple = namedtuple('category_weighting', ('category', 'weighting'))

for category_file_path in glob(sys.argv[1]+'/*.csv'):
    category = category_file_path.split('/')[-1][:-len('.csv')]
    with open(category_file_path) as f:
        for row in csv.DictReader(f):
            if name==row['name']:
                categories.append(category_tuple(category=category, weighting=int(row['number'])))

categories.sort(key=lambda category: category.weighting, reverse=True)

print(categories[0].category if len(categories) > 0 and (len(categories) == 1 or (len(sys.argv) > 3 and categories[0].weighting / categories[1].weighting > float(sys.argv[3]))) else "")