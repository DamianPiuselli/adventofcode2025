with open("input9.txt") as f:
    lines = f.read().splitlines()
    coords = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines]


from itertools import combinations

all_rectangles = combinations(coords, 2)

max_area = 0
coord1, coord2 = None, None

for rect in all_rectangles:
    (x1, y1), (x2, y2) = rect
    area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
    if area > max_area:
        max_area = area
        coord1, coord2 = (x1, y1), (x2, y2)

print(f"Max area: {max_area} between points {coord1} and {coord2}")
