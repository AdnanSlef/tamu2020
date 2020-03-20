#!/usr/bin/env python3

part1 = '103208311412521644754805923974'
part2 = '10881183128414021520157116851780189419421991209921942315241625302578269728072902300131153236334834643575368637343782389340044129'

a = [int(part1[i:i+3])for i in range(0,len(part1),3)]
b = [int(part2[i:i+4])for i in range(0,len(part2),4)]

def flag(lst):
    return ''.join([chr(lst[0])]+[chr(lst[i]-lst[i-1]) for i in range(1,len(lst))])

print(flag(a+b))
