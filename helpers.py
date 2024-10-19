"""
Module contains all the functions that are needed for the game tic-tac-toe.
"""
import re
from random import randint


def print_board_game(cells):
    """
    Print the board for the game
    """
    print(f'\t\t{cells[7]} | {cells[8]} | {cells[9]}')
    print('\t\t--+---+--')
    print(f'\t\t{cells[4]} | {cells[5]} | {cells[6]}')
    print('\t\t--+---+--')
    print(f'\t\t{cells[1]} | {cells[2]} | {cells[3]}')


def print_board_manual(cells):
    """
    Print the board for the manual
    """
    print('\ty')
    print('\t^')
    print(f'3\t|\t{cells[7]} | {cells[8]} | {cells[9]}')
    print('\t|\t--+---+--')
    print(f'2\t|\t{cells[4]} | {cells[5]} | {cells[6]}')
    print('\t|\t--+---+--')
    print(f'1\t|\t{cells[1]} | {cells[2]} | {cells[3]}')
    print('\t----------------> x')
    print('\t\t1\t2\t3')


def get_user_input():
    """
    Get input of user - check if input is valid coordinates
    :return: tuple of coordinates
    """
    while True:
        coordinate_input = (
            input('Please enter coordinates for placing your symbol: '
                  '\n (You can choose between 1,1 and 3,3) '))

        is_coordinate_valid = (
            re.fullmatch("[1-3],[1-3]", coordinate_input))

        if is_coordinate_valid:
            lst = coordinate_input.split(',')
            return int(lst[0]), int(lst[1])


def get_cell_idx(x_coordinate, y_coordinate):
    """
    Function to transform coordinates to cell
    :param x_coordinate: X-coordinate
    :param y_coordinate: Y-coordinate
    :return: None if coordinates hit no cell
    """
    coordinates_to_cell = {
        (1, 1): 1, (2, 1): 2, (3, 1): 3,
        (1, 2): 4, (2, 2): 5, (3, 2): 6,
        (1, 3): 7, (2, 3): 8, (3, 3): 9
    }

    return coordinates_to_cell.get((x_coordinate, y_coordinate), None)


def is_cell_engaged(cell):
    """
    Return True or False whether the cell is already engaged or not
    :param cell: the monitoring cell
    :return: True if cell is engaged, False if cell is not engaged
    """
    return cell in ['X', 'O']


def set_input_to_board(cells, player_dictionary):
    """
    Function to set user input to board
    :param cells: Game board
    :param player_dictionary: Dictionary to hold information of the player
    """
    while True:
        coordinates = get_user_input()
        cell_idx = get_cell_idx(coordinates[0], coordinates[1])

        if not is_cell_engaged(cells[cell_idx]):
            cells[cell_idx] = player_dictionary['symbol']
            break

        print(f'Cell is already engaged with symbol {cells[cell_idx]}.'
              f' Please enter new coordinates')


def victory(cells, player_dictionary):
    """
    Checks if a player has won
    :param cells: Game board
    :param player_dictionary: Dictionary to hold information of the player
    :return: True if a player has won, False if a player hasn't won so far
    """
    return (
        (cells[1] == player_dictionary['symbol'] and
         cells[2] == player_dictionary['symbol'] and
         cells[3] == player_dictionary['symbol']) or
        (cells[4] == player_dictionary['symbol'] and
         cells[5] == player_dictionary['symbol'] and
         cells[6] == player_dictionary['symbol']) or
        (cells[7] == player_dictionary['symbol'] and
         cells[8] == player_dictionary['symbol'] and
         cells[9] == player_dictionary['symbol']) or
        (cells[1] == player_dictionary['symbol'] and
         cells[4] == player_dictionary['symbol'] and
         cells[7] == player_dictionary['symbol']) or
        (cells[2] == player_dictionary['symbol'] and
         cells[5] == player_dictionary['symbol'] and
         cells[8] == player_dictionary['symbol']) or
        (cells[3] == player_dictionary['symbol'] and
         cells[6] == player_dictionary['symbol'] and
         cells[9] == player_dictionary['symbol']) or
        (cells[1] == player_dictionary['symbol'] and
         cells[5] == player_dictionary['symbol'] and
         cells[9] == player_dictionary['symbol']) or
        (cells[7] == player_dictionary['symbol'] and
         cells[5] == player_dictionary['symbol'] and
         cells[3] == player_dictionary['symbol'])
    )


def increment_wins(player_dictionary):
    """
    Increment wins of the player
    :param player_dictionary:
    """
    player_dictionary['wins'] += 1


def print_rules(cells):
    """
    Initialises the rules of the game
    :return: void
    """
    print('###### Welcome to the Tic-Tac-Toe Game! ######')
    print('###### Two players take turns placing their symbols, "X" or "O", on'
          ' a 3x3 grid. ######')
    print('###### The goal is to be the first to align three symbols in a row.'
          '######')
    print('###### This can be done vertically, horizontally, or diagonally.'
          '######')
    print('###### If all spaces are filled and no one has three in a row, the'
          ' game ends in a draw. ######')
    print('')
    print_board_manual(cells)
    print('')
    print('Let\'s start by choosing the players\' names and their symbols...')


def set_names_and_symbol(player_dict1, player_dict2):
    """
    Function to set the names and symbols of the players
    :param player_dict1: Dictionary to hold information of the player1
    :param player_dict2: Dictionary to hold information of the player2
    :return:
    """
    player_dict1['name'] = input(f'What is your name '
                                 f'{player_dict1['player']}? ')

    while player_dict1['symbol'] not in ['X', 'O']:
        player_dict1['symbol'] = input('What is your symbol?'
                                       '\n(You can choose'
                                       'between "X" and "O") ')
    if player_dict1['symbol'] == 'X':
        player_dict2['symbol'] = 'O'
    else:
        player_dict2['symbol'] = 'X'

    player_dict2['name'] = input(f'What is your name '
                                 f'{player_dict2['player']}? ')

    while player_dict1['symbol'] not in ['X', 'O']:
        player_dict1['symbol'] = input('What is your symbol?'
                                       '\n(You can choose between'
                                       '"X" and "O") ')


def whose_start(player_dict1, player_dict2):
    """
    Function to determine a random value between 0 and 1 to decide which player
    start the game.
    :return: void
    """
    number = randint(0, 1)
    if number == 1:
        player_dict1['turn_flag'] = True
        player_dict2['turn_flag'] = False
        print(f'##### {player_dict1['name']} starts the game. #####')
    else:
        player_dict1['turn_flag'] = False
        player_dict2['turn_flag'] = True
        print(f'##### {player_dict2['name']} starts the game. #####')


def check_board_is_full(cells):
    """
    Function to check if all cells are engaged
    :return: True if all cells are engaged, False if all cells aren't engaged
    """
    for cell in cells:
        if cell not in ['X', 'O']:
            return False
    return True


def new_game(cells):
    """
    Function to decide if players want to play a new game
    :return: True if players want to play a new game, False if the want not
    play a new game.
    """
    answer = ''
    while answer not in ['y', 'n']:
        answer = input('Would you play another game? (y/n)')

    if answer == 'y':
        reset_board_game(cells)
        return True
    return False

def switch_turn_flags(player_dict1, player_dict2):
    """
    Function to switch the turn flag of the players in order to decide which
    player's turn
    :param player_dict1: Dictionary to hold information of the player1
    :param player_dict2: Dictionary to hold information of the player2
    """
    if player_dict1['turn_flag']:
        player_dict1['turn_flag'] = False
        player_dict2['turn_flag'] = True
    else:
        player_dict1['turn_flag'] = True
        player_dict2['turn_flag'] = False


def reset_board_game(cells):
    """
    Function to reset the board
    :param cells: Game board
    """
    for idx in enumerate(cells):
        cells[idx] = ' '
