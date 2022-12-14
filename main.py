import argparse
import pycountry
parser = argparse.ArgumentParser(description='commands you may use')
parser.add_argument('--filename', '-f', required=True)
parser.add_argument('--medals', '-m', action='store_true', required=False)
parser.add_argument('--total', '-t', action='store_true', required=False)
parser.add_argument('--overall', '-o', action='store_true', required=False)
parser.add_argument('--country', '-c', required=False)
parser.add_argument('--year', '-y', required=False)
parser.add_argument('--interactive', '-i', required=False)
parser.add_argument('--output', '-out', required=False)

args = parser.parse_args()


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

    print(f'in {year_ol},country won {gold} gold, '
          f'{silver} silver and {bronze} bronze medals')


def if_medal(filename, country, year, file_output):
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
                        if file_output is not None:
                            with open(file_output, 'a') as file_o:
                                file_o.write(f'{counter + 1}. {name_athlete} - {sport_athlete} - {medal_line}\n')
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


def if_overall(filename, country):
    dict_countries = {}
    with open(filename, 'r') as file:
        file.readline()
        next_line = file.readline()
        while next_line:
            split_line = next_line.split('\t')
            medal_line = split_line[-1][:-1]
            noc_line = split_line[7]
            year_line = split_line[9]

            if noc_line not in dict_countries:
                dict_countries[noc_line] = {}
            if year_line not in dict_countries[noc_line]:
                dict_countries[noc_line][year_line] = 0
            if medal_line == 'Gold' or medal_line == 'Silver' or medal_line == 'Bronze':
               dict_countries[noc_line][year_line] += 1

            next_line = file.readline()

    max_value = max(dict_countries[country].values())
    max_key = max(dict_countries[country], key=dict_countries[country].get)
    min_value = min(dict_countries[country].values())
    min_key = min(dict_countries[country], key=dict_countries[country].get)

    return max_value, max_key, min_value, min_key


def average(filename, country):
    dict_countries = {}
    with open(filename, 'r') as file:
        file.readline()
        next_line = file.readline()
        while next_line:
            split_line = next_line.split('\t')
            medal_line = split_line[-1][:-1]
            noc_line = split_line[7]
            year_line = split_line[9]

            if noc_line not in dict_countries:
                dict_countries[noc_line] = {}
            if year_line not in dict_countries[noc_line]:
                dict_countries[noc_line][year_line] = [0, 0, 0]

            if medal_line == 'Gold':
                dict_countries[noc_line][year_line][0] += 1
            elif medal_line == 'Silver':
                dict_countries[noc_line][year_line][1] += 1
            elif medal_line == 'Bronze':
                dict_countries[noc_line][year_line][2] += 1

            next_line = file.readline()

    total_golds = 0
    total_silvers = 0
    total_bronzes = 0
    for year in dict_countries[country]:
        total_golds += int(dict_countries[country][year][0])
        total_silvers += int(dict_countries[country][year][1])
        total_bronzes += int(dict_countries[country][year][2])

    average_golds = int(total_golds / len(dict_countries[country]))
    average_silvers = int(total_silvers / len(dict_countries[country]))
    average_bronzes = int(total_bronzes / len(dict_countries[country]))

    print(f'* average medals: gold - {average_golds}, silver - {average_silvers}, bronze - {average_bronzes}')


if args.medals:
    if len(args.country) > 3:
        args.country = pycountry.countries.get(name=args.country).alpha_3
    if_medal(args.filename, args.country, args.year, args.output)
elif args.total:
    if_total(args.filename, args.year)
elif args.overall:
    if len(args.country) > 3:
        args.country = pycountry.countries.get(name=args.country).alpha_3
    maximum = if_overall("olympic_athletes.tsv", args.country)
    max_meds = maximum[0]
    year_max = maximum[1]
    print(f'{args.country}: the best year was {year_max} - country won {max_meds} medals')




