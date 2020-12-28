"""
--- Day 24: Lobby Layout ---


Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.

As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.

The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.

The tiles are all white on one side and black on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a reference tile in the very center of the room. (Every line starts from the same reference tile.)

Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these directions with no delimiters; for example, esenee identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.

Here is a larger example:

sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of 10 tiles are black.

Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, how many tiles are left with the black side up?


--- Part Two ---
The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208
After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?


https://adventofcode.com/2020/day/24
"""

# How hexagon grids work
# https://www.redblobgames.com/grids/hexagons/


from copy import deepcopy


class Floor:
    def __init__(self, data):
        self.tiles = data
        self.pattern = dict()     # {(z, y, x): n}
        self._directions = {      # (z, y, x)
            'e':  ( 0, -1,  1),   # east
            'se': ( 1, -1,  0),   # southeast
            'sw': ( 1,  0, -1),   # southwest
            'w':  ( 0,  1, -1),   # west
            'nw': (-1,  1,  0),   # northwest
            'ne': (-1,  0,  1),   # northeast
        }

    def _get_position(self, tile):
        z = y = x = idx = 0
        while idx < len(tile):
            move = self._directions.get(tile[idx])
            if move is None:
                move = self._directions.get(tile[idx:idx+2])
                idx += 1
            idx += 1
            z, y, x = z + move[0], y + move[1], x + move[2]
        return (z, y, x)

    def arrange_tiles(self):
        for tile in self.tiles:
            position = self._get_position(tile)
            if position not in self.pattern:
                self.pattern[position] = 1
            else:
                del self.pattern[position]

    def _get_neighbors(self, tile):
        z, y, x = tile
        neighbors = {
            (z, y - 1, x + 1),  # east
            (z + 1, y - 1, x),  # southeast
            (z + 1, y, x - 1),  # southwest
            (z, y + 1, x - 1),  # west
            (z - 1, y + 1, x),  # northwest
            (z - 1, y, x + 1),  # northeast
        }
        return neighbors

    def flip_tiles(self, days):
        for _ in range(days):
            new_pattern = deepcopy(self.pattern)
            black_tiles = set(self.pattern.keys())
            for tile in self.pattern:
                neighbors = self._get_neighbors(tile)
                black_neighbors = neighbors.intersection(black_tiles)
                white_neighbors = neighbors.difference(black_tiles)
                if len(black_neighbors) not in (1, 2):
                    del new_pattern[tile]
                for w in white_neighbors:
                    w_neighbors = self._get_neighbors(w)
                    w_black_neighbors = w_neighbors.intersection(black_tiles)
                    if len(w_black_neighbors) == 2:
                        new_pattern[w] = 1
            self.pattern = deepcopy(new_pattern)

    def count_black_tiles(self):
        return sum(self.pattern.values())

def main():
    with open('inputs/day_24.txt') as input_file:
        data = input_file.read().splitlines()

    floor = Floor(data)
    floor.arrange_tiles()
    print(floor.count_black_tiles())

    floor.flip_tiles(100)
    print(floor.count_black_tiles())


if __name__ == '__main__':
    main()