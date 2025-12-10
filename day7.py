import functools


class State:
    def __init__(self, debug=False):
        self.cycle = 0
        self.splits = 0
        self.layers = []
        self.debug = debug

    def load_data(self, path):
        with open(path) as f:
            self.layers = [[char for char in lines.strip()] for lines in f.readlines()]
            self.cycle = 0
            self.splits = 0
            if self.debug:
                print(self)
            return self.layers

    def __repr__(self):
        return "\n".join(
            [f"Cycle: {self.cycle} Splits: {self.splits}"]
            + [" ".join(layer) for layer in self.layers]
        )

    def process_next_layer(self):

        if self.cycle >= len(self.layers) - 1:
            print(f"No more layers to process. Total splits: {self.splits}")
            return False

        if "S" in self.layers[self.cycle]:
            position = self.layers[self.cycle].index("S")
            # check if there is a refractor (^) on the next layer, else beam moves down (|)

            if self.layers[self.cycle + 1][position] == "^":
                self.layers[self.cycle + 1][position + 1] = "|"
                self.layers[self.cycle + 1][position - 1] = "|"
                self.splits += 1

            elif self.layers[self.cycle + 1][position] == ".":
                self.layers[self.cycle + 1][position] = "|"

        else:  # not "S", so we are moving in the following layers.
            for idx, char in enumerate(self.layers[self.cycle]):
                if char == "|":
                    if self.layers[self.cycle + 1][idx] == "^":
                        self.layers[self.cycle + 1][idx + 1] = "|"
                        self.layers[self.cycle + 1][idx - 1] = "|"
                        self.splits += 1

                    elif self.layers[self.cycle + 1][idx] == ".":
                        self.layers[self.cycle + 1][idx] = "|"

        self.cycle += 1
        if self.debug:
            print(self)

        return True


@functools.lru_cache(maxsize=None)
def count_paths(r, c, grid_tuple):
    """Count unique paths from position (r, c) to the bottom of the grid."""
    grid = [list(row) for row in grid_tuple]
    
    num_rows = len(grid)
    num_cols = len(grid[0])

    # base case. out of bounds
    if not (0 <= r < num_rows and 0 <= c < num_cols):
        if r >= num_rows:  # successfully exited the grid
            return 1
        return 0

    current_char = grid[r][c]

    # base case. hit an empty space
    if current_char in (".", "^"):
        return 0

    # next move
    paths_from_here = 0

    if current_char in ("|", "S"):
        # move down and check 0 and ±1 columns from the previous position
        for dc_offset in (-1, 0, 1):
            paths_from_here += count_paths(r + 1, c + dc_offset, grid_tuple)

    return paths_from_here


if __name__ == "__main__":
    state = State(debug=True)
    data = state.load_data("test7.txt")
    while state.process_next_layer():
        pass

    result = count_paths(0, data[0].index("S"), data)
    print(f"Total unique paths: {result}")
    grid_tuple = tuple(tuple(row) for row in data)
    result = count_paths(0, data[0].index("S"), grid_tuple)
    print(f"Total unique paths: {result}")
