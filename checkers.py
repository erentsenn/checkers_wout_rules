from CheckersGame import CheckersGame
from Move import Move

if __name__ == '__main__':
    checkers = CheckersGame()
    checkers.start_game()

    while (checkers.game_active):
        origin = input('FROM:')
        destination = input('TO:')

        move = Move(origin, destination) # по факту проверили координаты
        checkers.move(move) # с обработанными координатами непосредственно делаем ход
