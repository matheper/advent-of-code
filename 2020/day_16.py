"""
--- Day 16: Ticket Translation ---


As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?


--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?


https://adventofcode.com/2020/day/16
"""

class TrainTicket:
    def __init__(self, rules, ticket, nearby):
        self.rules = self._parse_rules(rules)
        self.ticket = self._parse_tickets(ticket)[0]
        self.nearby = self._parse_tickets(nearby)

    def _parse_rules(self, raw_rules):
        rules = {}
        for rule in raw_rules.split('\n'):
            key, values = rule.split(': ')
            rules[key] = []
            for range_ in values.split(' or '):
                value_1, value_2 = range_.split('-')
                rules[key].append((int(value_1), int(value_2)))
        return rules

    def _parse_tickets(self, raw_tickets):
        tickets = []
        for ticket in raw_tickets.split('\n')[1:]:
            tickets.append(list(map(int, ticket.split(','))))
        return tickets

    def _is_valid(self, value, rule):
        for range_ in rule:
            min_value, max_value = range_
            if min_value <= value <= max_value:
                return True
        return False

    def _is_value_valid(self, value):
        for rule in self.rules.values():
            if self._is_valid(value, rule):
                return True
        return False

    def scanning_error_rate(self):
        invalids = []
        for ticket in self.nearby:
            for value in ticket:
                if not self._is_value_valid(value):
                    invalids.append(value)
        return sum(invalids)

    def _get_valid_tickets(self):
        valid = []
        for ticket in self.nearby:
            is_valid = True
            for value in ticket:
                if not self._is_value_valid(value):
                    is_valid = False
                    break
            if is_valid:
                valid.append(ticket)
        return valid

    def _get_possible_order(self):
        all_tickets = [self.ticket] + self._get_valid_tickets()
        possible_order = {}
        for key, rule in self.rules.items():
            # iterate over each field of a ticket
            for index in range(len(self.ticket)):
                valid = [
                    self._is_valid(ticket[index], rule)
                    for ticket in all_tickets
                ]
                if all(valid):
                    possible_order[key] = possible_order.get(key, list())
                    possible_order[key].append(index)
        return possible_order

    def _order_fields(self):
        possible_order = self._get_possible_order()
        ordered_fields = dict()
        keys = list(possible_order)
        while keys:
            for key in keys:
                if len(possible_order[key]) == 1:
                    position = possible_order[key][0]
                    ordered_fields[key] = position
                    keys.remove(key)
                    for k in keys:
                        possible_order[k].remove(position)
        return ordered_fields

    def departure(self):
        ordered_fields = self._order_fields()
        indexes = [
            index for key, index in ordered_fields.items()
            if key.startswith('departure')
        ]
        result = 1
        for i in indexes:
            result *= self.ticket[i]
        return result

def main():
    with open('inputs/day_16.txt') as input_file:
        rules, ticket, nearby = input_file.read().split('\n\n')
    
    train_ticket = TrainTicket(rules, ticket, nearby)
    print(train_ticket.scanning_error_rate())
    print(train_ticket.departure())



if __name__ == '__main__':
    main()