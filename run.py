import sys

alpha = {}
alpha['A'] = 10
alpha['A'] = 11
alpha['A'] = 12
alpha['A'] = 13
alpha['A'] = 14
alpha['A'] = 15

input = open('input', "r")
for line in input:
    n = len(line)
    i = 0
    while i < n:
        if line[i] == "\\":
            len = line[i + 1]
            #print len
            char = line[i + 2]
            #print char
            if len in alpha.keys():
                len = alpha(len)
            else:
                len = int(len)
            sys.stdout.write(char * (len + 3))
            i = i + 2
        else:
            sys.stdout.write(line[i])
            i = i + 1
    print