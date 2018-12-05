import string

filename = "input.txt"

f = open(filename, "r")

c = 0
l = [0]

alphabet = list(string.ascii_lowercase)

def count_in_string(char, string):
    c = 0
    for letter in string:
        if letter is char:
            c += 1
    return c

list_2 = []
list_3 = []

for e in f:
    for letter in alphabet:
        l_count = count_in_string(letter, e.rstrip())
        if l_count is 2:
            list_2.append(e.rstrip())
            break

f.close()

f = open(filename, "r")
for e in f:
    for letter in alphabet:
        l_count = count_in_string(letter, e.rstrip())
        if l_count is 3:
            list_3.append(e.rstrip())
            break


print(list_2)
print(list_3)

l2 = len(list_2)
l3 = len(list_3)

print(l2*l3)
l2 = len(list_2)
