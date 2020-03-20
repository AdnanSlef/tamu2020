#!/usr/bin/env python3
from pwn import *

answers = []


conn = remote('challenges.tamuctf.com',7393)
print(conn.recv())

answers = [True]*20
for n in range(1048576):
    a = [int(k)for k in list(bin(n)[2:].zfill(20))]
    conn.sendline('2')
    for i in range(20):
        print(conn.recv())
        conn.sendline('Yes' if a[i]else 'No')
    res = conn.recv()
    if b'not who you' in res:
        print('fail')
    else:
        print(res)
        print(answers)
        break

#conn.interactive()
conn.close()
