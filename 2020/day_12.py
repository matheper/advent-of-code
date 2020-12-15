"""
--- Day 12: Rain Risk ---


Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?


https://adventofcode.com/2020/day/12
"""

from collections import namedtuple


class Ship:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation
        self._orientation_move = [
            (0, 1),   # N
            (1, 0),   # E
            (0, -1),  # S
            (-1, 0)   # W
        ]

    def move(self, instruction):
        action, value = instruction
        if action == 'N':    # move north
            self.y += value
        elif action == 'S':  # move south
            self.y -= value
        elif action == 'E':  # move east
            self.x += value
        elif action == 'W':  # move west
            self.x -= value
        elif action == 'R':  # turn right
            self.orientation = (self.orientation + value // 90) % 4
        elif action == 'L':  # turn left
            self.orientation = (self.orientation - value // 90) % 4
        elif action == 'F':  # move forward
            self.x += self._orientation_move[self.orientation][0] * value
            self.y += self._orientation_move[self.orientation][1] * value

    def navigate(self, instructions):
        for instruction in instructions:
            self.move(instruction)

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


def main():
    with open('inputs/day_12.txt') as input_file:
        instructions = [(i[0], int(i[1:])) for i in input_file.read().splitlines()]
    ship = Ship(x=0, y=0, orientation=1)
    ship.navigate(instructions)
    print(ship.manhattan_distance())


if __name__ == '__main__':
    main()