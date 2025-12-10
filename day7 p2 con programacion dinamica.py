first, *rest = open("day7.txt")


a = 0
b = [c == "S" for c in first]

for line in rest:
    for i in range(len(line)):
        if line[i] == "^":
            a += bool(b[i])
            b[i - 1] += b[i]
            b[i + 1] += b[i]
            b[i] = 0


print(a, sum(b))
