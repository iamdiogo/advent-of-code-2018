"""
Day 3 solution
"""

size = 1000
l = [0] * size

L = [] # Will hold ids of claims made, in the respective space
L2 = [] # Will hold how many times a the inches have been claimed

# Generate "space" of size size
for i in range(0, size):
    L.append(l[:])
    L2.append(l[:])

f = open("input/day3.txt", "r")

b = []

# Read contents into a list
for line in f:
    b.append(line.rstrip())

n_changed = [] # Will hold ids of all claims made
changed = [] # Will hold ids of claims that have overlapped over another

print("\nCalculating...")

for a in b:
    # The id of the claim
    me = int(a.split()[0].replace("#", ""))

    # The space from the left
    left_space = int(a.split()[2].replace(",", " ").replace(":", "").split()[0])

    # The space from the top
    top_space = int(a.split()[2].replace(",", " ").replace(":", "").split()[1])

    # The width of the claim
    width = int(a.split()[3].replace("x", " ").split()[0])

    # The height of the claim
    height = int(a.split()[3].replace("x", " ").split()[1])

    my_count = 0 # How many
    my_count_tot = 0
    my_count_null = 0
    did_not_overlap = True

    for i in range(top_space, top_space + height):
        for j in range(left_space, left_space + width):

            # Sum 1 into that inch-space, meaning it has been claimed one more time
            L2[i][j] += 1

            if L[i][j] == 0: # If it hasn't been claimed at all
                if me not in n_changed:
                    n_changed.append(me) # Add to claims made
            else:
                if me not in changed:
                    changed.append(me) # Add to claims that overlapped over another
                if L[i][j] not in changed:
                    changed.append(L[i][j]) # Add previous claim of that space as it has been overlapped over
            L[i][j] = me # The space [i][j] was last claimed by the current id


f_count = 0
# Count how may inch-spaces are more than 1 (aka, were overlapped)
for i, value in enumerate(L2):
    for j in range(0, len(L2[i])):
        if L2[i][j] > 1:
            f_count += 1


wow = []
# Find the only id that has never overlapped over other
for element in n_changed:
    if element not in changed:
        wow.append(element)
        break

print("\n Solution #1 is {}".format(f_count))

print("\n Solution #2 is {}\n".format(wow[0]))
