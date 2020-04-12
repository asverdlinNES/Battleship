import random

EMPTY_FIELD = [['1 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['2 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['3 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['4 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['5 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['6 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
LETTERS = 'ABCDEFGHI'
ALL_TURNS = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']


def print_the_field(list):
    print('   A B C D E F G H I')
    for row in list:
        for i in row:
            print(i + '|', end='')
        print()


def letter_to_index(new_turn):
    letter = new_turn[0]
    if letter == 'A':
        l = 1
    elif letter == 'B':
        l = 2
    elif letter == 'C':
        l = 3
    elif letter == 'D':
        l = 4
    elif letter == 'E':
        l = 5
    elif letter == 'F':
        l = 6
    elif letter == 'G':
        l = 7
    elif letter == 'H':
        l = 8
    elif letter == 'I':
        l = 9
    return l


def digit_to_index(new_turn):
    digit = int(new_turn[1]) - 1
    return digit


def add_shot(list, turn):
    l = letter_to_index(turn)
    d = digit_to_index(turn)
    if list[d][l] == 'S':
        list[d][l] = '0'
    elif list[d][l] == '0':
        list[d][l] = '0'
    else:
        list[d][l] = 'x'
    return list[d][l]


def result(list, res, turn, previous_turn):
    if res == '0':
        neighbours_turn = close_neighbours(turn)
        neighbours_previous_turn = close_neighbours(previous_turn)
        for neighbour in neighbours_turn:
            ln = letter_to_index(neighbour)
            dn = digit_to_index(neighbour)
            if list[dn][ln] == 'S':
                return 'Ранил!'
        for neighbour_previous in neighbours_previous_turn:
            lnp = letter_to_index(neighbour_previous)
            dnp = digit_to_index(neighbour_previous)
            if list[dnp][lnp] == 'S':
                return 'Ранил!'
        return 'Убил!'
    else:
        return 'Мимо!'


def result_for_user(list, res, turn, coordinates):
    if res == '0':
        neighbours_turn = close_neighbours(turn)
        for neighbour in neighbours_turn:
            ln = letter_to_index(neighbour)
            dn = digit_to_index(neighbour)
            if list[dn][ln] == 'S':
                coordinates.append(turn)
                return 'Ранил!'
        if coordinates == []:
            return 'Убил!'
        if len(coordinates) >= 1:
            coordinates.clear()
            return 'Скорее всего убил. Но если ты попал в две клетки, то проверь на всякий случай противоположную клетку, вдруг это трехпалубный корабль!'
    else:
        return 'Мимо!'


def end_of_game(list):
    counter = 0
    for row in list:
        for i in row:
            if i == '0':
                counter += 1
    while counter < 10:
        return False
    else: return True


def add_ships(field, string):
    ship_list = string.split()
    for cell in ship_list:
        l = letter_to_index(cell)
        d = digit_to_index(cell)
        field[d][l] = 'S'
    user_field = field
    print()
    print_the_field(user_field)


def place_my_ships(list):
    print('Напишите поля, на которых будет стоять трехпалубный корабль. Например, F6 F5 F4')
    ships = input()
    add_ships(user_field, ships)
    print('Напишите поля, на которых будут стоять два двухпалубных корабля. Например, B1 C1 H3 H4')
    ships = input()
    add_ships(user_field, ships)
    print('Напишите поля, на которых будут стоять три однопалубных корабля. Например, C6 E2 A6')
    ships = input()
    add_ships(user_field, ships)


def print_situation(user_field, field_that_user_sees):
    common_list = []
    for i in range(len(user_field)):
        common_list_row = []
        for j in range(len(user_field[1])):
            common_list_row.append(user_field[i][j])
        common_list_row.append('       ')
        for k in range(len(user_field[1])):
            common_list_row.append(field_that_user_sees[i][k])
        common_list.append(common_list_row)
    print('       Твое поле:             Поле Сани Свердлина:')
    print('   A B C D E F G H I           A B C D E F G H I')
    for row in common_list:
        for i in row:
            if i != '       ':
                print(i + '|', end='')
            else:
                print(i, end='')
        print()


def close_neighbours(cell):
    list_of_neighbours = []
    letter_index_in_LETTERS = letter_to_index(cell[0]) - 1
    cell_digit = int(cell[1])
    if letter_index_in_LETTERS <= 7:
        right_neighbour = LETTERS[letter_index_in_LETTERS + 1] + str(cell_digit)
        list_of_neighbours.append(right_neighbour)
    if letter_index_in_LETTERS >= 1:
        left_neighbour = LETTERS[letter_index_in_LETTERS - 1] + str(cell_digit)
        list_of_neighbours.append(left_neighbour)
    if cell_digit >= 2:
        up_neighbour = LETTERS[letter_index_in_LETTERS] + str(cell_digit - 1)
        list_of_neighbours.append(up_neighbour)
    if cell_digit <= 6:
        down_neighbour = LETTERS[letter_index_in_LETTERS] + str(cell_digit + 1)
        list_of_neighbours.append(down_neighbour)
    return list_of_neighbours


def diagonal_neighbours(cell):
    list_of_neighbours = []
    letter_index_in_LETTERS = letter_to_index(cell[0]) - 1
    cell_digit = int(cell[1])
    if letter_index_in_LETTERS <= 7 and cell_digit >= 2:
        right_up_neighbour = LETTERS[letter_index_in_LETTERS + 1] + str(cell_digit - 1)
        list_of_neighbours.append(right_up_neighbour)
    if letter_index_in_LETTERS >= 1 and cell_digit >= 2:
        left_up_neighbour = LETTERS[letter_index_in_LETTERS - 1] + str(cell_digit - 1)
        list_of_neighbours.append(left_up_neighbour)
    if letter_index_in_LETTERS <= 7 and cell_digit <= 6:
        right_down_neighbour = LETTERS[letter_index_in_LETTERS + 1] + str(cell_digit + 1)
        list_of_neighbours.append(right_down_neighbour)
    if letter_index_in_LETTERS >= 1 and cell_digit <= 6:
        left_down_neighbour = LETTERS[letter_index_in_LETTERS - 1] + str(cell_digit + 1)
        list_of_neighbours.append(left_down_neighbour)
    return list_of_neighbours


demonstration_user_field = [['1 ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', '0'], ['2 ', ' ', ' ', 'S', '0', 'S', ' ', ' ', ' ', ' '], ['3 ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' '], ['4 ', 'S', ' ', ' ', ' ', ' ', 'S', ' ', 'S', ' '], ['5 ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'S', ' '], ['6 ', ' ', 'S', 'S', ' ', 'x', ' ', ' ', ' ', ' '], ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
demonstration_field_user_sees = [['1 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['2 ', ' ', ' ', ' ', '0', ' ', ' ', ' ', ' ', 'x'], ['3 ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x'], ['4 ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' '], ['5 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['6 ', 'x', ' ', '0', 'x', 'x', ' ', ' ', ' ', ' '], ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ']]

print()
print()
print('Привет! Это игра "Морской бой". "Морской бой" с небольшой изюминкой, с которой ты встретишься во время игры')
print()
print('             Вот так выглядит поле:')
print()
print_situation(demonstration_user_field, demonstration_field_user_sees)
print('"S" - клетки, на которых находятся здоровые корабли или их части')
print('"0" - уже убитые корабли или их раненные части')
print('"х" - клетки, по которым были совершены выстрелы мимо')
print()
print('Нажми Enter, чтобы начать')
input()

print('Сначала расположим корабли на вашем поле')
print('В этой игре поле 7х9, 1 трехпалубный кораль, 2 двухпалубных и 3 однопалубных')
print()

user_field = EMPTY_FIELD
print_the_field(user_field)
place_my_ships(user_field)

possible_program_field = [[['1 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['2 ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' '], ['3 ', 'S', ' ', ' ', ' ', ' ', ' ', 'S', 'S', ' '], ['4 ', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['5 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' '], ['6 ', ' ', 'S', 'S', 'S', ' ', ' ', ' ', ' ', ' '], ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ']],
[['1 ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' '], ['2 ', ' ', ' ', 'S', ' ', ' ', ' ', 'S', 'S', ' '], ['3 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['4 ', ' ', 'S', ' ', ' ', 'S', 'S', 'S', ' ', ' '], ['5 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['6 ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' '], ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ']],
[['1 ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' '], ['2 ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', 'S', 'S'], ['3 ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' '], ['4 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['5 ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', 'S', ' '], ['6 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' '], ['7 ', ' ', ' ', 'S', ' ', ' ', 'S', ' ', ' ', ' ']],
[['1 ', ' ', ' ', ' ', ' ', ' ', 'S', 'S', 'S', ' '], ['2 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['3 ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', 'S'], ['4 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S'], ['5 ', 'S', ' ', ' ', ' ', 'S', ' ', ' ', ' ', ' '], ['6 ', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ']],
[['1 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['2 ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' '], ['3 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S'], ['4 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['5 ', ' ', ' ', 'S', ' ', 'S', 'S', ' ', ' ', ' '], ['6 ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', 'S'], ['7 ', ' ', ' ', 'S', ' ', 'S', 'S', ' ', ' ', ' ']],
[['1 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['2 ', ' ', ' ', ' ', ' ', 'S', 'S', ' ', ' ', ' '], ['3 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S'], ['4 ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' ', 'S'], ['5 ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', ' '], ['6 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['7 ', ' ', 'S', 'S', 'S', ' ', 'S', ' ', ' ', ' ']],
[['1 ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' '], ['2 ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' '], ['3 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['4 ', ' ', ' ', 'S', ' ', ' ', ' ', 'S', 'S', 'S'], ['5 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['6 ', ' ', ' ', 'S', 'S', ' ', ' ', 'S', ' ', ' '], ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ']]
]

field_user_sees = [['1 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['2 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['3 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['4 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['5 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['6 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['7 ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


print()
print('Отлично, давай уже играть!')
print('Нажми Enter, чтобы начать')
input()
print()

which_field = random.randint(0, len(possible_program_field) - 1)
program_field = possible_program_field[which_field]
possible_turn_program = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']

count = 0
is_previous_win = 0
coordinates_of_this_ship = []
coordinates_of_program_ship = []

while not end_of_game(user_field):
    program_turn = possible_turn_program[random.randint(0, len(possible_turn_program)-1)]

    while is_previous_win == 1:
        random_neighbour = random.randint(0,len(close_neighbours(previous_shot))-1)
        possible_turn = close_neighbours(previous_shot)[random_neighbour]
        if possible_turn in possible_turn_program:
            program_turn = possible_turn
            break

    print()
    print('             Ход Сани Свердлина - ' + program_turn + ':')
    shot_res = add_shot(user_field, program_turn)

    if shot_res == 'x':
        print('                   === Мимо! ===')
        print()
        print_situation(user_field, field_user_sees)
        possible_turn_program.remove(program_turn)

        while True:
            print()
            print('                     Твой ход:')
            user_turn = input()

            if user_turn in ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']:
                user_result = add_shot(program_field, user_turn)
                print('                   === {} ==='.format(result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship)))
                print()
                user_letter = letter_to_index(user_turn)
                user_digit = digit_to_index(user_turn)

                if result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship) == 'Ранил!' or result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship) == 'Убил!' or result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship) == 'Скорее всего убил. Но на всякий случай проверь противоположную клетку, вдруг это трехпалубный корабль!':
                    field_user_sees[user_digit][user_letter] = '0'
                else:
                    field_user_sees[user_digit][user_letter] = 'x'
                count += 1
                break

            else:
                print('У Сани Свердлина нет такого поля. Введи свой ход еще раз')

    if shot_res == '0':
        previous_shot = program_turn
        print('                   === {} ==='.format(
            result(user_field, add_shot(user_field, program_turn), program_turn, previous_shot)))
        print()
        print_situation(user_field, field_user_sees)
        print()
        possible_turn_program.remove(program_turn)

        if result(user_field, add_shot(user_field, program_turn), program_turn, previous_shot) == 'Ранил!':
            coordinates_of_this_ship.append(program_turn)
            is_previous_win = 1
            previous_shot = program_turn

        elif result(user_field, add_shot(user_field, program_turn), program_turn, previous_shot) == 'Убил!':
            is_previous_win = 0
            previous_shot = program_turn
            coordinates_of_this_ship.append(program_turn)

            for i in coordinates_of_this_ship:
                dia_nei = diagonal_neighbours(i)
                clo_nei = close_neighbours(i)

                for j in range(4):
                    if dia_nei[j] in possible_turn_program:
                        possible_turn_program.remove(dia_nei[j])

                    if clo_nei[j] in possible_turn_program:
                        possible_turn_program.remove(clo_nei[j])

            coordinates_of_this_ship = []

        while True:
            print()
            print('                     Твой ход:')
            user_turn = input()

            if user_turn in ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']:
                user_result = add_shot(program_field, user_turn)
                print('                   === {} ==='.format(result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship)))
                print()
                user_letter = letter_to_index(user_turn)
                user_digit = digit_to_index(user_turn)

                if result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship) == 'Ранил!' or result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship) == 'Убил!' or result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship) == 'Скорее всего убил. Но на всякий случай проверь противоположную клетку, вдруг это трехпалубный корабль!':
                    field_user_sees[user_digit][user_letter] = '0'
                else:
                    field_user_sees[user_digit][user_letter] = 'x'
                count += 1
                break

            else:
                print('У Сани Свердлина нет такого поля. Введи свой ход еще раз')

        while not end_of_game(user_field) and not end_of_game(program_field):
            program_turn = possible_turn_program[random.randint(0, len(possible_turn_program) - 1)]

            while is_previous_win == 1:
                random_neighbour = random.randint(0, len(close_neighbours(previous_shot)) - 1)
                possible_turn = close_neighbours(previous_shot)[random_neighbour]

                neighbours4 = close_neighbours(previous_shot)
                countx = 0

                for i in neighbours4:
                    l4 = letter_to_index(i)
                    d4 = digit_to_index(i)
                    if user_field[d4][l4] == 'x' or user_field[d4][l4] == '0':
                        countx += 1

                if countx == 4:

                    for i in neighbours4:
                        l4 = letter_to_index(i)
                        d4 = digit_to_index(i)

                        if user_field[d4][l4] == '0':
                            previous_shot = i
                            random_neighbour = random.randint(0, len(close_neighbours(previous_shot)) - 1)
                            possible_turn = close_neighbours(previous_shot)[random_neighbour]

                if possible_turn in possible_turn_program:
                    program_turn = possible_turn
                    break

            print()
            print('             Ход Сани Свердлина - ' + program_turn + ':')
            add_shot(user_field, program_turn)
            print('                   === {} ==='.format(
                result(user_field, add_shot(user_field, program_turn), program_turn, previous_shot)))
            print()
            print_situation(user_field, field_user_sees)
            possible_turn_program.remove(program_turn)

            if result(user_field, add_shot(user_field, program_turn), program_turn, previous_shot) == 'Ранил!':
                coordinates_of_this_ship.append(program_turn)
                is_previous_win = 1
                previous_shot = program_turn

            elif result(user_field, add_shot(user_field, program_turn), program_turn, previous_shot) == 'Убил!':
                is_previous_win = 0
                previous_shot = program_turn
                coordinates_of_this_ship.append(program_turn)

                for i in coordinates_of_this_ship:
                    dia_nei = diagonal_neighbours(i)
                    clo_nei = close_neighbours(i)
                    for j in range(len(dia_nei)):
                        if dia_nei[j] in possible_turn_program:
                            possible_turn_program.remove(dia_nei[j])
                    for j in range(len(clo_nei)):
                        if clo_nei[j] in possible_turn_program:
                            possible_turn_program.remove(clo_nei[j])

                coordinates_of_this_ship = []

            while True:
                print()
                print('                     Твой ход:')
                user_turn = input()
                if user_turn in ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']:
                    user_result = add_shot(program_field, user_turn)
                    print('                   === {} ==='.format(
                        result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship)))
                    print()
                    user_letter = letter_to_index(user_turn)
                    user_digit = digit_to_index(user_turn)
                    if result_for_user(program_field, user_result, user_turn,
                                       coordinates_of_program_ship) == 'Ранил!' or result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship) == 'Убил!' or result_for_user(program_field, user_result, user_turn, coordinates_of_program_ship) == 'Скорее всего убил. Но на всякий случай проверь противоположную клетку, вдруг это трехпалубный корабль!':
                        field_user_sees[user_digit][user_letter] = '0'
                    else:
                        field_user_sees[user_digit][user_letter] = 'x'
                    count += 1
                    break
                else:
                    print('У Сани Свердлина нет такого поля. Введи свой ход еще раз')

        else:
            if end_of_game(user_field):
                print('Игра окончена. Я выиграл за {} ходов! Спасибо за игру'.format(count))
            else:
                print('Игра окончена. Ты выиграл за {} ходов! Спасибо за игру'.format(count))
        print_situation(user_field, program_field)

        break

