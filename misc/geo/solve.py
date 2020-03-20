#!/usr/bin/env python3
a = '11000010100011000111111111101110'
b = '11000001100101000011101111011111'
y = bin(int(a,2)&int(b,2))[2:]
o = bin(int(a,2)|int(b,2))[2:]
x = bin(int(a,2)^int(b,2))[2:]

todos = [a,b,y,o,x]
nombres = 'abyox'
for i in range(len(todos)):
    print(nombres[i]+': '+todos[i].zfill(len(a))+' '+str(int(todos[i],2)).zfill(10))
