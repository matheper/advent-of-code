"""
--- Day 20: Jurassic Jigsaw ---


The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171
To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

--- Part Two ---
Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

In the example above, the tiles become:

.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###
Remove the gaps to form the actual image:

.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, after flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with O):

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea monster. In the above example, the habitat's water roughness is 273.

How many # are not part of a sea monster?


https://adventofcode.com/2020/day/20
"""

from copy import deepcopy

class Camera:
    def __init__(self, data):
        self.tiles = self._parse(data)
        self.full_image = self.reassemble()
    
    def _parse(self, data):
        tiles = {}
        for raw in data.split('\n\n'):
            raw_tile = raw.split('\n')
            id_ = int(''.join(raw_tile[0][5:-1]))
            tiles[id_] = list(map(list, raw_tile[1:]))
        return tiles

    def _get_possible_borders(self, tile):
        borders = [
            tile[0],  # top
            tile[-1],  # bottom
            [t[0] for t in tile],  # left
            [t[-1] for t in tile],  # right
        ]
        borders += [reversed(b) for b in borders]  # flip
        borders = [''.join(b) for b in borders]
        return borders

    def _are_neighbors(self, tile_1, tile_2):
        for b1 in self._get_possible_borders(tile_1):
            for b2 in self._get_possible_borders(tile_2):
                if b1 == b2:
                    return True
        return False

    def _find_neighbors(self, tile):
        neighbors = list()
        for neighbor_key, neighbor_value in self.tiles.items():
            if tile == neighbor_key:
                continue
            if self._are_neighbors(self.tiles[tile], neighbor_value):
                neighbors.append(neighbor_key)
        return neighbors

    def _find_corners(self):
        corners = [
            tile for tile in self.tiles
            if len(self._find_neighbors(tile)) == 2
        ]
        return corners

    def corners_multiplication(self):
        corners = self._find_corners()
        result = 1
        for corner in corners:
            result *= corner
        return result
    
    def rotate(self, img):
        return list(zip(*reversed(img)))

    def _get_reflections(self, image):
        image = deepcopy(image)
        flip = [i[::-1] for i in image]
        for img in (image, flip):
            yield img  # 0
            yield self.rotate(img)  # 90
            yield self.rotate(self.rotate(img))  # 180
            yield self.rotate(self.rotate(self.rotate(img)))  # 270

    def reassemble(self):
        """Reassemble the image from any tile."""
        left = lambda x: [t[0] for t in x]
        right = lambda x: [t[-1] for t in x]
        def _arrange(arrangement, tile, image, y, x):
            arrangement[tile] = (y, x, image)
            for neighbor in self._find_neighbors(tile):
                if neighbor not in arrangement.keys():
                    for n_img in self._get_reflections(self.tiles[neighbor]):
                        if n_img[-1] == image[0]:  # top
                            _arrange(arrangement, neighbor, n_img, y - 1, x)
                        elif n_img[0] == image[-1]:  # bottom
                            _arrange(arrangement, neighbor, n_img, y + 1, x)
                        elif right(n_img) == left(image):  # left
                            _arrange(arrangement, neighbor, n_img, y, x - 1)
                        elif left(n_img) == right(image):  # right
                            _arrange(arrangement, neighbor, n_img, y, x + 1)
                        else:
                            continue
                        break  # skip other reflections once it matches one

        tile = next(iter(self.tiles.keys()))
        image = self.tiles[tile]
        arrangement = dict()
        _arrange(arrangement, tile, image, 0, 0)

        def _connect(full_image, tile, y):
            tile_size = len(tile) - 2
            for tile_y, tile_row in enumerate(tile[1:-1]):
                y_position = tile_y + tile_size * y
                if y_position >= len(full_image):
                    full_image.append(list())
                full_image[y_position] += (tile_row[1:-1])

        full_image = list()
        y_values = [p[0] for p in arrangement.values()]
        x_values = [p[1] for p in arrangement.values()]
        for y in range(min(y_values), max(y_values) + 1):
            shift_y = y - min(y_values)
            for x in range(min(x_values), max(x_values) + 1):
                for tile, position in arrangement.items():
                    if position[0] == y and position[1] == x:
                        _connect(full_image, position[2], shift_y)
        return full_image

    def detect(self, pattern):
        counter = 0
        window_size = (len(pattern), len(pattern[0]))
        for reflection in self._get_reflections(self.full_image):
            for y in range(len(reflection) - window_size[0]):
                for x in range(len(reflection[y]) - window_size[1]):
                    detected = True
                    for window_y in range(window_size[0]):
                        for window_x in range(window_size[1]):
                            if (
                                pattern[window_y][window_x] == '#' and
                                reflection[y + window_y][x + window_x] != '#'
                            ):
                                detected = False
                                break  # stops pattern check
                        if not detected:
                            break  # stops pattern check
                    if detected:
                        counter += 1
            if counter:  # assuming there are patters only in one reflection
                return counter

    def count_pounds(self, pattern):
        pattern_match = self.detect(pattern)
        image_pounds = sum([x.count('#') for x in self.full_image])
        pattern_pounds = sum([x.count('#') for x in pattern])
        return image_pounds - pattern_pounds * pattern_match


def main():
    with open('inputs/day_20.txt') as input_file:
        data = input_file.read()
    camera = Camera(data)
    print(camera.corners_multiplication())

    sea_monster = [list(x) for x in [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]]

    print(camera.detect(sea_monster))
    print(camera.count_pounds(sea_monster)) 


if __name__ == '__main__':
    main()