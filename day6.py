import math
from collections import defaultdict


def part1():
    data = defaultdict(list)

    with open("day6.txt") as f:
        lines = f.readlines()

        for line in lines:
            for i, token in enumerate(line.split()):
                data[i].append(token)

    # data stored as strings, last field is the operation for that "column"
    subtotals = []
    for key, values in data.items():
        operation = values.pop()

        match operation:
            case "*":
                subtotals.append(math.prod(int(v) for v in values))
            case "+":
                subtotals.append(sum(int(v) for v in values))

    return sum(subtotals)


def part2():
    # Parsing the data its a lot more complex, we care about spaces and we should parse column wise
    # we can use the operator sybol to distinguish between the "first column" for each problem.
    # we start by mapping the data into a bidimensional array

    # (x,y) is (column,row)
    data = defaultdict(tuple[int, int])

    with open("day6.txt") as f:
        lines = [line.strip("\n") for line in f.readlines()]

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                data[(x, y)] = char

    # now we have the data mapped, we can start implementing the logic
    # the row with the operations will be used to "index" the problems
    operations_row = max((y for x, y in data.keys() if data[(x, y)] in ("*", "+")))
    columns = max(x for x, y in data.keys())

    # read one column at a time
    subtotal = []
    operation = None
    block_values = []

    for x in range(columns + 1):
        curr_value = ""

        if not all(data[(x, y)] == " " for y in range(operations_row)):
            for y in range(operations_row + 1):
                char = data[(x, y)]
                if char == " ":
                    continue
                elif char in ("*", "+"):
                    operation = char
                else:
                    curr_value += char
            if curr_value:
                block_values.append(curr_value)

        # if column of spaces, operate on block values and append to subtotal
        if all(data[(x, y)] == " " for y in range(operations_row)) or x == columns:
            if operation and block_values:
                match operation:
                    case "*":
                        subtotal.append(math.prod(int(v) for v in block_values))
                    case "+":
                        subtotal.append(sum(int(v) for v in block_values))
            # reset for next block
            block_values = []
            operation = None

    return sum(subtotal)


# print(part1())
print(part2())
