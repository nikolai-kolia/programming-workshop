from random import randint


def display_board(board):
    first_colomn = 1
    s = f'{first_colomn} '
    for x in range(3):
        for y in range(3):
            s += f'| {board[x][y]} | '
            if (y % 3 == 2):
                first_colomn += 1
                print(s)
                s = f'{first_colomn} '
    print('    1     2     3')


def is_game_over():
    for row in board:
        if sum(row) > 0:
            return False
    return True


def play_game():
    player1_sum, player2_sum = 0, 0
    any_move, is_possible_moves_1, is_possible_moves_2, game_over = True, True, True, False
    while not game_over:
        display_board(board)
        if is_possible_moves_1 == False and is_possible_moves_2 == False:
            display_board(board)
            print(
                f"Игра окончена! Сумма очков первого игрока: {player1_sum}. Сумма очков второго игрока: {player2_sum}.")
            if player1_sum > player2_sum:
                print("Победил первый игрок!")
            elif player2_sum > player1_sum:
                print("Победил второй игрок!")
            else:
                print("Ничья!")
            game_over = True
            break
        print(f"Ход первого игрока возможен в {'любой' if any_move else last_x + 1} строке")
        while True:
            try:
                if any_move:
                    x = int(input("Введите номер строки: ")) - 1
                    y = int(input("Введите номер столбца: ")) - 1
                    if board[x][y] != 0:
                        any_move = False
                        player1_sum += board[x][y]
                        board[x][y] = 0
                        last_y = y
                        break
                else:
                    if sum(board[last_x]) == 0:
                        print('У первого игрока нет ходов')
                        is_possible_moves_1 = False
                        break
                    else:
                        is_possible_moves_1 = True
                        x = int(input("Введите номер строки: ")) - 1
                        y = int(input("Введите номер столбца: ")) - 1
                        if last_x == x:
                            if board[x][y] != 0:
                                any_move = False
                                player1_sum += board[x][y]
                                board[x][y] = 0
                                last_y = y
                                break
                        else:
                            raise
            except:
                print('Невожможно выбрать данное число')

        if is_game_over():
            display_board(board)
            print(
                f"Игра окончена! Сумма очков первого игрока: {player1_sum}. Сумма очков второго игрока: {player2_sum}.")
            if player1_sum > player2_sum:
                print("Победил первый игрок!")
            elif player2_sum > player1_sum:
                print("Победил второй игрок!")
            else:
                print("Ничья!")
            game_over = True
            break

        print(f"Ход второго игрока возможен в {last_y + 1} столбце")
        while True:
            try:
                if board[0][last_y] + board[1][last_y] + board[2][last_y] == 0:
                    print('У второго игрока нет ходов')
                    is_possible_moves_2 = False
                    break
                else:
                    is_possible_moves_2 = True
                    x = int(input("Введите номер строки: ")) - 1
                    y = int(input("Введите номер столбца: ")) - 1
                    if last_y == y:
                        if board[x][y] != 0:
                            player2_sum += board[x][y]
                            board[x][y] = 0
                            last_x = x
                            break
                    else:
                        raise
            except:
                print('Невожможно выбрать данное число')

        if is_game_over():
            display_board(board)
            print(
                f"Игра окончена! Сумма очков первого игрока: {player1_sum}. Сумма очков второго игрока: {player2_sum}.")
            if player1_sum > player2_sum:
                print("Победил первый игрок!")
            elif player2_sum > player1_sum:
                print("Победил второй игрок!")
            else:
                print("Ничья!")
            game_over = True


board = [[randint(1, 9) for _ in range(3)] for _ in range(3)]
play_game()
