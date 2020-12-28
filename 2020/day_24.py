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


https://adventofcode.com/2020/day/24
"""

# How to navigate in an hexagon grid
# https://www.redblobgames.com/grids/hexagons/

class Floor:
    def __init__(self, data):
        self.tiles = data
        self.pattern = dict()
        # self._directions = {  # (z, y, x)
        #     'e':  ( 1,  0),   # east
        #     'se': ( 0,  1),   # southeast
        #     'sw': (-1,  1),   # southwest
        #     'w':  (-1,  0),   # west
        #     'nw': ( 0, -1),   # northwest
        #     'ne': ( 1, -1),   # northeast
        # }
        self._directions = {  # (z, y, x)
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

    def flit_tiles(self):
        for tile in self.tiles:
            position = self._get_position(tile)
            self.pattern[position] = self.pattern.setdefault(position, 0) + 1

    def count_black(self):
        return sum([i%2 for i in self.pattern.values()])

def main():
    with open('inputs/day_24.txt') as input_file:
        data = input_file.read().splitlines()
    floor = Floor(data)
    floor.flit_tiles()
    print(floor.count_black())
    # floor.play(100)
    # print(floor.labels())


if __name__ == '__main__':
    main()