def parse(input_file):
    template, insertion_rules = input_file.read().split("\n\n")
    rules = dict()
    for rule in insertion_rules.split("\n"):
        pair, insertion = rule.strip().split(" -> ")
        rules[pair] = insertion
    return (template, rules)


def count_chars(text):
    return {c: text.count(c) for c in set(text)}


def part_1(input_data):
    template, rules = input_data
    new_polymer = polymer = template
    steps = 10
    for _ in range(steps):
        for i in range(len(polymer) - 1):
            element = rules[polymer[i : i + 2]]
            new_polymer = new_polymer[: i + i + 1] + element + new_polymer[i + i + 1 :]
        polymer = new_polymer
    counter = count_chars(polymer)
    return max(counter.values()) - min(counter.values())


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, values):
        self.root = None
        for value in values:
            node = Node(value)
            if self.root is None:
                self.root = node
            else:
                current = self.root
                while current.next is not None:
                    current = current.next
                current.next = node

    def __str__(self):
        values = ""
        current = self.root
        while current is not None:
            values += current.value
            current = current.next
        return values


def part_1_linked_list(input_data):
    template, rules = input_data
    polymer = LinkedList(template)
    steps = 10
    for _ in range(steps):
        current = polymer.root
        while current.next is not None:
            element = Node(rules[current.value + current.next.value])
            current_next = current.next
            element.next = current_next
            current.next = element
            current = current_next
    counter = count_chars(str(polymer))
    return max(counter.values()) - min(counter.values())


def count_from_pairs(pairs):
    counter = {}
    for pair in pairs:
        counter[pair[0]] = counter.setdefault(pair[0], 0) + pairs[pair]
        counter[pair[1]] = counter.setdefault(pair[1], 0) + pairs[pair]
    counter = {k: v // 2 - 1 for k, v in counter.items()}
    return counter


def part_2(input_data):
    template, rules = input_data
    polymer = template
    pairs = {}
    for i in range(len(polymer) - 1):
        key = f"{polymer[i]}{polymer[i+1]}"
        pairs[key] = pairs.setdefault(key, 0) + 1

    steps = 40
    for _ in range(steps):
        new_pairs = {}
        for pair in pairs:
            element = rules[pair]
            key_left = f"{pair[0]}{element}"
            new_pairs[key_left] = new_pairs.setdefault(key_left, 0) + pairs[pair]
            key_right = f"{element}{pair[1]}"
            new_pairs[key_right] = new_pairs.setdefault(key_right, 0) + pairs[pair]
        pairs = new_pairs
    # Doubles the first and last template elements
    adjust_key = f"{template[0]}{template[-1]}"
    pairs[adjust_key] = pairs.setdefault(adjust_key, 0) + 1
    counter = count_from_pairs(pairs)
    return max(counter.values()) - min(counter.values())


def main():
    with open(
        "2021/inputs/day_14.txt"
    ) as input_file:
        input_data = parse(input_file)

    print(f"part_1: {part_1(input_data)}")
    print(f"part_1: {part_1_linked_list(input_data)}")
    print(f"part_2: {part_2(input_data)}")


if __name__ == "__main__":
    main()

"""
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?


--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
"""
