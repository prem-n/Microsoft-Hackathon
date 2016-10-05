import sys

input = open('input', "r")
for line in input:
    n = len(line)
    i = 0
    while i < n:
        if line[i] == "\\":
            len = line[i + 1]
            print len
            char = line[i + 2]
            print char
            sys.stdout.write(char * (int(len) + 3))
        else:
            sys.stdout.write(line[i])
        i = i + 2
    print