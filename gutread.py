#!/usr/bin/python3
import string
import time
import sys
import os
__author__ = 'joseph'
file=input("ENTER THE NAME OF THE FILE: ")
#timey=time.time()
path="."
#path="/home/joseph/Downloads/Text Parser Files/"
file=path+file
g=open(file,mode='r',buffering=32768, encoding='utf-8')
d=dict()
start=False
fd=g.fileno()
f=(os.read(fd, 1048576*25)).decode("utf-8")
g.close()

for line in f.split("\n"):
    if "*** END OF THIS" in line:
        break
    elif start:
        line=line.lower()
        line=line.replace("-"," ")
        for word in line.split(" "):
            word=word.strip("!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~\n \t")
            if word=="" or word[0].isdigit():
                 continue
            if word[-2:]=="'s":
                d[word]=d.get(word[:-2],0)+1
            else:
                d[word]=d.get(word,0)+1
    elif "*** START OF THIS" in line:
        start=True
#print(time.time()-timey)
sortedDict=sorted(d.items(), key= lambda x: "%i\u00000000%s"%(sys.maxsize-x[1], x[0]))[:20]
print("# of unique words: %i"%len(d))
print("# of words: %i"%sum(d.values()))
top=[]
for item in range(0,20):
    top.append("%i most commonly used word: %s-%i"%(item+1,sortedDict[item][0],sortedDict[item][1]))
print("\n".join(top))
#print(time.time()-timey)
df=open(path+"/wordlist.txt", mode="r", encoding="utf-8")
for line in df:
    line=line[:-1]
    if line in d:
        del d[line]
notIn=sorted(d.keys())
print("\n".join(notIn))
#print(time.time()-timey)