# ruff: noqa
import pytest

from refactoring_golf.hole10.kata import Game


class TestTicTacToeGame:
    def setup_method(self):
        self.game = Game()

    def test_should_not_allow_player_o_to_play_first(self):
        with pytest.raises(Exception):
            self.game.play("O", 0, 0)

    def test_should_not_allow_player_x_to_play_twice_in_a_row(self):
        self.game.play("X", 0, 0)
        with pytest.raises(Exception):
            self.game.play("X", 1, 0)

    def test_should_not_allow_a_player_to_play_in_last_played_position(self):
        self.game.play("X", 0, 0)
        with pytest.raises(Exception):
            self.game.play("O", 0, 0)

    def test_should_not_allow_a_player_to_play_in_any_played_position(self):
        self.game.play("X", 0, 0)
        self.game.play("O", 1, 0)
        with pytest.raises(Exception):
            self.game.play("X", 0, 0)

    def test_should_declare_player_x_as_winner_if_it_plays_three_in_top_row(self):
        self.game.play("X", 0, 0)
        self.game.play("O", 1, 0)
        self.game.play("X", 0, 1)
        self.game.play("O", 1, 1)
        self.game.play("X", 0, 2)

        winner = self.game.winner()

        assert winner == "X"

    def test_should_declare_player_o_as_winner_if_it_plays_three_in_top_row(self):
        self.game.play("X", 1, 0)
        self.game.play("O", 0, 0)
        self.game.play("X", 1, 1)
        self.game.play("O", 0, 1)
        self.game.play("X", 2, 2)
        self.game.play("O", 0, 2)

        winner = self.game.winner()

        assert winner == "O"

    def test_should_declare_player_x_as_winner_if_it_plays_three_in_middle_row(self):
        self.game.play("X", 1, 0)
        self.game.play("O", 0, 0)
        self.game.play("X", 1, 1)
        self.game.play("O", 0, 1)
        self.game.play("X", 1, 2)

        winner = self.game.winner()

        assert winner == "X"

    def test_should_declare_player_o_as_winner_if_it_plays_three_in_middle_row(self):
        self.game.play("X", 0, 0)
        self.game.play("O", 1, 0)
        self.game.play("X", 2, 1)
        self.game.play("O", 1, 1)
        self.game.play("X", 2, 2)
        self.game.play("O", 1, 2)

        winner = self.game.winner()

        assert winner == "O"

    def test_should_declare_player_x_as_winner_if_it_plays_three_in_bottom_row(self):
        self.game.play("X", 2, 0)
        self.game.play("O", 0, 0)
        self.game.play("X", 2, 1)
        self.game.play("O", 0, 1)
        self.game.play("X", 2, 2)

        winner = self.game.winner()

        assert winner == "X"

    def test_should_declare_player_o_as_winner_if_it_plays_three_in_bottom_row(self):
        self.game.play("X", 0, 0)
        self.game.play("O", 2, 0)
        self.game.play("X", 1, 1)
        self.game.play("O", 2, 1)
        self.game.play("X", 0, 1)
        self.game.play("O", 2, 2)

        winner = self.game.winner()

        assert winner == "O"
