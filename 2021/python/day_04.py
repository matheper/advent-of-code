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
        "../inputs/day_04.txt"
    ) as input_file:
        input_data = input_file.read()
    sequence, boards = parse_input(input_data)
    winner_score = part_1(sequence, boards)
    print(winner_score)

    loser_score = part_2(sequence, boards)
    print(loser_score)


if __name__ == "__main__":
    main()