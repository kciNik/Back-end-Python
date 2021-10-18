class WrongInputException(Exception):
    """
    Exception for wrong digit input
    """


class NotDigitInputException(Exception):
    """
    Exception for non digit input
    """


class BusyCellException(Exception):
    """
    Exception for busy cell
    """


class WinException(Exception):
    """
    Exception for win
    """


class Field:

    def __init__(self):
        self.player = False
        self.cells = [' ' for _ in range(9)]

    def check_draw(self):
        if self.cells.count(' ') == 0:
            return True
        return False

    def check_win(self):
        win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_comb:
            if self.cells[each[0]] == self.cells[each[1]] == self.cells[each[2]] != ' ':
                raise WinException

    def step(self, x):
        self.cells[x - 1] = 'O' if self.player else 'X'
        self.check_win()
        self.player = not self.player

    def user_input(self):
        return input('Player ' + ('2' if self.player else '1') + ', make ur choice -> ')

    def check_input(self, data):
        if not data.isdigit():
            raise NotDigitInputException
        index = int(data)
        if index < 1 or index > 9:
            raise WrongInputException
        if not self.cells[index - 1] == ' ':
            raise BusyCellException

    def print(self):
        print(self.cells[0] + '|' + self.cells[1] + '|' + self.cells[2])
        print('-' * 5)
        print(self.cells[3] + '|' + self.cells[4] + '|' + self.cells[5])
        print('-' * 5)
        print(self.cells[6] + '|' + self.cells[7] + '|' + self.cells[8])

    def game(self):
        while not self.check_draw():
            self.print()
            x = self.user_input()
            try:
                self.check_input(x)
            except NotDigitInputException:
                print('Ur input is not a digit, please enter 1 to 9')
                continue
            except WrongInputException:
                print('Ur input is wrong, please enter 1 to 9')
                continue
            except BusyCellException:
                print('This cell is busy, please try another :)')
                continue
            try:
                self.step(int(x))
            except WinException:
                print('Player ' + ('2' if self.player else '1') + ' wins!')
                self.print()
                return
        print('Draw!')
        self.print()


if __name__ == '__main__':
    a = Field()
    a.game()
