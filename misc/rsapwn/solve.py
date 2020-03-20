#!/usr/bin/env python3
from pwn import *
from factordb.factordb import FactorDB

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

conn = remote('challenges.tamuctf.com',8573)

print(conn.recv())
conn.sendline()

x = int(conn.recv())
print(x)
f = FactorDB(x)
f.connect()
m = ' '.join(str(i)for i in f.get_factor_list())
print(m)
conn.sendline(m)


conn.interactive()
conn.close()
