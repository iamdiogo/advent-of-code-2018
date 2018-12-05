"""
Day 5 solution (incomplete)
"""

f = open("input/day5.txt")

polymer = ""
for line in f:
    polymer = line.rstrip().strip()
    break

#print(polymer)

string = polymer
a = string

#for i, v in enumerate(a):
#    if i == len(a) - 1:
#        break
#    print(i)
#    print(" current: {}".format(v))
#    print(" next: {}".format(a[i+1]))
#    print()

#def find_and_remove(string):

#string = a[:]

restart = False
while True:
    for index, value in enumerate(string):
        if index == len(string) - 1:
            print("FINAL IS")
            print(string)
            restart = False
            break

        #print("here")

        if abs(ord(value) - ord(string[index + 1])) == 32:
            #print("Hehe")
            #print(string[:index] + string[index+2:])
            string = string[:index] + string[index+2:]
            restart = True
            break
            print()
    if not restart:
        break



print("it is")
print(string)

print("and it's length is")
print(len(string))
#print(find_and_remove(a))
