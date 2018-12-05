"""
Day 2 solution
"""
import string

filename = "input/day2.txt"

f = open(filename, "r")

b = []
# Read contents into a list
for line in f:
    b.append(line.rstrip())

c = 0
l = [0]

# Create alphabet list
alphabet = list(string.ascii_lowercase)

def count_in_string(char, string):
    """
    Counts how many char in string
    """
    c = 0
    for letter in string:
        if letter is char:
            c += 1
    return c

def compare_strings(s1, s2):
    """
    Compares strings and returns
    a pair with the distance between them and
    a string containing the characters in common
    """
    l = len(s1)
    i1 = -1
    count = 0
    common = ""
    for letter in s1:
        i1 += 1
        if letter == s2[i1]:
            count += 1
            common += letter
    differ_by = l - count
    return [differ_by, common]

list_2 = [] # Strings with exactly 2 of any letter
list_3 = [] # Strings with exactly 3 of any letter

# Iterate and find strings with exactly 2 of any letter
for e in b:
    for letter in alphabet:
        l_count = count_in_string(letter, e)
        if l_count is 2:
            list_2.append(e)
            break

# Iterate and find strings with exactly 3 of any letter
for e in b:
    for letter in alphabet:
        l_count = count_in_string(letter, e.rstrip())
        if l_count is 3:
            list_3.append(e.rstrip())
            break


l2 = len(list_2) # Count of strings with exactly 2 of any letter
l3 = len(list_3) # Count of strings with exactly 3 of any letter

print("\n Solution #1 is {}".format(l2*l3))

sol2 = []
found = False

# Search for a string that has distance 1 to another
# and push to sol2 the common characters
for el in b:
    for e in b:
        r = compare_strings(el, e)
        if r[0] is 1:
            sol2.append(r[1])
            found = True
            break
    if found:
        break


print("\n Solution #2 is {}\n".format(sol2[0]))
