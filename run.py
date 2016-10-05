import sys

alpha = {}
alpha['A'] = 10
alpha['B'] = 11
alpha['C'] = 12
alpha['D'] = 13
alpha['E'] = 14
alpha['F'] = 15

input = open('input', "r")
for line in input:
    line = line.strip()
    #print line
    if "\\\\" in line:
        print "CORRUPTED"
        continue
    else:
        n = len(line)
        i = 0
        c_res = ""
        while i < n:
            if line[i] == "\\":
                c_len = line[i + 1]
                char = line[i + 2]
                if char == "\\":
                    c_res = "CORRUPTED"
                    break
                if c_len in alpha.keys():
                    c_len = alpha[c_len]
                elif c_len.isdigit():
                    c_len = int(c_len)
                else:
                    c_res = "CORRUPTED"
                    break
                c_res += char * (c_len + 2)
                i = i + 2
            else:
                c_res += line [i]
                i = i + 1
        print c_res