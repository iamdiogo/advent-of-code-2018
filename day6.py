"""
Day 6, incomplete
"""

f = open('input/day6.txt')

points = []
for line in f:
    x, y = line.rstrip().replace(',', '').split()
    points.append([int(x), int(y)])

for e in points:
    print(e)


print()
max_x = max(points)[0]
max_y = max(points, key=lambda x: x[1])[1]


# Generate grid1
grid1_size = 500
grid1_row = [None] * grid1_size
grid1 = []
for i in range(grid1_size):
    grid1.append(grid1_row[:])

# Generate grid2
grid2_size = 1000
grid2_row = [None] * grid2_size
grid2 = []
for i in range(grid2_size):
    grid2.append(grid2_row[:])


def calculate_distance(c1, c2):
    dx = abs(c2[0] - c1[0])
    dy = abs(c2[1] - c1[1])
    return [dx, dy]

def get_closest_point(coordinates):
    distances = []
    for p in points:
        distances.append(calculate_distance(p, coordinates))
    minimum = min(distances)
    count_closest = distances.count(minimum)
    if count_closest == 1:
        return distances.index(minimum)
    else:
        print("same")
        return -1

for i, row in enumerate(grid1):
    for j, element in enumerate(row):
        grid1[i][j] = get_closest_point([i, j])

for i, row in enumerate(grid2):
    for j, element in enumerate(row):
        grid2[i][j] = get_closest_point([i, j])

counter1 = [-1] * len(points)

for row in grid1:
    for element in row:
        if element == -1:
            continue
        counter1[element] += 1

counter2 = [-1] * len(points)

for row in grid2:
    for element in row:
        if element == -1:
            continue
        counter2[element] += 1

print("\n\n")
print(counter1)
print()
print(counter2)

finite_ones = [-1] * len(points)
for i, v in enumerate(counter1):
    if v == counter2[i]:
        finite_ones[i] = v

for i, v in enumerate(grid1):
    for j, v2 in enumerate(v):
        if j == 0 and v2 != -1:
            finite_ones[v2] = -1

print("\n\n")
print(finite_ones)
