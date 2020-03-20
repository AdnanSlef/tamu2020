#!/usr/bin/env python3
with open('woof.txt','r') as f:
    data = f.read().split()
print(data)
numdata=[]
for x in range(3):
    for y in range(3):
        for z in range(3):
            if x != y and x!=z and y!=z:
                numdata.append(int(''.join(word.replace('woof',str(x)).replace('bark',str(y)).replace('ruff',str(z))for word in data),3))
for num in numdata:
    print(hex(num)[2:])
for num in numdata:
    print(len(bin(num)[2:]))
