import os
from Piece import Piece

class Board:
    def __init__(self):
        self.board = self.generate_board()

    def move(self, move):
        if self.is_legal_move(move):
            origin_x = move.origin_x
            origin_y = move.origin_y
            destination_x = move.destination_x
            destination_y = move.destination_y

            piece_to_move = self.board[origin_x][origin_y]
            self.board[destination_x][destination_y] = piece_to_move
            self.board[origin_x][origin_y] = None # совершаем ход - поле куда пошла шашка становится шашкой, а откуда ушла пустым полем
        else:
            raise Exception('IllegalMove')

    def is_legal_move(self, move):
        return True

    def generate_board(self):
        board = []

        # Инициализируем пустое поле
        for row in range(0, 8):
            board.append([])
            for col in range(0, 8):
                board[row].append(None)

        # Расставляем черные и белые шашки
        for x in range(0, 8):
            for y in range(0, 8):
                x_is_even = x % 2 == 0
                y_is_even = y % 2 == 0

                # black pieces
                if x in range(0, 3):
                    if x_is_even and not y_is_even:
                        board[x][y] = Piece('BLACK')
                    if not x_is_even and y_is_even:
                        board[x][y] = Piece('BLACK')

                # red pieces
                if x in range(5, 8):
                    if not x_is_even and y_is_even:
                        board[x][y] = Piece('RED')
                    if x_is_even and not y_is_even:
                        board[x][y] = Piece('RED')
        return board

    def __repr__(self): # метод для представления объекта класса как строки(то что будет делать принт)
        print('\n', ' ' * 6, 'Checkers', end='\n\n')
        for row in range(7, -1, -1):
            # for row in range(0, 8):
            print(row + 1, end=' ')
            # print(8 - row, ' | ', end='')
            for col in range(0, 8):
                to_print = ' . '
                piece = self.board[row][col]
                if piece: to_print = f' {piece.print_color()} '
                print(to_print, end='')
            print()
        print('   A  B  C  D  E  F  G  H')
        return ''
