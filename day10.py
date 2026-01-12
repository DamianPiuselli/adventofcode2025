from collections import deque


def parse(path):
    with open(path) as f:
        lines = f.read().strip().splitlines()

    for line in lines:
        tokens = line.split()

        target_str = tokens[0][1:-1]  # Remove surrounding parentheses
        joltages = eval(tokens[-1].replace("{", "[").replace("}", "]"))
        switches_indices = [eval(token.replace(")", ",)")) for token in tokens[1:-1]]

        yield target_str, switches_indices, joltages


def solve_part1(target_str, switches_indices):
    # 1. Setup the target (####..##..)
    # Mapping '#' to 1 and '.' to 0.
    # We read left-to-right, so index 0 is the leftmost bit.

    target = sum(1 << i for i, char in enumerate(target_str) if char == "#")

    # Convert switch indices into bitmasks
    switches = []
    for indices in switches_indices:
        mask = 0
        for idx in indices:
            mask |= 1 << idx
        switches.append(mask)

    # 3. BFS
    queue = deque([(0, [])])  # (current_state, list_of_switches_pressed)
    visited = {0}

    while queue:
        current_state, path = queue.popleft()

        if current_state == target:
            return path

        for i, switch_mask in enumerate(switches):
            # XOR toggles the bits
            next_state = current_state ^ switch_mask

            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [i]))

    return None


if __name__ == "__main__":
    part1 = 0

    for target_str, switches_indices, joltages in parse("input10.txt"):
        solution = solve_part1(target_str, switches_indices)
        part1 += len(solution) if solution is not None else 0
        if solution is not None:
            print(f"Target: {target_str}, Switches pressed: {solution}")
        else:
            print(f"Target: {target_str}, No solution found.")

    print(f"Part 1: {part1}")
