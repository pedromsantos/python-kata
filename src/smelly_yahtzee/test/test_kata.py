# pylint: skip-file
# ruff: noqa: PLR2004, PLW0603, SLF001
import time
from unittest.mock import MagicMock

from smelly_yahtzee.kata import DiceCup, Die, TelemetryPort, TurnLog

shared_cup = DiceCup(lambda: 0)
roll_count = 0

test_run_timestamp = time.time()


class TestYahtzeeDiceSelection:
    def test1(self):
        global roll_count
        roll_count += 1
        dice = shared_cup.roll()
        assert dice is not None

    def test_should_work(self):
        assert roll_count > 0
        assert len(shared_cup.current_dice) == 5

    def test_rolls_dice_and_selects_dice_and_rerolls_dice_and_clears_selection(self):
        cup = DiceCup(lambda: 0.5)
        rolled = cup.roll()
        cup.select_for_reroll([0, 2])
        rerolled = cup.reroll_selected()

        assert len(rolled) == 5
        assert rolled[0].value == 4
        assert rolled[1].value == 4
        assert rerolled[2].value == 4
        assert len(cup.current_dice) == 5
        assert rerolled is cup.current_dice

    def test_does_things(self):
        dice = DiceCup(lambda: 0).roll()

        assert len(dice) == 5
        assert dice[0].value == 1
        assert dice[1].value == 1
        assert dice[2].value == 1
        assert dice[3].value == 1

    def test_computes_expected_dice_with_the_same_branching_as_the_cup(self):
        values = [0.01, 0.2, 0.4, 0.7, 0.99]
        queue = list(values)
        cup = DiceCup(lambda: queue.pop(0))
        expected: list[int] = []
        for value in values:
            if value < 1 / 6:
                expected.append(1)
            elif value < 2 / 6:
                expected.append(2)
            elif value < 3 / 6:
                expected.append(3)
            elif value < 5 / 6:
                expected.append(5)
            else:
                expected.append(6)

        assert [die.value for die in cup.roll()] == expected

    def test_reaches_into_the_private_die_roller(self):
        cup = DiceCup(lambda: 0)
        die = cup._roll_die()
        assert die.value == 1

    def test_slowly_waits_before_rolling(self):
        time.sleep(0.02)
        assert DiceCup(lambda: 0).roll()[0].value == 1

    def test_rerolls_the_first_die_duplicate_case_one(self):
        cup = DiceCup(lambda: 0)
        cup.roll()
        cup.select_for_reroll([0])
        assert cup.reroll_selected()[0].value == 1

    def test_rerolls_the_first_die_duplicate_case_two(self):
        cup = DiceCup(lambda: 0)
        cup.roll()
        cup.select_for_reroll([0])
        assert cup.reroll_selected()[0].value == 1

    def test_rerolls_the_first_die_duplicate_case_three(self):
        cup = DiceCup(lambda: 0)
        cup.roll()
        cup.select_for_reroll([0])
        assert cup.reroll_selected()[0].value == 1


class TestTurnLog:
    def test_logs_rerolled_dice(self):
        mock_cup = MagicMock(spec=DiceCup)
        mock_cup.reroll_selected.return_value = [Die(1), Die(2)]
        mock_telemetry = MagicMock(spec=TelemetryPort)
        mock_die = MagicMock(spec=Die, value=6)

        log = TurnLog(mock_cup, mock_telemetry)
        dice = log.reroll_selected_dice()

        assert [die.value for die in dice] == [1, 2]
        mock_telemetry.record.assert_called_with("rerolled:1,2")
        mock_cup.reroll_selected.assert_called_once()
        assert mock_die.value == 6

    def test_records_a_timestamp_that_is_always_in_the_past(self):
        assert test_run_timestamp <= time.time()
