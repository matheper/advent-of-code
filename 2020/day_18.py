"""
--- Day 18: Operation Order ---


As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?


--- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?


https://adventofcode.com/2020/day/18
"""


class StrangeMath:
    def __init__(self, operations):
        self.operations = operations
        self.operator_map = {
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
        }

    def _no_precedence(self, operands, operators):
        result = operands[0]
        for operand, operator in zip(operands[1:], operators):
            result = self.operator_map[operator](result, operand)
        return result

    def _sum_precedence(self, operands, operators):
        while True:
            try:
                index = operators.index('+')
                operands[index] = self.operator_map[operators[index]](
                    operands[index], operands[index + 1]
                )
                operands.pop(index + 1)
                operators.pop(index)
            except ValueError:
                break
        result = operands.pop(0)
        for operator in operators:
            result = self.operator_map[operator](result, operands.pop(0))
        return result

    def _compute(self, operands, operators, precedence):
        if precedence:
            return self._sum_precedence(operands, operators)
        return self._no_precedence(operands, operators)

    def evaluate(self, operation, precedence, index=0):
        operands = []
        operators = []
        while index < len(operation):
            if operation[index] == '(':
                op, index = self.evaluate(operation, precedence, index + 1)
                operands.append(op)
            elif operation[index] == ')':
                return (self._compute(operands, operators, precedence), index)
            elif operation[index] in ('+', '*'):
                operators.append(operation[index])
            else:
                operands.append(int(operation[index]))
            index += 1
        result = self._compute(operands, operators, precedence)
        return result

    def sun_results(self, precedence):
        return sum([self.evaluate(op, precedence) for op in self.operations])

def main():
    with open('inputs/day_18.txt') as input_file:
        operations = input_file.read().splitlines()
        operations = [i.replace(' ', '') for i in operations]
    strange_math = StrangeMath(operations)
    print(strange_math.sun_results(precedence=False))
    print(strange_math.sun_results(precedence=True))

if __name__ == '__main__':
    main()