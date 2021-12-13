def parse(input_file):
    input_data = []
    for row in input_file:
        input_data.append(list(map(int, row.strip())))
    return input_data


def part_1(input_data):
    low_points = []
    for i, row in enumerate(input_data):
        for j, value in enumerate(row):
            if not (
                i - 1 >= 0 and value >= input_data[i - 1][j] or
                j - 1 >= 0 and value >= input_data[i][j - 1] or
                j + 1 < len(row) and value >= input_data[i][j + 1] or
                i + 1 < len(input_data) and value >= input_data[i + 1][j]
            ):
                low_points.append(value)
    print(low_points)
    return sum(low_points) + len(low_points)


def part_2(input_data):
    pass


def main():
    with open("../inputs/day_09.txt") as input_file:
        input_data = parse(input_file)

    print(f"part_1: {part_1(input_data)}")
    print(f"part_2: {part_2(input_data)}")


if __name__ == "__main__":
    main()


"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
"""
