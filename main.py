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


def if_medal(filename, country, year):
    counter = 0
    names = []
    medals = []

    with open(filename, 'r') as file:
        file.readline()
        next_line = file.readline()
        while next_line:
            split_line = next_line.split('\t')
            medal_line = split_line[-1][:-1]
            name_athlete = split_line[1]
            sport_athlete = split_line[-3]

            if country in split_line and year in split_line:
                if counter < 10:
                    if name_athlete not in names and medal_line != 'NA':
                        print(f'{counter + 1}. {name_athlete} - {sport_athlete} - {medal_line}')
                        counter += 1
                        names.append(name_athlete)
                medals.append(medal_line)
            next_line = file.readline()

        if len(names) == 0:
            print('invalid input (either country or year)')
            quit()

        if counter < 10:
            print(f'in {year} {country} had only {counter} medalists')

        count_medals(medals, year)


def if_total(filename, year):
    dict_countries = {}
    with open(filename, 'r') as file:
        file.readline()
        next_line = file.readline()
        while next_line:
            split_line = next_line.split('\t')
            medal_line = split_line[-1][:-1]
            noc_line = split_line[7]

            if year in split_line and medal_line != 'NA':
                if noc_line not in dict_countries:
                    dict_countries[noc_line] = [0, 0, 0]  # gold-silver-bronze

                if medal_line == 'Gold':
                    dict_countries[noc_line][0] += 1
                elif noc_line in dict_countries and medal_line == 'Silver':
                    dict_countries[noc_line][1] += 1
                elif noc_line in dict_countries and medal_line == 'Bronze':
                    dict_countries[noc_line][2] += 1

            next_line = file.readline()
    if len(dict_countries) == 0:
        print('there was no olympiad that year')
    else:
        for key, value in dict_countries.items():  # iterating items
            print(f'{key}: {value[0]} gold - {value[1]} silver - {value[2]} bronze')


file_name = sys.argv[1]
command = sys.argv[2]
country_c = sys.argv[3]
year_c = sys.argv[-1]

if command == "-medals":
    if_medal(file_name, country_c, year_c)




