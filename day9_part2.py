from itertools import combinations, pairwise

with open("input9.txt") as f:
    lines = f.read().splitlines()
    red = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines]


def area(pair_of_coords):
    (x, y), (u, v) = pair_of_coords
    return (abs(x - u) + 1) * (abs(y - v) + 1)


# All possible rectangles from red points, sorted by decreasing area
pairs = list(combinations(red, 2))
pairs.sort(key=area, reverse=True)

# all lines that delimit the polygon
lines = []
for a, b in pairwise(red + [red[0]]):  # closing the polygon
    x, y = a
    u, v = b
    lines.append((min(x, u), min(y, v), max(x, u), max(y, v)))  # (x1, y1, x2, y2)

# sort by decreasing size
lines.sort(key=lambda p: p[3] + p[2] - p[1] - p[0], reverse=True)

for coord1, coord2 in pairs:
    x, y, u, v = (
        min(coord1[0], coord2[0]),
        min(coord1[1], coord2[1]),
        max(coord1[0], coord2[0]),
        max(coord1[1], coord2[1]),
    )
    for p, q, r, s in lines:
        if p < u and q < v and r > x and s > y:
            break

    else:
        print("p2:", area((coord1, coord2)))
        break
