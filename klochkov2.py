def display_board():
    print('-------------')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('-------------')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print('-------------')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print('-------------')


def check_win(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def play_game():
    current_player = 'X'
    game_over = False
    while not game_over:
        display_board()
        position = int(input('Выберите позицию от 1 до 9: ')) - 1
        if position >= 0 and position <= 8 and board[position] == ' ' :
            board[position] = current_player
            if check_win(current_player):
                display_board()
                print(f'Игра окончена! Игрок {current_player} победил!')
                game_over = True
            elif ' ' not in board:
                display_board()
                print('Игра окончена! Ничья!')
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Некорректный ход. Попробуйте снова.')


board = [' ' for _ in range(9)]
play_game()
