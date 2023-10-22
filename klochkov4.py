def display_board():
    first_colomn = 1
    s = f'{first_colomn} '
    for x in range(len(board)):
        for y in range(len(board[x])):
            s += f'| {board[x][y]} | '
            if (y % 9 == 8):
                first_colomn += 1
                print(s)
                s = f'{first_colomn} '
        if len(board[x]) < 9:
            print(s)
    print('    1     2     3     4     5      6    7     8     9')


def play_game():
    game_over = False
    while not game_over:
        display_board()
        print('Выберите координаты чисел либо напишите "+", чтобы добавить числа')
        first_position = input('Выберите координаты первого числа (два числа через пробел - столбец, строка): ').split()
        if first_position == ['+']:
            l = []
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y] != ' ':
                        l.append(board[x][y])
                    if len(l) == 9:
                        board.append(l)
                        l = []
            if l != []:
                board.append(l)
            continue
        second_position = input('Выберите координаты второго числа (два числа через пробел - столбец, строка): ').split()
        if second_position == ['+']:
            l = []
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y] != ' ':
                        l.append(board[x][y])
                    if len(l) == 9:
                        board.append(l)
                        l = []
            if l != []:
                board.append(l)
            continue
        try:
            if first_position != second_position:
                x1, x2, y1, y2 = int(first_position[1]) - 1, int(second_position[1]) - 1, int(
                    first_position[0]) - 1, int(second_position[0]) - 1
                first_number = board[x1][y1]
                second_number = board[x2][y2]
                if first_number != ' ' and second_number != ' ':
                    if (first_number + second_number == 10) or (first_number == second_number):
                        board[x1][y1] = ' '
                        board[x2][y2] = ' '
                    else:
                        raise
                else:
                    raise
            else:
                raise
        except:
            print('Невозможно выбрать данную пару чисел.')


board = [[], [], []]
s = '123456789111213141516171819'
for x in range(3):
    for y in range(9):
        board[x].append(int(s[0]))
        s = s[1:]
play_game()

'''
                        try:
                            for x in range(3):
                                for y in range(9):
                                    if board[x][y] != ' ' and board[x][y + 1] != ' ' and board[x][y - 1] != ' ' and \
                                            board[x + 1][y] != ' ' and board[x - 1][y] != ' ':
                                        if ((board[x][y] + board[x][y + 1] == 10) or (
                                                board[x][y] == board[x][y + 1])):
                                            raise
                                        elif ((board[x][y] + board[x][y - 1] == 10) or (
                                                board[x][y] == board[x][y - 1])):
                                            raise
                                        elif ((board[x][y] + board[x + 1][y] == 10) or (
                                                board[x][y] == board[x + 1][y])):
                                            raise
                                        elif ((board[x][y] + board[x - 1][y] == 10) or (
                                                board[x][y] == board[x - 1][y])):
                                            raise
                            print(board)
                            print(map(int, ''.join(board).split()))
                        except:
                            print('All right')
'''
