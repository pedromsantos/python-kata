# pylint: skip-file
# ruff: noqa
import time
from unittest.mock import MagicMock

from smelly_mars_rover.kata import CommandTranslator, Coordinate, MissionLog, TelemetryPort

shared_translator = CommandTranslator()
call_count = 0

test_run_timestamp = time.time()


class _RecordingTelemetry:
    def __init__(self) -> None:
        self.recorded: list[str] = []

    def record(self, entry: str) -> None:
        self.recorded.append(entry)


class TestCommandTranslator:
    def test1(self):
        global call_count
        call_count += 1
        result = shared_translator.translate("I", "ES")
        assert result is not None

    def test_should_work(self):
        assert call_count > 0
        assert shared_translator.get_last_language_used() == "ES"

    def test_translates_and_logs_and_reports_last_language_and_handles_unknown_language_and_sequences(self):
        t = CommandTranslator()
        assert t.translate("G", "FR") == "L"
        assert t.translate("D", "FR") == "R"
        assert t.translate("A", "FR") == "M"
        assert t.translate("Z", "FR") == "Z"
        assert t.translate_sequence("GDA", "FR") == "LRM"
        assert t.get_last_language_used() == "FR"
        assert t.translate("X", "XX") == "X"

    def test_computes_the_expected_translation_using_the_same_logic_as_production(self):
        t = CommandTranslator()
        commands = "IDA"
        expected = ""
        for c in commands:
            if c == "I":
                expected += "L"
            elif c == "D":
                expected += "R"
            elif c == "A":
                expected += "M"
            else:
                expected += c
        assert t.translate_sequence(commands, "ES") == expected

    def test_reaches_into_a_private_translation_helper_directly(self):
        t = CommandTranslator()
        private_result = t._translate_spanish("I")
        assert private_result == "L"

    def test_slowly_waits_for_the_translator_to_be_ready(self):
        time.sleep(0.05)
        t = CommandTranslator()
        assert t.translate("A", "IT") == "M"

    def test_translates_italian_rotate_left_duplicate_case_one(self):
        t = CommandTranslator()
        assert t.translate("S", "IT") == "L"

    def test_translates_italian_rotate_left_duplicate_case_two(self):
        t = CommandTranslator()
        assert t.translate("S", "IT") == "L"

    def test_translates_italian_rotate_left_duplicate_case_three(self):
        t = CommandTranslator()
        assert t.translate("S", "IT") == "L"


class TestMissionLog:
    def test_logs_a_translated_sequence(self):
        mock_translator = MagicMock(spec=CommandTranslator)
        mock_translator.translate_sequence.return_value = "LRM"
        mock_telemetry = MagicMock(spec=TelemetryPort)
        mock_coordinate = MagicMock(spec=Coordinate, x=0, y=0)

        log = MissionLog(mock_translator, mock_telemetry)
        result = log.log_translated_sequence("GDA", "FR")

        assert result == "LRM"
        mock_translator.translate_sequence.assert_called_with("GDA", "FR")
        assert mock_coordinate.x == 0

    def test_records_telemetry_with_the_run_timestamp(self):
        telemetry = _RecordingTelemetry()
        log = MissionLog(CommandTranslator(), telemetry)

        log.log_translated_sequence("A", "IT")

        assert "IT" in telemetry.recorded[0]
        assert test_run_timestamp <= time.time()
