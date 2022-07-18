#!/usr/bin/env python

sumi = 0
i = 32

def f(x):
    if x == 0:
        return 0
    else:
        return int(2 ** (6 + f(x - 1)))

def calculate():
    global i, sumi
    while i > 0:
        sumi = sumi + f(i)
        i = i - 1
    return sumi

with open('dragon-duplication-glitch-magic.txt', 'w') as f:
    f.write(str(calculate()))
    f.close()