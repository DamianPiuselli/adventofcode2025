# --- Day 1: Secret Entrance ---

## Part 1
with open("input1.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    # L moves dial to negatives, R to positives. positions are a cycle between 0-99
    data = [int(line.replace("L", "-").replace("R", "")) for line in data]

position = 50  # starting position
n0 = 0  # number of times we stop at 0

for move in data:
    position = (position + move) % 100  # Mod100 to represent the cycle
    if position == 0:
        n0 += 1
print(f"Final position: {position}, number of times at 0: {n0}")

## Part 2 -> count each time it passes zero (or stop at zero)
### obs: take into account that a single move can pass zero multiple times
### Dumb approach because numbers are small. If the moves were enormous, we would use pure modular arithmetic.

with open("input1.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    # L moves dial to negatives, R to positives. positions are a cycle between 0-99
    data = [int(line.replace("L", "-").replace("R", "")) for line in data]

pos = 50
n0 = 0  # number of times we pass or stop at 0

for move in data:
    if move > 0:
        # moving right
        for step in range(1, move + 1):
            pos = (pos + 1) % 100
            if pos == 0:
                n0 += 1
    else:
        # moving left
        for step in range(1, abs(move) + 1):
            pos = (pos - 1) % 100
            if pos == 0:
                n0 += 1

print(f"Final position: {pos}, number of times at or passed 0: {n0}")
