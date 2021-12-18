def parse(input_file):
    input_data = []
    for line in input_file:
        input_data.append([int(x) for x in line.strip()])
    return input_data


def get_next_node(queue, distances):
    items = [(x, distances[x]) for x in queue]
    return min(items, key=lambda x: x[1])[0]


def dijkstra(graph, source, target):
    queue = set()
    distances = dict()
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            queue.add((x, y))
            distances[(x, y)] = float("inf")
    distances[source] = 0

    while queue:
        u = get_next_node(queue, distances)
        queue.remove(u)
        for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            next_x = u[0] + x
            next_y = u[1] + y
            if (
                next_x >= 0
                and next_y >= 0
                and next_x <= target[0]
                and next_y <= target[1]
            ):
                neighbour = (next_x, next_y)
                dist = distances[u] + graph[next_x][next_y]
                if dist < distances[neighbour]:
                    distances[neighbour] = dist
    return distances[target]


def part_1(input_data):
    source = (0, 0)
    target = (len(input_data) - 1, len(input_data[0]) - 1)
    min_distance = dijkstra(input_data, source, target)
    return min_distance


def part_2(input_data):
    pass


def main():
    with open("2021/inputs/day_15.txt") as input_file:
        input_data = parse(input_file)

    print(f"part_1: {part_1(input_data)}")
    print(f"part_2: {part_2(input_data)}")


if __name__ == "__main__":
    main()

"""
--- Day 15: Chiton ---
You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?
"""
