"""
--- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?


--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

https://adventofcode.com/2020/day/1
"""

def find_expense_entries_trio(entries, target=2020):
    len_ = len(entries)
    for i in range(len_):
        for j in range(i + 1, len_):
            for k in range(j + 1, len_):
                if entries[i] + entries[j] + entries[k] == target:
                    return entries[i] * entries[j] * entries[k]


def find_expense_entries(entries, target=2020):
    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            if entries[i] + entries[j] == target:
                return entries[i] * entries[j]


def find_expense_entries_any_size(entries, target, combination_size):
    """
    This function creates all possible combinations of combination_size until a valid combination is found.
    The recursion allow combinations of any size instead of fixed `for` statements for each combination_size.
    """
    def _find_expenses_entries(
            entries, target, size, entries_index,
            temp_index, temp_list, expense_result
    ):
        if temp_index >= size:
            if sum(temp_list) == target:
                expense_result[0] = 1
                for expense in temp_list:
                    expense_result[0] *= expense
                expense_result[1] = True
            return
        for i in range(entries_index, len(entries)):
            if not expense_result[1]:
                temp_list[temp_index] = entries[i]
                _find_expenses_entries(
                    entries=entries,
                    target=target,
                    size=size,
                    entries_index=i + 1,
                    temp_index=temp_index + 1,
                    temp_list=temp_list,
                    expense_result=expense_result,
                )

    temp_list = [0] * combination_size
    expense_result = [1, False]
    _find_expenses_entries(
        entries, target, combination_size, 0, 0, temp_list, expense_result
    )
    return expense_result[0] if expense_result[1] else None


def main():
    with open('inputs/day_01.txt') as input_file:
        entries = [int(i) for i in input_file]
    print(find_expense_entries(entries))
    print(find_expense_entries_any_size(entries, 2020, 2))
    print(find_expense_entries_trio(entries))
    print(find_expense_entries_any_size(entries, 2020, 3))
    print(find_expense_entries(entries, 431424))
    print(find_expense_entries_any_size(entries, 431424, 2))

if __name__ == '__main__':
    main()