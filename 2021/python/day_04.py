class Board:
    def __init__(self, board_data):
        rows = []
        for line in board_data.split("\n"):
            numbers = list(map(int, line.strip().split(" ")))
            rows.append(numbers)
        self.rows = rows
        cols = []
        for col_idx in range(len(self.rows[0])):
            col = [row[col_idx] for row in self.rows]
            cols.append(col)
        self.cols = cols

    def contains_line(self, sequence):
        for row in self.rows:
            if all(x in sequence for x in row):
                return True
        for col in self.cols:
            if all(x in sequence for x in col):
                return True
        return False

    def sum(self, sequence):
        numbers = [x for row in self.rows for x in row]
        marked = [x if x in numbers else 0 for x in sequence]
        total = sum(numbers) - sum(marked)
        return total


def parse_input(input_data):
    data = input_data.replace("  ", " ").split("\n\n")
    sequence = list(map(int, data[0].split(",")))
    boards = []
    for board_data in data[1:]:
        boards.append(Board(board_data))
    return sequence, boards


def part_1(sequence, boards):
    drawn_values = []
    for value in sequence:
        drawn_values.append(value)
        for board in boards:
            if board.contains_line(drawn_values):
                return board.sum(drawn_values) * value
    return -1


def part_2(sequence, boards):
    drawn_values = []
    for value in sequence:
        drawn_values.append(value)
        idx = 0
        while idx < len(boards):
            board = boards[idx]
            if board.contains_line(drawn_values):
                last_board = boards.pop(idx)
                if not len(boards):
                    return last_board.sum(drawn_values) * value
            else:
                idx += 1
    return -1


def main():
    with open(
        "/Users/matheus/Projects/Algorithms/adventofcode/2021/inputs/day_04.txt"
    ) as input_file:
        input_data = input_file.read()
    sequence, boards = parse_input(input_data)
    winner_score = part_1(sequence, boards)
    print(winner_score)

    loser_score = part_2(sequence, boards)
    print(loser_score)


def test_day_04():
    input_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    sequence, boards = parse_input(input_data)
    winner_score = part_1(sequence, boards)
    assert winner_score == 4512

    loser_score = part_2(sequence, boards)
    assert loser_score == 1924


if __name__ == "__main__":
    main()
    # test_day_04()
