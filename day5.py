"""
Day 5 solution (unoptimized)
"""
import string as awesome

f = open("input/day5.txt")

string = ""
for line in f:
    string = line.rstrip().strip()
    break

def get_length_polymer(polymer):
    restart = False
    while True:
        for index, value in enumerate(polymer):
            if index == len(polymer) - 1:
                restart = False
                break
            if abs(ord(value) - ord(polymer[index + 1])) == 32:
                #polymer = polymer[:index] + polymer[index+2:]
                del polymer[index]
                del polymer[index]
                restart = True
                break
        if not restart:
            break
    return len(polymer)

print("it's length is")
print(get_length_polymer(list(string)))

#exit(0)
# Create alphabet list
alpha_lower = list(awesome.ascii_lowercase)
alpha_upper = list(awesome.ascii_uppercase)

final_length = []

for i in range(26):
    print(" calculating for {}".format(alpha_lower[i]))
    temp = string.replace(alpha_lower[i], "").replace(alpha_upper[i], "")
    c = get_length_polymer(list(temp))
    final_length.append(c)

for e in range(26):
    print("{} is {}".format(alpha_lower[e], final_length[e]))
