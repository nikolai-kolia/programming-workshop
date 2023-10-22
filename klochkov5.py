def display_board():
    first_colomn = 1
    s = f'{first_colomn} '
    for x in range(4):
        for y in range(5):
            s += f'| {board[x][y]} | '
            if (y % 5 == 4):
                first_colomn += 1
                print(s)
                s = f'{first_colomn} '
    print('    1     2     3     4     5')


def play_game():
    current_player = 'A'
    game_over = False
    score = {'A': 0, 'B': 0, 'C': 0}
    while not game_over:
        display_board()
        position = input('Выберите координаты (два числа через пробел - столбец, строка): ').split()
        try:
            x, y = int(position[1]) - 1, int(position[0]) - 1
            board[x][y] = current_player
            try:
                if (board[x][y] == board[x + 1][y]):
                    score[current_player] -= 1
            except:
                pass
            try:
                if (board[x][y] == board[x - 1][y]):
                    score[current_player] -= 1
            except:
                pass
            try:
                if (board[x][y] == board[x][y + 1]):
                    score[current_player] -= 1
            except:
                pass
            try:
                if (board[x][y] == board[x][y - 1]):
                    score[current_player] -= 1
            except:
                pass
            try:
                if (board[x][y] == board[x - 1][y - 1]):
                    score[current_player] -= 1
            except:
                pass
            try:
                if (board[x][y] == board[x - 1][y + 1]):
                    score[current_player] -= 1
            except:
                pass
            try:
                if (board[x][y] == board[x + 1][y - 1]):
                    score[current_player] -= 1
            except:
                pass
            try:
                if (board[x][y] == board[x + 1][y + 1]):
                    score[current_player] -= 1
            except:
                pass
            if ' ' not in [y for x in board for y in x]:
                display_board()
                if max([score[_] for _ in score]) == score['A']:
                    print('Игра окончена! Игрок A победил!')
                elif max([score[_] for _ in score]) == score['B']:
                    print('Игра окончена! Игрок B победил!')
                else:
                    print('Игра окончена! Игрок C победил!')
                game_over = True
            else:
                if current_player == 'A':
                    current_player = 'B'
                elif current_player == 'B':
                    current_player = 'C'
                else:
                    current_player = 'A'
        except:
            print('Невозможно выбрать данные координаты.')


board = [[], [], [], []]
for x in range(4):
    for y in range(5):
        board[x].append(' ')
play_game()
