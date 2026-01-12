## Data structure
#  xyz: abc def ghi   #Position: *outputs

## Part 1, given a starting and ending positions, find all the possible paths between them through
# the network. Multiple possible endings, one single starting point.

# The data encodes a network, since I want find all paths and not the shortest path, I will use DFS.

adjacency_list = {}

for line in open("input11.txt"):
    node, *neighbors = line.replace(":", "").split()
    adjacency_list[node] = neighbors


def find_all_paths(adjacency_list, start, end, path=[]):
    # add the starting node to the current path
    path = path + [start]

    if start == end:
        return [path]  # found a path

    if start not in adjacency_list:
        return []  # no path found

    paths = []
    for node in adjacency_list[start]:
        if node not in path:  # avoid cycles, just 1 visit per node
            new_paths = find_all_paths(adjacency_list, node, end, path)
            for p in new_paths:
                paths.append(p)

    return paths


all_routes = find_all_paths(adjacency_list, "you", "out")
print(f"part 1 answer: {len(all_routes)}")

## part 2, all valid paths must pass through "fft" and "dac" nodes. New starting node is "svr"
## Seems that with those values the number of paths explodes...

## New approach. Calculate subpaths and combine them.
#   valid paths:
#   svr --> fft --> dac --> out  OR svr --> dac --> fft --> out
#   subpaths:
#   svr --> fft, fft --> dac, dac --> out
#   svr --> dac, dac --> fft, fft --> out

## STILL TOO SLOW! T.T, needs another approach...
# svr_to_fft = find_all_paths(adjacency_list, "svr", "fft")
# fft_to_dac = find_all_paths(adjacency_list, "fft", "dac")
# dac_to_out = find_all_paths(adjacency_list, "dac", "out")
# svr_to_dac = find_all_paths(adjacency_list, "svr", "dac")
# dac_to_fft = find_all_paths(adjacency_list, "dac", "fft")
# fft_to_out = find_all_paths(adjacency_list, "fft", "out")

# NEW APPROACH: Count paths instead of listing them all, also use memoization to speed up the process

from functools import lru_cache


@lru_cache(maxsize=None)
def count_paths(current_node, target):
    # base case 1
    if current_node == target:
        return 1

    # base case 2
    if current_node not in adjacency_list:
        return 0

    total_paths = 0
    for neighbor in adjacency_list[current_node]:
        total_paths += count_paths(neighbor, target)
    return total_paths


svr_to_fft = count_paths("svr", "fft")
fft_to_dac = count_paths("fft", "dac")
dac_to_out = count_paths("dac", "out")
svr_to_dac = count_paths("svr", "dac")
dac_to_fft = count_paths("dac", "fft")
fft_to_out = count_paths("fft", "out")

part2_answer = (svr_to_fft * fft_to_dac * dac_to_out) + (
    svr_to_dac * dac_to_fft * fft_to_out
)
print(f"part 2 answer: {part2_answer}")
