with open("day5.txt") as f:
    lines = f.readlines()
    i = lines.index("\n")
    fresh_ranges = [list(map(int, line.strip().split("-"))) for line in lines[:i]]
    ingredients = [int(line.strip()) for line in lines[i + 1 :]]


def part1():
    # Just boolean check, break after first match
    fresh = 0

    for ingredient in ingredients:
        for min, max in fresh_ranges:
            if min <= ingredient <= max:
                fresh += 1
                break

    return fresh


print("Part 1:", part1())


def part2():
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])

    merged = True

    while merged:
        merged_ranges = []
        merged_ranges.append(sorted_ranges[0])
        merged = False

        for i in range(1, len(sorted_ranges)):
            if sorted_ranges[i][0] <= sorted_ranges[i - 1][1]:
                merged_ranges[-1][1] = max(sorted_ranges[i][1], merged_ranges[-1][1])
                merged = True
            else:
                merged_ranges.append(sorted_ranges[i])

        sorted_ranges = merged_ranges

    return sum([x[1] - x[0] + 1 for x in sorted_ranges])


print(f"Part 2: {part2()}")
