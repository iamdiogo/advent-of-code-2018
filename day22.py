import string

filename = "input.txt"

f = open(filename, "r")

c = 0
l = [0]

alphabet = list(string.ascii_lowercase)

def compare_strings(s1, s2):
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

gl = []
for line in f:
    gl.append(line.rstrip())

for el in gl:
    for e in gl:
        r = compare_strings(el, e)
        if r[0] is 1:
            print(r)
