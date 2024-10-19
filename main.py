"""
Module contains the actual game flow of the game tic-tac-toe.
"""
import helpers

if __name__ == "__main__":
    cells = [' '] * 10
    player_one = {'player': 'Player1',
                  'name': '', 'symbol': '', 'turn_flag': False, 'wins': 0}
    player_two = {'player': 'Player2',
                  'name': '', 'symbol': '', 'turn_flag': False, 'wins': 0}
    helpers.print_rules(cells)
    helpers.set_names_and_symbol(player_one, player_two)
    while True:
        helpers.whose_start(player_one, player_two)
        GAME_IS_RUNNING = True
        print(player_one)
        print(player_two)
        while GAME_IS_RUNNING:
            if player_one['turn_flag']:
                print(f"{player_one['name']}\'s turn: ")
                helpers.set_input_to_board(cells, player_one)
                helpers.print_board_game(cells)
                if helpers.victory(cells, player_one):
                    print(f'{player_one['name']} has won!')
                    helpers.increment_wins(player_one)
                    break
                if helpers.check_board_is_full(cells):
                    print('Draw!')
                    break
                helpers.switch_turn_flags(player_one, player_two)

            else:
                print(f"{player_two['name']}\'s turn: ")
                helpers.set_input_to_board(cells, player_two)
                helpers.print_board_game(cells)
                if helpers.victory(cells, player_two):
                    print(f'{player_two['name']} has won!')
                    helpers.increment_wins(player_two)
                    break
                if helpers.check_board_is_full(cells):
                    print('Draw!')
                    break
                helpers.switch_turn_flags(player_one, player_two)

        if not helpers.new_game(cells):
            break
