import sys

command = sys.argv[1]
country = sys.argv[2]
year = sys.argv[-1]

counter = 0
names = []

with open('olympic_athletes.tsv', 'r') as file:
    file.readline()
    next_line = file.readline()
    while next_line:
        split_line = next_line.split('\t')
        noc_line = split_line[7]
        year_line = split_line[9]
        medal_line = split_line[-1][:-1]
        name_athlete = split_line[1]
        sport_athlete = split_line[-3]

        if country in split_line:
            if year in split_line:
                while counter < 10:
                    if name_athlete not in names and medal_line != 'NA':
                        print(f'{counter + 1}. {name_athlete} - {sport_athlete} - {medal_line}')
                        counter += 1
                        names.append(name_athlete)

                    else:
                        break

        next_line = file.readline()

    if counter < 10:
        print(f'in {year} {country} had only {counter} medalists')


