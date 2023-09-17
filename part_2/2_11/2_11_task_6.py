# Часть 2. Модуль 11. Практическая работа. Задача 6. Крестики-нолики
# Что нужно сделать
# Создайте программу, которая реализует игру «Крестики-нолики».
#
# Для этого напишите:
# 1. Класс, который будет описывать поле игры.
# class Board:
#     # Класс поля, который создаёт у себя экземпляры клетки.
#     # Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
#     # Помимо этого, класс должен содержать методы:
#     # «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята, меняет её состояние.
#         Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
#     # «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False.
#         True — если один из игроков победил, False — если победителя нет.
#
# 2. Класс, который будет описывать одну клетку поля:
# class Cell:
#     # Клетка, у которой есть значения:
#     # занята она или нет;
#     # номер клетки;
#     # символ, который клетка хранит (пустая, крестик, нолик).
#
# 3. Класс, который описывает поведение игрока:
# class Player:
#     # У игрока может быть:
#     # имя,
#     # количество побед.
#
#     # Класс должен содержать метод:
#     # «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки).
#         Введённый номер нужно обязательно проверить.
#
# 4. Класс, который управляет ходом игры:
# class Game:
#     # класс «Игры» содержит атрибуты:
#     # состояние игры,
#     # игроки,
#     # поле.
#
#     # А также методы:
#     # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки,
#         изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
#     # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается
#         победой одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.
#     # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры,
#         хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# Сообщения о процессе получения результата осмысленны и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.

class Cell:  # Клетка
    symbols = [' ', 'X', 'O']

    def __init__(self, number, symbol=symbols[0]):
        self.number = number  # номер клетки
        self.symbol = symbol  # символ, который клетка хранит (пустая, крестик, нолик)
        self.busy = False  # занята она или нет


class Board:  # Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.cells = [Cell(number) for number in range(1, 10)]  # хранит информацию о состоянии поля

    def print_board(self):
        print('+---+---+---+')
        print('| {} | {} | {} |'.format(self.cells[0].symbol, self.cells[1].symbol, self.cells[2].symbol))
        print('+---+---+---+')
        print('| {} | {} | {} |'.format(self.cells[3].symbol, self.cells[4].symbol, self.cells[5].symbol))
        print('+---+---+---+')
        print('| {} | {} | {} |'.format(self.cells[6].symbol, self.cells[7].symbol, self.cells[8].symbol))
        print('+---+---+---+')

    def change_state_cell(self, number, symbol):  # «Изменить состояние клетки» (получает номер клетки)
        try:
            if self.cells[number].symbol != ' ':  # если клетка не занята
                return False
            else:
                self.cells[number].symbol = symbol  # меняет её состояние
                return True
        except ValueError as err3:
            print(f"Ошибка ввода ({err3}, {type(err3)}): введите число от 1 до 9).")
        except IndexError as err4:
            print(f"Ошибка ввода ({err4}, {type(err4)}): введите число от 1 до 9).")
        except TypeError as err5:
            print(f"Ошибка ввода ({err5}, {type(err5)}): введите число от 1 до 9).")

    def check_win(self):  # «Проверить окончание игры» (не получает входящих данных)
        win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                     (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for elem in win_combo:
            if self.cells[elem[0]].symbol == self.cells[elem[1]].symbol == self.cells[elem[2]].symbol != ' ':
                return True  # True — если один из игроков победил
        return False


class Player:  # Описывает поведение игрока
    number = 0

    def __init__(self, name, symbol, wins_count=0):
        self.name = name  # имя игрока
        self.symbol = symbol
        self.wins_count = wins_count  # количество побед

    def player_step(self):  # «Сделать ход» (ничего не принимает)
        try:

            number = int(input(f'{self.name}, введите номер клетки от 1 до 9: ')) - 1

            if not Cell(number).busy:  # проверка номера
                return number  # возвращает ход игрока (номер клетки)

            else:
                print('Клетка занята, переходите.')
                self.player_step()

        except ValueError as err1:
            print(f"Что-то не то ввели: {err1}, {type(err1)}")


class Game:

    def __init__(self, board, state_game=False):
        self.board = board  # поле
        self.players = (Player('Player One', 'x'), Player('Player Two', 'o'))  # игроки
        self.state_game = state_game  # состояние игры

    def start_step(self, player: Player):  # Метод запуска одного хода игры (получает одного из игроков)

        while True:
            num_cell = player.player_step()  # запрашивает у игрока номер клетки
            value = player.symbol
            state = self.board.change_state_cell(num_cell, value)  # изменяет поле
            if state:
                break
            else:
                print("Клетка занята или ошибка ввода. Повторите ввод.")

        self.board.print_board()
        if self.board.check_win():  # проверяет, выиграл ли игрок
            player.wins_count += 1
            print(f"{player.name} win!")
            return True  # Если игрок победил, возвращает True
        return False  # иначе False

    def start_game(self):  # Метод запуска одной игры
        # self.board.board_list.clear()    # Очищает поле
        while True:  # запускает цикл с игрой, который завершается победой одного из игроков или ничьей
            if self.board.check_win():

                break  # return True    # Если игра завершена, метод возвращает True
            else:
                for player in self.players:
                    if self.start_step(player):
                        break
                # return False    # иначе False


if __name__ == '__main__':
    win = [0, 0]
    def start_all_games():  # Основной метод запуска игр.
        game_continue = '1'
        while True:  # В цикле запускает игры
            if game_continue == '0':
                break
            board = Board()
            game = Game(board)
            game.start_game()

            for i, i_payer in enumerate(game.players):
                win[i] += i_payer.wins_count
            print(f"Счет: {win[0]} | {win[1]}")

            game_continue = input('Хотите продолжить? 1 - до, 0 - нет: ')
            # запрашивая после каждой игры, хотят ли игроки продолжать играть
            # После каждой игры выводится текущий счёт игроков.

    start_all_games()
