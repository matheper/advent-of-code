"""
--- Day 17: Conway Cubes ---
As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###
Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......
After the full six-cycle boot process completes, 112 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?


https://adventofcode.com/2020/day/17
"""

from copy import deepcopy

class CubeSpace:
    def __init__(self, grid):
        self.active_cubes = set()
        for y, row in enumerate(grid):
            for x, cube in enumerate(row):
                if cube == '#':
                    self.active_cubes.add((0, y, x))

    def count_active(self):
        return len(self.active_cubes)

    def get_active_neighbors(self, cube):
        active_neighbors = 0
        for z in range(cube[0] - 1, cube[0] + 2):
            for y in range(cube[1] - 1, cube[1] + 2):
                for x in range(cube[2] - 1, cube[2] + 2):
                    if (z, y, x) != cube and (z, y, x) in self.active_cubes:
                        active_neighbors += 1
        return active_neighbors

    def _update_active_cube(self, cube, active_cubes):
        active_neighbors = self.get_active_neighbors(cube)
        if active_neighbors not in (2, 3):
            active_cubes.remove(cube)

    def _update_inactive_neighbors(self, cube, active_cubes):
        for z in range(cube[0] - 1, cube[0] + 2):
            for y in range(cube[1] - 1, cube[1] + 2):
                for x in range(cube[2] - 1, cube[2] + 2):
                    neighbor = (z, y, x)
                    if neighbor != cube and neighbor not in self.active_cubes:
                        active_neighbors = self.get_active_neighbors(neighbor)
                        if active_neighbors == 3:
                            active_cubes.add(neighbor)

    def _cicle(self):
        temp_active_cubes = deepcopy(self.active_cubes)
        for cube in self.active_cubes:
            self._update_active_cube(cube, temp_active_cubes)
            self._update_inactive_neighbors(cube, temp_active_cubes)
        self.active_cubes = temp_active_cubes

    def boot(self, cicles):
        for cicle in range(cicles):
            self._cicle()
        return self.count_active()


def main():
    with open('inputs/day_17.txt') as input_file:
        initial_grid = input_file.read().splitlines()
    space = CubeSpace(initial_grid)
    print(space.boot(6))


if __name__ == '__main__':
    main()