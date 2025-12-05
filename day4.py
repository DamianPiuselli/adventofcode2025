from collections import defaultdict


# store the coordinates of "@" values in a default dict
# do nothing with empty cells "."


def convolve(rolls):

    def _convolve(x, y):
        count = 0
        neighbors = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if (nx, ny) in rolls:
                count += 1
        return count

    n_rolls = defaultdict(str)

    for x, y in rolls:
        count = _convolve(x, y)
        if count >= 4:
            n_rolls[(x, y)] = "@"

    return n_rolls


with open("day4.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]
    rolls = defaultdict(str)

    for x, _ in enumerate(grid):
        for y, _ in enumerate(grid[0]):
            if grid[x][y] == "@":
                rolls[(x, y)] = "@"
    print(rolls)

# count starting number of rolls "@"
n_rolls_per_iter = [len(rolls)]
last_len = len(rolls)

# iterate until no changes occur, ie no rolls can be removed.
while True:
    rolls = convolve(rolls)
    n_rolls_per_iter.append(len(rolls))
    if len(rolls) == last_len:
        break
    last_len = len(rolls)

print(f"part 1: {n_rolls_per_iter[0] - n_rolls_per_iter[1]}")
print(f"part 2: {n_rolls_per_iter[0] - n_rolls_per_iter[-1]}")
