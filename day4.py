
size = 1000

l = [0] * size
L = []
for i in range(0, size):
    L.append(l.copy())


f = open("day4.txt", "r")

b = []

for line in f:
    b.append(line.rstrip())

b.sort()

def get_datetime(entry):
    year = int(entry.split()[0].replace("[", "").replace("-", " ").split()[0])
    month = int(entry.split()[0].replace("[", "").replace("-", " ").split()[1])
    day = int(entry.split()[0].replace("[", "").replace("-", " ").split()[2])

    hours = int(entry.split()[1].replace("]", "").replace(":", " ").split()[0])
    minutes = int(entry.split()[1].replace("]", "").replace(":", " ").split()[1])

    if hours < 10:
        hours += 24

    return [year, month, day, [hours, minutes]]

current_guard = None
last_falls = None

sleeps = {}
sleeptimes = {}

for a in b:
    print(a.split())
    if len(a.split()) is 6:
        current_guard = int(a.split()[3].replace("#", ""))
        print("\n####")
        print(current_guard)
        print("####\n")

    if current_guard is not None:
        try:
            sleeps[current_guard]
        except:
            sleeps[current_guard] = 0

        try:
            sleeptimes[current_guard]
        except:
            sleeptimes[current_guard] = [0 for i in range(60)]

    if len(a.split()) is 4:
        update = a.split()[2]
        print(update)
        if update == "falls":
            last_falls = get_datetime(a)
        elif update == "wakes":
            wake = get_datetime(a)
            hdiff = wake[3][0] - last_falls[3][0]
            mdiff = wake[3][1] - last_falls[3][1]
            print("\n\nIT IS\nhours: {}\nminutes: {}\n\n".format(hdiff, mdiff))
            totaldiff = mdiff + (hdiff*60)
            sleeps[current_guard] += totaldiff
            for n in range(last_falls[3][1], wake[3][1]):
                print(n)
            for i in range(last_falls[3][1], wake[3][1]):
                sleeptimes[current_guard][i] += 1
        else:
            raise Exception

print(sleeps)

counts = []
for guard in sleeps:
    a = [sleeps[guard], guard]
    counts.append(a)

counts.sort()
print()
print(counts[len(counts) - 1])

guard_chosen = counts[len(counts) - 1][1]

time_chosen = sleeptimes[guard_chosen].index(max(sleeptimes[guard_chosen]))

solution = guard_chosen * time_chosen
print(solution)
