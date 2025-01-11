from mars_rover.kata import Rover


def test_turn_360_degrees_clockwise():
    commands = "5 5\n1 2 N\nLMLMLMLMM"
    rover = Rover()

    position = rover.execute(commands)

    assert position == commands


def test_turn_360_degrees_counter_clockwise():
    commands = "5 5\n3 3 E\nMMRMMRMRRM"
    rover = Rover()

    position = rover.execute(commands)

    assert position == commands
