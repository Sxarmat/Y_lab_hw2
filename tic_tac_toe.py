from random import choice



class TicTacToe():
    pass

def game():
    global playing_field
    playing_field = [[0 for i in range(10)] for n in range(10)]
    global cells
    cells = {}
    new_game()
    result = ''
    while cells:
        show_playing_field()
        key_cell = int(input('Ваш ход\n'))
        if move(key_cell, 'X'):
            if check_louse(key_cell, 'X'):
                result = 'Вы проиграли'
                break
            print('Ход компьютера')
            key_cell = choice(list(cells.keys()))
            if not move(key_cell, 'O'):
                result = 'Ошибка'
            if check_louse(key_cell, 'O'):
                result = 'Вы победили'
                break
        else:
            print('Не корректное значение поля')
            continue
    result = 'Ничья' if not result else result
    show_playing_field()
    return result


def new_game():
    i = 0
    for row in range(10):
        for cell in range(10):
            key_cell = cell + 1 + i
            playing_field[row][cell] = key_cell
            cells[key_cell] = (row, cell)
        i += 10


def show_playing_field():
    for i in playing_field:
        for j in i:
            _end = '  ' if len(str(j)) == 1 else ' '
            print(j, end=_end)
        print()


def move(key_cell, simbol):
    if key_cell in cells:
        playing_field[cells[key_cell][0]][cells[key_cell][1]] = simbol
        return True
    return False


def check_louse(key_cell, simbol):
    row = cells[key_cell][0]
    cell = cells[key_cell][1]
    k = 4
    border_field = range(10)
    diagonal_1 = ''
    diagonal_2 = ''
    vertical = ''
    horizontal = ''
    for i in range(row - 4, row + 5):
        row_1 = i
        col_1, col_2 = cell - k, cell + k
        if row_1 in border_field:
            vertical += str(playing_field[i][cell])
            if col_1 in border_field:
                diagonal_1 += str(playing_field[row_1][col_1])
            if col_2 in border_field:
                diagonal_2 += str(playing_field[row_1][col_2])
        k -= 1
    for j in range(cell - 4, cell + 5):
        if j in range(10):
            horizontal += str(playing_field[row][j])
    del cells[key_cell]
    combination = simbol * 5
    if combination in diagonal_1 or combination in diagonal_2 or combination in vertical or combination in horizontal:
        return True
    return False


if __name__ == '__main__':
    print(game())
