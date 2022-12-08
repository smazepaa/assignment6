import sys

command = sys.argv[1]
country = sys.argv[2]
year = sys.argv[-1]

with open('olympic_athletes.tsv', 'r') as file:
    next_line = file.readline()
    while next_line:
        next_line = file.readline()
        split_line = next_line.split('\t')
        noc_line = split_line[7]
        year_line = split_line[9]
        medal_line = split_line[-1][:-1]
        name_athlete = split_line[1]
        sport_athlete = split_line[-3]


