"""
--- Day 7: Handy Haversacks ---


You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)


https://adventofcode.com/2020/day/7
"""

import re


def parse_rules(rules):
    luggage_rules = dict()
    for rule in rules:
        rule = rule.replace('contain', ',')
        rule = re.sub(r'\d+|bags|bag|no other|\.', '', rule)
        bags = [b.strip() for b in rule.split(',')]
        luggage_rules[bags[0]] = {bag: 0 for bag in bags[1:] if bag}
    return luggage_rules


def count_bags(luggage_rules, bag_color, target_color, count_allow_color, visited):
    if bag_color == target_color:
        return 1

    visited.add(bag_color)
    allow_bag = 0
    for bag in luggage_rules[bag_color]:
        if bag not in visited:
            count = count_bags(luggage_rules, bag, target_color, count_allow_color, visited)
            count_allow_color[bag] = count
            allow_bag = max(allow_bag, count)
        else:
            allow_bag = max(allow_bag, count_allow_color[bag])
    return allow_bag


def allow_bag_colors(luggage_rules, target_color):
    number_of_bags = 0
    count_allow_color = {bag: 0 for bag in luggage_rules}
    visited = set()
    for bag_color in luggage_rules:
        if bag_color not in visited:
            count_allow_color[bag_color] = count_bags(luggage_rules, bag_color, target_color, count_allow_color, visited)
    return sum(count_allow_color.values()) - 1  # remove the target color itself


def main():
    luggage_rules = [
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.',
    ]

    luggage_rules = parse_rules(luggage_rules)
    bag_color = 'shiny gold'
    print(allow_bag_colors(luggage_rules, bag_color))

    with open('inputs/day_07.txt') as input_file:
        luggage_rules = input_file.read().split('\n')
    luggage_rules = parse_rules(luggage_rules)
    bag_color = 'shiny gold'
    print(allow_bag_colors(luggage_rules, bag_color))

if __name__ == '__main__':
    main()