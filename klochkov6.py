def display_board(board):
    first_colomn = 0
    s = f'{first_colomn} '
    for x in range(len(board)):
        for y in range(len(board[x])):
            s += f'| {board[x][y]} | '
            if (y % 10 == 9):
                first_colomn += 1
                print(s)
                s = f'{first_colomn} '
    print('    0     1     2     3     4     5      6    7     8     9')


def is_valid_move(x, y):
    if x < 0 or x >= 10 or y < 0 or y >= 10:
        return False
    if board[x][y] != ' ':
        return False
    return True


def check_lose(x, y):
    try:
        if (board[x][y] != ' ' and board[x + 1][y] != ' ' and board[x + 2][y] != ' '):
            return True
    except:
        pass
    try:
        if (board[x][y] != ' ' and board[x - 1][y] != ' ' and board[x - 2][y] != ' '):
            return True
    except:
        pass
    try:
        if (board[x][y] != ' ' and board[x][y + 1] != ' ' and board[x][y + 2] != ' '):
            return True
    except:
        pass
    try:
        if (board[x][y] != ' ' and board[x][y - 1] != ' ' and board[x][y - 2] != ' '):
            return True
    except:
        pass
    try:
        if (board[x][y] != ' ' and board[x - 1][y - 1] != ' ' and board[x - 2][y - 2] != ' '):
            return True
    except:
        pass
    try:
        if (board[x][y] != ' ' and board[x + 1][y + 1] != ' ' and board[x + 2][y + 2] != ' '):
            return True
    except:
        pass
    try:
        if (board[x][y] != ' ' and board[x + 1][y - 1] != ' ' and board[x + 2][y - 2] != ' '):
            return True
    except:
        pass
    try:
        if (board[x][y] != ' ' and board[x - 1][y + 1] != ' ' and board[x - 2][y + 2] != ' '):
            return True
    except:
        pass
    return False


def play_game():
    player = 'X'
    game_over = False
    while not game_over:
        display_board(board)
        print(f"Ход игрока {player}")
        while True:
            try:
                x = int(input("Введите номер строки: "))
                y = int(input("Введите номер столбца: "))
                if not is_valid_move(x, y):
                    print("Некорректный ход. Попробуйте снова.")
                    continue
                break
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")
        board[x][y] = player
        if check_lose(x, y):
            display_board(board)
            print(f"Игра окончена! Победитель: {'O' if player == 'X' else 'X'}")
            game_over = True
        player = 'O' if player == 'X' else 'X'


board = [[' ' for _ in range(10)] for _ in range(10)]
play_game()
