with open("day8.txt") as f:
    coordinates = [line.strip().split(",") for line in f.readlines()]
    coordinates = [(int(x), int(y), int(z)) for x, y, z in coordinates]

# calculate the distance for each unique pair of coordinates
from math import sqrt
from itertools import combinations

unique_pairs_coords = [*combinations(coordinates, 2)]

distances = []

for (x1, y1, z1), (x2, y2, z2) in unique_pairs_coords:
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    distances.append(distance)

paired_list = list(zip(unique_pairs_coords, distances))
paired_list.sort(key=lambda x: x[1])

# build the connecting circuits from the shortest 10 distances
from collections import defaultdict

network = defaultdict(list)  # map id (int) to list of connected coords
next_id = 0

# iter over first 1000 for part 1, over all for part 2.
for (coord1, coord2), distance in paired_list:
    # for part2
    network_current_values = [val for sublist in network.values() for val in sublist]
    if len(network_current_values) == len(coordinates):
        break  # all coordinates are now connected

    last_connection = coord1, coord2  # keep track of last connection made

    # if both coords not in network, create new subnetwork
    if coord1 not in network_current_values and coord2 not in network_current_values:
        network[next_id].append(coord1)
        network[next_id].append(coord2)
        next_id += 1

    # if both coords in network,
    elif coord1 in network_current_values and coord2 in network_current_values:
        # find their subnetworks
        key1, key2 = None, None
        for key, value in network.items():
            if coord1 in value:
                key1 = key
            if coord2 in value:
                key2 = key
        # if they are in different subnetworks, merge them
        if key1 != key2:
            network[key1].extend(network[key2])
            del network[key2]

    # if one coord in network, add the other to the same subnetwork
    elif coord1 in network_current_values:
        for key, value in network.items():
            if coord1 in value:
                network[key].append(coord2)
                break
    elif coord2 in network_current_values:
        for key, value in network.items():
            if coord2 in value:
                network[key].append(coord1)
                break


# lens = [len(value) for value in network.values()]
# lens.sort()
# print(f"part 1: product of three largest subnetworks: {lens[-1] * lens[-2] * lens[-3]}")

print(f"part 2 response{last_connection[0][0]*last_connection[1][0]}")
