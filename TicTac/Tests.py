import tic_tac
import pytest


class TestTicTac:

    def test_steps(self):
        game = tic_tac.Field()
        game.step(1)
        assert game.cells[0] == 'X'
        game.step(2)
        assert game.cells[1] == 'O'

    def test_input(self):
        game = tic_tac.Field()
        game.step(1)
        assert game.cells[0] == 'X'
        with pytest.raises(tic_tac.NotDigitInputException):
            game.check_input('h')
        with pytest.raises(tic_tac.WrongInputException):
            game.check_input('0')
        with pytest.raises(tic_tac.BusyCellException):
            game.check_input('1')

    def test_win(self):
        game = tic_tac.Field()
        game.step(1)
        assert game.cells[0] == 'X'
        game.step(4)
        assert game.cells[3] == 'O'
        game.step(2)
        assert game.cells[1] == 'X'
        game.step(5)
        assert game.cells[4] == 'O'
        with pytest.raises(tic_tac.WinException):
            game.step(3)
        assert game.cells[2] == 'X'

    def test_draw(self):
        game = tic_tac.Field()
        game.step(1)
        assert game.cells[0] == 'X'
        game.step(2)
        assert game.cells[1] == 'O'
        game.step(3)
        assert game.cells[2] == 'X'
        game.step(4)
        assert game.cells[3] == 'O'
        game.step(6)
        assert game.cells[5] == 'X'
        game.step(9)
        assert game.cells[8] == 'O'
        game.step(5)
        assert game.cells[4] == 'X'
        game.step(7)
        assert game.cells[6] == 'O'
        game.step(8)
        assert game.cells[7] == 'X'
        assert game.check_draw()
