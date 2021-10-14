class Field:

    def __init__(self, size=3):
        self.count = size ** 2
        self.player = False
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
        win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_comb:
            if self.cells[each[0]] == self.cells[each[1]] == self.cells[each[2]] != ' ':
                print(self.cells[each[0]] + ' win!')
                self.end = True
                return
        a.check_tie()

    def step(self, x):
        if self.is_cell_empty(x):
            self.cells[x - 1] = 'O' if self.player else 'X'
            a.player = not a.player
        else:
            print('This cell is busy, try another :)')

    def print(self):
        print(self.cells[0] + '|' + self.cells[1] + '|' + self.cells[2])
        print('-' * 5)
        print(self.cells[3] + '|' + self.cells[4] + '|' + self.cells[5])
        print('-' * 5)
        print(self.cells[6] + '|' + self.cells[7] + '|' + self.cells[8])

    def game(self):
        a.print()
        while not a.end:
            x = int(input('Player ' + ('2' if self.player else '1') + ', make ur choice '))
            self.step(x)
            a.print()
            a.check_win()


a = Field()
a.game()

# szfgdsdh