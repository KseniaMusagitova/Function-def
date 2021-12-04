# 1 задача
def shutdown(p1, p2):
    diff = p1.find('B') - p2.find('B')
    if diff < 0:
        return 'p1'
    elif diff > 0:
        return 'p2'
    else:
        return 'tie'


print(shutdown('  Bang!', '   Bang!'))
print(shutdown('    Bang!', ' Bang!'))
print(shutdown('  Bang!', '  Bang!'))


# 2 задача (ханойские башни)
def solve_hanoi_tower(discs):
    return 2 ** discs - 1


print(solve_hanoi_tower(10))


# 3 задача (определение дуплетов)
def calc_dice_scores(lst):
    return sum([a + b for a, b in lst]) if not any([a == b for a, b in lst]) else 0


print(calc_dice_scores([(4, 5), (4, 5), (4, 5)]))


# 4 задача (мини-судоку)
def any_duplicates(square):
    plain = [i for x in square for i in x]
    return sorted(plain) != [1, 2, 3, 4, 5, 6, 7, 8, 9]


# дубликатов нет
a = any_duplicates([[1, 3, 5], [2, 7, 8], [4, 6, 9]])
print(a)
# есть дубликат
b = any_duplicates([[1, 1, 5], [2, 7, 8], [4, 6, 9]])

# 5 задача (Игра в палочки: есть 10 палочек. Игроки по очереди
# берут от одной до трёх палочек. Играют до тех пор пока не
# закончатся палочки. Тот кто взял последним - тот проиграл)

# 1 способ
number_of_sticks = 10
player_turn = 1
while number_of_sticks > 0:
    print(f'How many sticks you take? Remaining {number_of_sticks} ')
    taken = int(input()) # количество палочек, которое взял игрок

    if taken < 1 or taken > 3:
        print(f'You tried to take {taken}. Allowed to take 1, 2, 3, sticks')
        continue

    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if number_of_sticks <= 0:
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost')

    player_turn = 1 if player_turn == 2 else 2

# 2 способ
number_of_sticks = 10
player_turn = 1


def can_take(sticks):
    return 1 <= sticks <= 3


def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2


def end_of_game(sticks):
    return sticks <= 0


while (not end_of_game(number_of_sticks)):
    print(f'How many sticks you take? Remaining {number_of_sticks} ')
    taken = int(input())  # количество палочек, которое взял игрок

    if not can_take(taken):
        print(f'You tried to take {taken}. Allowed to take 1, 2, 3, sticks')
        continue

    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if end_of_game(number_of_sticks):
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost')
        break

    player_turn = switch_player_turn(player_turn)




