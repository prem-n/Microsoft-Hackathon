__author__ = 'Charu'
import operator

import os, json, sys
import operator
import math
name=[]
likes={}
dislike={}
paired=[-1 for x in range(0,100)]
def get_mat(fname):

    file = open(fname,"r")
    i=0
    prev=""
    for line in file:
        line = line.strip()
        if i%3==0:
            name.append(line)
            prev=line
        elif i%3==1:
            a=line.split(' ')
            likes[prev]=a

        elif i%3==2:
            a=line.split(' ')
            dislike[prev]=a
        i+=1

    for i in range(0,len(name)):
        for j in range(0,len(name)):
            if paired[j]==-1:
                a=set(dislike[name[i]]).intersection(likes[name[j]])
                b=set(dislike[name[j]]).intersection(likes[name[i]])
                if len(a)==0 and len(b)==0:
                    paired[j]=i
                    paired[i]=j
       
    res={}           
    for x in range(0,len(name)):
        if paired[x]!=-1:
            res[x]=name[x]+" "+name[paired[x]]
            
    sorted_x = sorted(res.items(), key=operator.itemgetter(1))
    for x in range(len(sorted_x)):
        print sorted_x[x][1]
            
              

get_mat("1.txt")# your code goes