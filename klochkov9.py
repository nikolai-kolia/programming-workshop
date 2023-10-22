from random import randint, choice


def print_board(board):
    first_colomn = 0
    s = f'{first_colomn} '
    for x in range(10):
        for y in range(10):
            s += f'| {board[x][y]} | '
            if (y % 10 == 9):
                first_colomn += 1
                print(s)
                s = f'{first_colomn} '
    print('    A     B     C     D     E     F     G     H     I     J')


def is_valid_position(row, col, size, direction):
    if direction == 'horizontal':
        if col + size > 10:
            return False
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + size + 1):
                if r >= 0 and r < 10 and c >= 0 and c < 10:
                    if board[r][c] != ' ':
                        return False
        return True
    elif direction == 'vertical':
        if row + size > 10:
            return False
        for r in range(row - 1, row + size + 1):
            for c in range(col - 1, col + 2):
                if r >= 0 and r < 10 and c >= 0 and c < 10:
                    if board[r][c] != ' ':
                        return False
        return True
    else:
        return False


def place_ship(row, col, size, direction):
    if direction == 'horizontal':
        for c in range(col, col + size):
            board[row][c] = 'S'
    elif direction == 'vertical':
        for r in range(row, row + size):
            board[r][col] = 'S'


def check_hit(board, x, y):
    if board[x][y] == 'S':
        board[x][y] = 'O'  # Попадание
        return True
    elif board[x][y] == 'O' or board[x][y] == '•':
        print('Вы уже стреляли в эту клетку.')
    else:
        board[x][y] = '•'  # Мимо
        return False


def check_drowning(board, coords_of_hits):
    if len(coords_of_hits) == 1:
        try:
            if board[coords_of_hits[0][0] + 1][coords_of_hits[0][1]] == 'S':
                return False
        except:
            pass
        try:
            if board[coords_of_hits[0][0]][coords_of_hits[0][1] + 1] == 'S':
                return False
        except:
            pass
        try:
            if board[coords_of_hits[0][0] - 1][coords_of_hits[0][1]] == 'S':
                return False
        except:
            pass
        try:
            if board[coords_of_hits[0][0]][coords_of_hits[0][1] - 1] == 'S':
                return False
        except:
            pass
        board[coords_of_hits[0][0]][coords_of_hits[0][1]] = 'X'
        try:
            if board[coords_of_hits[0][0] + 1][coords_of_hits[0][1]] != 'O' or board[coords_of_hits[0][0] + 1][
                coords_of_hits[0][1]] != 'S':
                board[coords_of_hits[0][0] + 1][coords_of_hits[0][1]] = '•'
        except:
            pass
        try:
            if (board[coords_of_hits[0][0] - 1][coords_of_hits[0][1]] != 'O' or board[coords_of_hits[0][0] - 1][
                coords_of_hits[0][1]] != 'S') and coords_of_hits[0][0] - 1 >= 0:
                board[coords_of_hits[0][0] - 1][coords_of_hits[0][1]] = '•'
        except:
            pass
        try:
            if board[coords_of_hits[0][0] + 1][coords_of_hits[0][1] + 1] != 'O' or board[coords_of_hits[0][0] + 1][
                coords_of_hits[0][1] + 1] != 'S':
                board[coords_of_hits[0][0] + 1][coords_of_hits[0][1] + 1] = '•'
        except:
            pass
        try:
            if (board[coords_of_hits[0][0] + 1][coords_of_hits[0][1] - 1] != 'O' or board[coords_of_hits[0][0] + 1][
                coords_of_hits[0][1] - 1] != 'S') and coords_of_hits[0][1] - 1 >= 0:
                board[coords_of_hits[0][0] + 1][coords_of_hits[0][1] - 1] = '•'
        except:
            pass
        try:
            if (board[coords_of_hits[0][0]][coords_of_hits[0][1] - 1] != 'O' or board[coords_of_hits[0][0] + 1][
                coords_of_hits[0][1] - 1] != 'S') and coords_of_hits[0][1] - 1 >= 0:
                board[coords_of_hits[0][0]][coords_of_hits[0][1] - 1] = '•'
        except:
            pass
        try:
            if board[coords_of_hits[0][0]][coords_of_hits[0][1] + 1] != 'O' or board[coords_of_hits[0][0] + 1][
                coords_of_hits[0][1] + 1] != 'S':
                board[coords_of_hits[0][0]][coords_of_hits[0][1] + 1] = '•'
        except:
            pass
        try:
            if (board[coords_of_hits[0][0] - 1][coords_of_hits[0][1] + 1] != 'O' or board[coords_of_hits[0][0] - 1][
                coords_of_hits[0][1] + 1] != 'S') and coords_of_hits[0][0] - 1 >= 0:
                board[coords_of_hits[0][0] - 1][coords_of_hits[0][1] + 1] = '•'
        except:
            pass
        try:
            if (board[coords_of_hits[0][0] - 1][coords_of_hits[0][1] - 1] != 'O' or board[coords_of_hits[0][0] - 1][
                coords_of_hits[0][1] - 1] != 'S') and coords_of_hits[0][0] - 1 >= 0 and coords_of_hits[0][1] - 1 >= 0:
                board[coords_of_hits[0][0] - 1][coords_of_hits[0][1] - 1] = '•'
        except:
            pass
        return True
    '''else:
        for _ in range(len(coords_of_hits)):
            try:
                if board[coords_of_hits[_][0] + 1][coords_of_hits[_][1]] == 'S':
                    return False
            except:
                pass
            try:
                if board[coords_of_hits[_][0]][coords_of_hits[_][1] + 1] == 'S':
                    return False
            except:
                pass
            try:
                if board[coords_of_hits[_][0] - 1][coords_of_hits[_][1]] == 'S':
                    return False
            except:
                pass
            try:
                if board[coords_of_hits[_][0]][coords_of_hits[_][1] - 1] == 'S':
                    return False
            except:
                pass
            if all(board[coords_of_hits[_][0]][coords_of_hits[_][1]] == 'O' for _ in range(len(coords_of_hits))):
                for _ in range(len(coords_of_hits)):
                    board[coords_of_hits[_][0]][coords_of_hits[_][1]] = 'X'
                    try:
                        if board[coords_of_hits[0][0] + 1][coords_of_hits[0][1]] != 'O' and \
                                board[coords_of_hits[0][0] + 1][coords_of_hits[0][1]] != 'S' and \
                                board[coords_of_hits[0][0] + 1][coords_of_hits[0][1]] != 'X':
                            board[coords_of_hits[0][0] + 1][coords_of_hits[0][1]] = '•'
                    except:
                        pass
                    try:
                        if (board[coords_of_hits[0][0] - 1][coords_of_hits[0][1]] != 'O' and
                            board[coords_of_hits[0][0] - 1][coords_of_hits[0][1]] != 'S' and
                            board[coords_of_hits[0][0] - 1][coords_of_hits[0][1]] != 'X') and coords_of_hits[0][
                            0] - 1 >= 0:
                            board[coords_of_hits[0][0] - 1][coords_of_hits[0][1]] = '•'
                    except:
                        pass
                    try:
                        if board[coords_of_hits[0][0] + 1][coords_of_hits[0][1] + 1] != 'O' and \
                                board[coords_of_hits[0][0] + 1][
                                    coords_of_hits[0][1] + 1] != 'S' and board[coords_of_hits[0][0] + 1][
                            coords_of_hits[0][1] + 1] != 'X':
                            board[coords_of_hits[0][0] + 1][coords_of_hits[0][1] + 1] = '•'
                    except:
                        pass
                    try:
                        if (board[coords_of_hits[0][0] + 1][coords_of_hits[0][1] - 1] != 'O' and
                            board[coords_of_hits[0][0] + 1][
                                coords_of_hits[0][1] - 1] != 'S' and board[coords_of_hits[0][0] + 1][
                                coords_of_hits[0][1] - 1] != 'X') and coords_of_hits[0][1] - 1 >= 0:
                            board[coords_of_hits[0][0] + 1][coords_of_hits[0][1] - 1] = '•'
                    except:
                        pass
                    try:
                        if (board[coords_of_hits[0][0]][coords_of_hits[0][1] - 1] != 'O' and
                            board[coords_of_hits[0][0] + 1][
                                coords_of_hits[0][1] - 1] != 'S' and board[coords_of_hits[0][0]][
                                coords_of_hits[0][1] - 1] != 'X') and coords_of_hits[0][1] - 1 >= 0:
                            board[coords_of_hits[0][0]][coords_of_hits[0][1] - 1] = '•'
                    except:
                        pass
                    try:
                        if board[coords_of_hits[0][0]][coords_of_hits[0][1] + 1] != 'O' and \
                                board[coords_of_hits[0][0] + 1][
                                    coords_of_hits[0][1] + 1] != 'S' and board[coords_of_hits[0][0] + 1][
                            coords_of_hits[0][1] + 1] != 'X':
                            board[coords_of_hits[0][0]][coords_of_hits[0][1] + 1] = '•'
                    except:
                        pass
                    try:
                        if (board[coords_of_hits[0][0] - 1][coords_of_hits[0][1] + 1] != 'O' and
                            board[coords_of_hits[0][0] - 1][
                                coords_of_hits[0][1] + 1] != 'S' and board[coords_of_hits[0][0] - 1][
                                coords_of_hits[0][1] + 1] != 'X') and coords_of_hits[0][0] - 1 >= 0:
                            board[coords_of_hits[0][0] - 1][coords_of_hits[0][1] + 1] = '•'
                    except:
                        pass
                    try:
                        if (board[coords_of_hits[0][0] - 1][coords_of_hits[0][1] - 1] != 'O' and
                            board[coords_of_hits[0][0] - 1][
                                coords_of_hits[0][1] - 1] != 'S' and board[coords_of_hits[0][0] - 1][
                                coords_of_hits[0][1] - 1] != 'X') and coords_of_hits[0][0] - 1 >= 0 and \
                                coords_of_hits[0][1] - 1 >= 0:
                            board[coords_of_hits[0][0] - 1][coords_of_hits[0][1] - 1] = '•'
                    except:
                        pass
                return True'''


def check_game_over(board):
    for row in board:
        if 'S' in row:
            return False
    return True


def play_game():
    game_over = False
    coords_of_hits = []
    while not game_over:
        print_board(board)
        coords = input('Введите координаты выстрела (например, A5): ')
        if len(coords) == 2:
            x = int(coords[1])
            y = ord(coords[0].upper()) - ord('A')
            if x >= 0 and x <= 9 and y >= 0 and y <= 9:
                hit = check_hit(board, x, y)
                if hit:
                    coords_of_hits.append((x, y))
                    print('Вы попали в корабль!')
                    if check_drowning(board, coords_of_hits):
                        coords_of_hits = []
                        print('Вы потопили корабль!')
                    if check_game_over(board):
                        game_over = True
                        print_board(board)
                        print('Поздравляем, вы победили!')
                else:
                    print('Вы промахнулись.')
            else:
                print('Некорректные координаты.')
        else:
            print('Некорректный ввод.')


ships = {'1': 4, '2': 3, '3': 3, '4': 2, '5': 2, '6': 2, '7': 1, '8': 1, '9': 1, '10': 1}
board = [[' '] * 10 for _ in range(10)]
for ship, size in ships.items():
    while True:
        row = randint(0, 9)
        col = randint(0, 9)
        direction = choice(['horizontal', 'vertical'])
        if is_valid_position(row, col, size, direction):
            place_ship(row, col, size, direction)
            break
play_game()
