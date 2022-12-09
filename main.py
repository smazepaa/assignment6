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


file_name = sys.argv[1]
command = sys.argv[2]
country_c = sys.argv[3]
year_c = sys.argv[-1]

if command == "-medals":
    if_medal(file_name, country_c, year_c)




