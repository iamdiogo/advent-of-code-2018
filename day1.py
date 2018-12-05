
filename = "input.txt"

f = open(filename, "r")

c = 0
l = [0]

found = False

while True:
    f = open(filename, "r")
    for line in f:
        #print(l)
        if line[:1] is "+":
            c += int(line[1:])
            print(c)
            if c in l:
                print(c)
                found = True
                break
            l.append(c)
        else:
            c -= int(line[1:])
            print(c)
            if c in l:
                print(c)
                found = True
                break
            l.append(c)
    f.close()
    if found == True:
        print("found")
        break



print(c)
