#!/usr/bin/python

import csv

fread = open('banknames.csv', 'r')
#import pandas as pd
#df = pd.read_csv(fread)
#saved_column = df.Name
#print saved_column

from collections import defaultdict
columns = defaultdict(list)
print columns

reader = csv.DictReader(fread)
for row in reader:
    for (k,v) in row.items():
        columns[k].append(v)
print (columns['Name'])

