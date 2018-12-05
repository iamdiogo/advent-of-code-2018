"""
Day 4 solution
"""
f = open("input/day4.txt", "r")

# Push contents of input into a list
b = []
for line in f:
    b.append(line.rstrip())
b.sort() # And sort it all

def get_datetime(entry):
    """
    Gets the date, based on a line of input
    """
    year = int(entry.split()[0].replace("[", "").replace("-", " ").split()[0])
    month = int(entry.split()[0].replace("[", "").replace("-", " ").split()[1])
    day = int(entry.split()[0].replace("[", "").replace("-", " ").split()[2])

    hours = int(entry.split()[1].replace("]", "").replace(":", " ").split()[0])
    minutes = int(entry.split()[1].replace("]", "").replace(":", " ").split()[1])

    if hours < 10:
        hours += 24

    return [year, month, day, [hours, minutes]]

current_guard = None # Last guard read
last_falls = None # Datetime of last time falled asleep

sleeps = {} # Holds total minutes a guard has slept
sleeptimes = {} # Holds the times a guard has slept

for a in b:
    # If it's a line containing the guard id
    if len(a.split()) == 6:
        current_guard = int(a.split()[3].replace("#", ""))

    # If this we already read a guard id line
    if current_guard is not None:
        try:
            sleeps[current_guard] # Check if guard key exists
        except KeyError:
            sleeps[current_guard] = 0

        try:
            sleeptimes[current_guard] # Check if guard key exists
        except KeyError:
            sleeptimes[current_guard] = [0 for i in range(60)]

    # If it's a line containing a status update
    if len(a.split()) == 4:
        update = a.split()[2]
        if update == "falls":
            last_falls = get_datetime(a)
        elif update == "wakes":
            wake = get_datetime(a)
            mdiff = wake[3][1] - last_falls[3][1]
            totaldiff = mdiff
            sleeps[current_guard] += totaldiff
            for i in range(last_falls[3][1], wake[3][1]):
                sleeptimes[current_guard][i] += 1
        else:
            raise Exception

counts = []
# Count and push to counts the total minutes
# slept by each guard
for guard in sleeps:
    a = [sleeps[guard], guard]
    counts.append(a)

# Sort from least time slept to most
counts.sort()

# Get guard that has slept more total minutes
guard_chosen = counts[len(counts) - 1][1]

# Get minute that guard_chosen has most slept
time_chosen = sleeptimes[guard_chosen].index(max(sleeptimes[guard_chosen]))

solution = guard_chosen * time_chosen
print("\n Solution #1 is {}".format(solution))

max_time_guard = []
# Push [most_time_spent_sleeping, guard_that_slept_that] into list,
# where list index is the minute from 0 to 59
for n in range(60):
    current_max = [0, 0]
    for guard in sleeptimes:
        if sleeptimes[guard][n] > current_max[0]:
            current_max = [sleeptimes[guard][n], guard]
    max_time_guard.append(current_max)

time_most_slept = max_time_guard.index(max(max_time_guard))
guard_most_slept = max(max_time_guard)[1]

solution = time_most_slept * guard_most_slept
print("\n Solution #2 is {}\n".format(solution))
