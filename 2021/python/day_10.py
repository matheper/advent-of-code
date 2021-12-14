def parse(input_file):
    input_data = [x.strip() for x in input_file]
    return input_data


def find_first_illegal(line):
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    stack = []
    for char in line:
        if char in pairs.values():
            if not stack or stack[-1] not in pairs or pairs[stack[-1]] != char:
                return char
            stack.pop()
        else:
            stack.append(char)
    return "-"


def part_1(input_data):
    points = {
        "-": 0,
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    illegals = [find_first_illegal(line) for line in input_data]
    print(illegals)
    return sum([points[i] for i in illegals])


def part_2(input_data):
    pass


def main():
    with open("../inputs/day_10.txt") as input_file:

        input_data = parse(input_file)

    print(f"part_1: {part_1(input_data)}")
    print(f"part_2: {part_2(input_data)}")


if __name__ == "__main__":
    main()
