from random import randint

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

rows = [row1, row2, row3]

symbols = ['X', 'O']

# player_* has a name and symbol, and a flag whose turn it is
# [name, symbol, flag]
player_one = {'name': '', 'symbol': '', 'turn_flag': False, 'wins': 0}
player_two = {'name': '', 'symbol': '', 'turn_flag': False, 'wins': 0}
count = 1

# decides if the game is running or not
is_running = True
game_is_running = True

def mock_data():

    player_one['name'] = 'Marc'
    player_two['name'] = 'Anika'
    player_one['symbol'] = 'X'
    player_two['symbol'] = 'O'

    row1[0] = 'O'
    row2[0] = 'X'
    row3[0] = 'X'

    row1[1] = 'X'
    row2[1] = 'O'
    row3[1] = 'O'

    row1[2] = 'O'
    row2[2] = 'X'
    row3[2] = 'X'



def start():
    """
    Function determines a random value between 0 and 1 to decide which player will start the game.
    :return: void
    """
    number = randint(0, 1)
    if number == 1:
        player_one['turn_flag'] = True
        player_two['turn_flag'] = False
        print(f'{player_one['name']} starts the game.')
    else:
        player_one['turn_flag'] = False
        player_two['turn_flag'] = True
        print(f'{player_two['name']} starts the game.')



def init_welcome_and_rules():
    """
    Function initialises the game, the players and selection of their symbols
    :return: void
    """
    print('###### Welcome to the Tic-Tac-Toe Game! ######')
    print('###### Two players take turns placing their symbols, "X" or "O", on a 3x3 grid. ######')
    print('###### The goal is to be the first to align three symbols in a row. ######')
    print('###### This can be done vertically, horizontally, or diagonally. ######')
    print('###### If all spaces are filled and no one has three in a row, the game ends in a draw. ######')
    print('')
    print('Let\'s start by choosing the players\' names and their symbols...')

    print('Player 1:')
    player_one['name'] = input('What is your name? ')

    while player_one['symbol'] not in symbols:
        player_one['symbol'] = input('What is your symbol? \n(You can choose between "X" and "O")')

    print('Player 2:')

    player_two['name'] = input('What is your name? ')

    if player_one['symbol'] == 'X':
        player_two['symbol'] = 'O'
    else:
        player_two['symbol'] = 'X'

    print(
        f'{player_one['name']} decided to have symbol {player_one['symbol']}, thus {player_two['name']} '
        f'has symbol {player_two['symbol']}.')

    print(f'Player_one: {player_one['name']}, {player_one['symbol']}, {player_one['turn_flag']}, {player_one['wins']}')
    print(f'Player_two: {player_two['name']}, {player_two['symbol']}, {player_two['turn_flag']}, {player_two['wins']}')

    print_board()

def print_board():
    """
    Print the game board
    :return:
    """
    print(f'{row1[0]} | {row1[1]} | {row1[2]}')
    print('--+---+--')
    print(f'{row2[0]} | {row2[1]} | {row2[2]}')
    print('--+---+--')
    print(f'{row3[0]} | {row3[1]} | {row3[2]}')


def set_board_input(player):
    """
    Determine user input and apply to the board
    :param player:
    :return: void
    """
    is_not_occupied = True

    while is_not_occupied:

        row_input = None
        position = None

        while row_input not in range(1, 4):
            row_input = input('At which row you want to place your symbol? \n (You can choose between 1, 2 and 3) ')

            if not row_input.isdigit():
                print(f'{row_input} is not a valid row. Please try again. ')
                continue
            else:
                row_input = int(row_input)

            if row_input in range(1, 4):

                while position not in range(0, 3):
                    position = input('At which position within the row you want to place your symbol? '
                                         '\n (You can choose between 0, 1 and 2) ')

                    if not position.isdigit():
                        print(f'{position} is not a valid position. Please try again. ')
                        continue
                    else:
                        position = int(position)

                    if position in range(0, 3):
                        print(f'Row_input: {row_input}, Position: {position}')

                        print(f'Row {rows[row_input - 1][position]}')
                        if contain_symbol(rows[row_input - 1][position]):
                            print('Location is already occupied. Please choose another one.')
                            row_input = None
                            position = None
                            break
                        else:
                            rows[row_input - 1][position] = player['symbol']
                            is_not_occupied = False
                            break
                    else:
                        print(f'{position} is not a valid position. Please try again. ')
                        position = None

            else:
                print(f'{row_input} is not a valid row. Please try again. ')
                row_input = None

    print_board()

def reset_board():
    for idx, element in enumerate(row1):
        row1[idx] = ' '
    for idx, element in enumerate(row2):
        row2[idx] = ' '
    for idx, element in enumerate(row3):
        row3[idx] = ' '

def new_game():
    """
    Start a new game by resetting the board and setting up the initial game state.
    """
    global count, game_is_running
    reset_board()  # Clear the board
    count = 0  # Reset the move counter
    game_is_running = True  # Set game flag to True
    start()  # Determine who starts the game

def contain_symbol(symbol):
    return symbol in symbols


def row_contain_symbols(lst):
    for element in lst:
        if not contain_symbol(element):
            return False
    return True

def win():
    has_won = False
    winning_combination = []
    # horizontal
    print(row1[0] == row1[1] == row1[2])
    print(row_contain_symbols([row1[0], row1[1], row1[2]]))
    if (row1[0] == row1[1] == row1[2]) and row_contain_symbols([row1[0], row1[1], row1[2]]):
        winning_combination = [row1[0], row1[1], row1[2]]
        has_won = True
    elif (row2[0] == row2[1] == row2[2]) and row_contain_symbols([row2[0], row2[1], row2[2]]):
        winning_combination = [row2[0], row2[1], row2[2]]
        has_won = True
    elif (row3[0] == row3[1] == row3[2]) and row_contain_symbols([row3[0], row3[1], row3[2]]):
        winning_combination = [row3[0], row3[1], row3[2]]
        has_won = True

    # vertical
    elif (row1[0] == row2[0] == row3[0]) and row_contain_symbols([row1[0], row2[0], row3[0]]):
        winning_combination = [row1[0], row2[0], row3[0]]
        has_won = True
    elif (row1[1] == row2[1] == row3[1]) and row_contain_symbols([row1[1], row2[1], row3[1]]):
        winning_combination = [row1[1], row2[1], row3[1]]
        has_won = True
    elif (row1[2] == row2[2] == row3[2]) and row_contain_symbols([row1[2], row2[2], row3[2]]):
        winning_combination = [row1[2], row2[2], row3[2]]
        has_won = True

    # diagonal
    elif (row1[0] == row2[1] == row3[2]) and row_contain_symbols([row1[0], row2[1], row3[2]]):
        winning_combination = [row1[0], row2[1], row3[2]]
        has_won = True
    elif (row1[2] == row2[1] == row3[0]) and row_contain_symbols([row1[2], row2[1], row3[0]]):
        winning_combination = [row1[2], row2[1], row3[0]]
        has_won = True

    if len(winning_combination) > 0 and winning_combination[0] == player_one['symbol']:
        winning_combination.append(player_one)
        player_one['wins'] += 1
    else:
        winning_combination.append(player_two)
        player_two['wins'] += 1



    print(f'winning_combination: {winning_combination}')
    print(f'has_won: {has_won}')

    return winning_combination, has_won


# main
init_welcome_and_rules()

while is_running:

    new_game()

    while game_is_running:
        answer = None
        if count == 9:
            game_is_running = False
            print('Its a Draw. There is no winner.')
            answer = input('Would you play another game? (y/n)')
            while answer not in ['y', 'n']:
                if answer == 'y':
                    count = 0
                    game_is_running = False
                    break
                else:
                    print('The game is finished!')
                    game_is_running = False
                    is_running = False
                    break

        elif player_one['turn_flag']:
            print(f'{player_one['name']}\'s turn:')
            set_board_input(player_one)
            player_one['turn_flag'] = False
            player_two['turn_flag'] = True
            result = win()
            if result[1]:
                print(f'The Winner is {player_one['name']} ')
                while answer not in ['y', 'n']:
                    answer = input('Would you play another game? (y/n)')
                    if answer == 'y':
                        game_is_running = False
                        break
                    else:
                        print('The game is finished!')
                        game_is_running = False
                        is_running = False
                        break
        elif player_two['turn_flag']:
            print(f'{player_two['name']}\'s turn:')
            set_board_input(player_two)
            player_two['turn_flag'] = False
            player_one['turn_flag'] = True
            result = win()
            if result[1]:
                print(f'The Winner is {player_two['name']} ')
                while answer not in ['y', 'n']:
                    answer = input('Would you play another game? (y/n)')
                    if answer == 'y':
                        game_is_running = False
                        break
                    else:
                        print('The game is finished!')
                        game_is_running = False
                        is_running = False
                        break
        count += 1

