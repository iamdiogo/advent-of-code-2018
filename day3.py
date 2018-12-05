
size = 1000

l = [0] * size
L = []
for i in range(0, size):
    L.append(l.copy())

# print(L)

f = open("test.txt", "r")

b = []

for line in f:
    b.append(line.rstrip())

changed = []
n_changed = []

magic = []

for a in b:
    me = int(a.split()[0].replace("#", ""))
    left_space = int(a.split()[2].replace(",", " ").replace(":", "").split()[0])
    top_space = int(a.split()[2].replace(",", " ").replace(":", "").split()[1])
    width = int(a.split()[3].replace("x", " ").split()[0])
    height = int(a.split()[3].replace("x", " ").split()[1])

    print(me)
    my_count = 0
    my_count_tot = 0
    my_count_null = 0
    did_not_overlap = True
    #i = -1
    for i in range(top_space, top_space + height):
        for j in range(left_space, left_space + width):

            #if me not in changed:
            #    changed.append(me)
            #if L[i][j] not in changed:
            #    changed.append(L[i][j])

            if L[i][j] is 0:
                if me not in n_changed:
                    n_changed.append(me)
            else:
                if me not in changed:
                    changed.append(me)
                if L[i][j] not in changed:
                    changed.append(L[i][j])
            L[i][j] = me


    #print(L)

#    for row in L:
#        i += 1
#        #print("i is {}".format(i))
#        #print("top_space is {}".format(top_space))
#        #print("height is {}".format(height))
#        if top_space <= i <= top_space:
#            for n in range(left_space, left_space + width):
#                print(row)
#                print("wow")
#                row[n] = 1
#        print(row)

    #print('\n')
    #print(a)
    #print([left_space, top_space, width, height])

#print(L)

#for r in L:
#    print(r)

f_count = 0
for i in range(0, len(L)):
    for j in range(0, len(L[i])):
        if L[i][j] > 1:
            f_count += 1


wow = []
for element in n_changed:
    print(element)
    if element not in changed:
        wow.append(element)
        continue

print("it isssssssss")
print(f_count)

print("and the list iiisss")
print(wow)
