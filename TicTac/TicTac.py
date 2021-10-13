class Field:

    def __init__(self, size=3):
        self.size = size
        self.count = size ** 2
        self.steps = 0
        self.end = False
        self.cells = [' ' for _ in range(self.count)]

    def is_cell_empty(self, x):
        return self.cells[x - 1] == ' '

    def check_tie(self):
        check = 0
        for i in self.cells:
            if i != ' ':
                check += 1
        if check == self.count:
            print('GG')
            self.end = True

    def check_win(self):
        win_comb = ((0, 1), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_comb:
            if self.cells[each[0]] == self.cells[each[1]] == self.cells[each[2]] != ' ':
                print(self.cells[each[0]] + ' win!')
                self.end = True
                return
        a.check_tie()

    def stepX(self, x):
        if self.is_cell_empty(x):
            self.cells[x - 1] = 'X'
            a.steps += 1

    def stepO(self, x):
        if self.is_cell_empty(x):
            self.cells[x - 1] = 'O'
            a.steps += 1

    def print(self):
        print(self.cells[0] + '|' + self.cells[1] + '|' + self.cells[2])
        print('-' * 5)
        print(self.cells[3] + '|' + self.cells[4] + '|' + self.cells[5])
        print('-' * 5)
        print(self.cells[6] + '|' + self.cells[7] + '|' + self.cells[8])


a = Field()
a.print()
while not a.end:
    if a.steps % 2 == 0:
        x = int(input('Player 1, Make ur choice: '))
        a.stepX(x)
    else:
        x = int(input('Player 2, Make ur choice: '))
        a.stepO(x)
    a.print()
    a.check_win()
