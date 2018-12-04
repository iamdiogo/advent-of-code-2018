
size = 1000

l = [0] * size
L = []
for i in range(0, size):
    L.append(l.copy())


f = open("day4.txt", "r")

b = []

for line in f:
    b.append(line.rstrip())

def get_datetime(entry):
    year = int(entry.split()[0].replace("[", "").replace("-", " ").split()[0])
    month = int(entry.split()[0].replace("[", "").replace("-", " ").split()[1])
    day = int(entry.split()[0].replace("[", "").replace("-", " ").split()[2])

    hours = int(entry.split()[1].replace("]", "").replace(":", " ").split()[0])
    minutes = int(entry.split()[1].replace("]", "").replace(":", " ").split()[1])

    if hours < 10:
        hours += 24

    return [year, month, day, [hours, minutes]]

for a in b:
    print(a.split())
    print(get_datetime(a))
