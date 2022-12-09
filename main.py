import sys

def count_medals(medals_list, year_ol):
    gold = 0
    silver = 0
    bronze = 0
    for medal in medals_list:
        if medal == 'Gold':
            gold += 1
        elif medal == 'Silver':
            silver += 1
        elif medal == 'Bronze':
            bronze += 1


    print(f'in {year_ol}, the country won {gold} gold, '
          f'{silver} silver and {bronze} bronze medals')

command = sys.argv[1]
country = sys.argv[2]
year = sys.argv[-1]

counter = 0
names = []
medals = []

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

                medals.append(medal_line)

        next_line = file.readline()

    if len(names) == 0:
        print('invalid input (either country or year)')
        quit()

    if counter < 10:
        print(f'in {year} {country} had only {counter} medalists')

    count_medals(medals, year)


