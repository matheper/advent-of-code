"""
--- Day 23: Crab Cups ---
The small crab challenges you to a game! The crab is going to mix up some cups, and you have to predict where they'll end up.

The cups will be arranged in a circle and labeled clockwise (your puzzle input). For example, if your labeling were 32415, there would be five cups in the circle; going clockwise around the circle from the first cup, the cups would be labeled 3, 2, 4, 1, 5, and then back to 3 again.

Before the crab starts, it will designate the first cup in your list as the current cup. The crab is then going to do 100 moves.

Each move, the crab does the following actions:

The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
For example, suppose your cup labeling were 389125467. If the crab were to do merely 10 moves, the following changes would occur:

-- move 1 --
cups: (3) 8  9  1  2  5  4  6  7 
pick up: 8, 9, 1
destination: 2

-- move 2 --
cups:  3 (2) 8  9  1  5  4  6  7 
pick up: 8, 9, 1
destination: 7

-- move 3 --
cups:  3  2 (5) 4  6  7  8  9  1 
pick up: 4, 6, 7
destination: 3

-- move 4 --
cups:  7  2  5 (8) 9  1  3  4  6 
pick up: 9, 1, 3
destination: 7

-- move 5 --
cups:  3  2  5  8 (4) 6  7  9  1 
pick up: 6, 7, 9
destination: 3

-- move 6 --
cups:  9  2  5  8  4 (1) 3  6  7 
pick up: 3, 6, 7
destination: 9

-- move 7 --
cups:  7  2  5  8  4  1 (9) 3  6 
pick up: 3, 6, 7
destination: 8

-- move 8 --
cups:  8  3  6  7  4  1  9 (2) 5 
pick up: 5, 8, 3
destination: 1

-- move 9 --
cups:  7  4  1  5  8  3  9  2 (6)
pick up: 7, 4, 1
destination: 5

-- move 10 --
cups: (5) 7  4  1  8  3  9  2  6 
pick up: 7, 4, 1
destination: 3

-- final --
cups:  5 (8) 3  7  4  1  9  2  6 
In the above example, the cups' values are the labels as they appear moving clockwise around the circle; the current cup is marked with ( ).

After the crab is done, what order will the cups be in? Starting after the cup labeled 1, collect the other cups' labels clockwise into a single string with no extra characters; each number except 1 should appear exactly once. In the above example, after 10 moves, the cups clockwise from 1 are labeled 9, 2, 6, 5, and so on, producing 92658374. If the crab were to complete all 100 moves, the order after cup 1 would be 67384529.

Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?


https://adventofcode.com/2020/day/23
"""

from copy import deepcopy


class Game:
    def __init__(self, data):
        self.cups = self._parse(data)

    def _parse(self, data):
        cups = [int(cup) for cup in data.replace('\n', '')]
        return cups

    def play(self, moves, pickup_size=3):
        max_cup = max(self.cups)
        current = 0
        current_cup = self.cups[current]
        for _ in range(moves):
            current_cup = self.cups[current]
            pickup = list()
            for _ in range(pickup_size):
                pop_idx = (current + 1)
                if pop_idx >= len(self.cups):
                    pop_idx = 0
                pickup.append(self.cups.pop(pop_idx))
            destination = current_cup - 1
            while destination not in self.cups:
                destination -= 1
                if destination <= 0:
                    destination = max_cup
            insert_idx = (self.cups.index(destination) + 1)
            [self.cups.insert(insert_idx, p) for p in reversed(pickup)]
            current = (self.cups.index(current_cup) + 1) % len(self.cups)

    def labels(self):
        idx_one = self.cups.index(1)
        cup_labels = (self.cups[idx_one + 1:] + self.cups[:idx_one])
        return ''.join([str(i) for i in cup_labels])


def main():
    with open('inputs/day_23.txt') as input_file:
        data = input_file.read()
    game = Game(data)
    game.play(100)
    print(game.labels())



if __name__ == '__main__':
    main()