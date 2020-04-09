# read and write using CSV module

"""import csv

with open('simple.txt') as csv_file:
    csv_reder = csv.reader(csv_file, delimiter =',')
    line_count = 0
    for row in csv_reder:
        if line_count == 0:
          print(f'culmn name are {",".join(row)}')
          line_count += 1

"""

# read and write using CSV files

import pandas
pread = pandas.read_csv('simpledata.csv')
print(pread)