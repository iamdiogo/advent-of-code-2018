"""
Day 1 solution

Note: It's slow, needs some optimizing
"""
filename = "input/day1.txt"

f = open(filename, "r")

b = []

# Read contents into a list
for line in f:
    b.append(line.rstrip())

c = 0
l = [0]

# Initially not found
found = False

while True:
    for line in b:
        if line[:1] is "+":
            c += int(line[1:])
            print(c)
            if c in l: # If found a repetition
                print(c)
                found = True
                break
            l.append(c)
        else:
            c -= int(line[1:])
            print(c)
            if c in l: # If found a repetition
                print(c)
                found = True
                break
            l.append(c)
    if found == True:
        print("\n Solution found!\n")
        break

print(c)
