import pytest

from smelly_tic_tac_toe.kata import Game

class TestGame:
    def setup_method(self):
        self.game = Game()

    def test_not_allow_player_o_to_play_first(self):
        with pytest.raises(Exception) as excinfo:
            self.game.play('O', 0, 0)
        assert str(excinfo.value) == "Invalid first player"

    def test_not_allow_player_x_to_play_twice_in_a_row(self):
        self.game.play('X', 0, 0)
        with pytest.raises(Exception) as excinfo:
            self.game.play('X', 1, 0)
        assert str(excinfo.value) == "Invalid next player"

    def test_not_allow_player_to_play_in_last_played_position(self):
        self.game.play('X', 0, 0)
        with pytest.raises(Exception) as excinfo:
            self.game.play('O', 0, 0)
        assert str(excinfo.value) == "Invalid position"

    def test_not_allow_player_to_play_in_any_played_position(self):
        self.game.play('X', 0, 0)
        self.game.play('O', 1, 0)
        with pytest.raises(Exception) as excinfo:
            self.game.play('X', 0, 0)
        assert str(excinfo.value) == "Invalid position"

    def test_declare_player_x_as_a_winner_if_three_in_top_row(self):
        self.game.play('X', 0, 0)
        self.game.play('O', 1, 0)
        self.game.play('X', 0, 1)
        self.game.play('O', 1, 1)
        self.game.play('X', 0, 2)
        winner = self.game.determine_winner()
        assert winner == 'X'

    def test_declare_player_o_as_a_winner_if_three_in_top_row(self):
        self.game.play('X', 2, 2)
        self.game.play('O', 0, 0)
        self.game.play('X', 1, 0)
        self.game.play('O', 0, 1)
        self.game.play('X', 1, 1)
        self.game.play('O', 0, 2)
        winner = self.game.determine_winner()
        assert winner == 'O'

    def test_declare_player_x_as_a_winner_if_three_in_middle_row(self):
        self.game.play('X', 1, 0)
        self.game.play('O', 0, 0)
        self.game.play('X', 1, 1)
        self.game.play('O', 0, 1)
        self.game.play('X', 1, 2)
        winner = self.game.determine_winner()
        assert winner == 'X'

    def test_declare_player_o_as_a_winner_if_three_in_middle_row(self):
        self.game.play('X', 0, 0)
        self.game.play('O', 1, 0)
        self.game.play('X', 2, 0)
        self.game.play('O', 1, 1)
        self.game.play('X', 2, 1)
        self.game.play('O', 1, 2)
        winner = self.game.determine_winner()
        assert winner == 'O'

    def test_declare_player_x_as_a_winner_if_three_in_bottom_row(self):
        self.game.play('X', 2, 0)
        self.game.play('O', 0, 0)
        self.game.play('X', 2, 1)
        self.game.play('O', 0, 1)
        self.game.play('X', 2, 2)
        winner = self.game.determine_winner()
        assert winner == 'X'

    def test_declare_player_o_as_a_winner_if_three_in_bottom_row(self):
        self.game.play('X', 0, 0)
        self.game.play('O', 2, 0)
        self.game.play('X', 1, 0)
        self.game.play('O', 2, 1)
        self.game.play('X', 1, 1)
        self.game.play('O', 2, 2)
        winner = self.game.determine_winner()
        assert winner == 'O'