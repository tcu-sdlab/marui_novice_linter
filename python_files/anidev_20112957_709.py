#! /usr/bin/env python3

n, b, d = map(int, input().split(' '))
a = map(int, input().split(' '))
e = w = 0

for an in a:
    if an > b:
        continue
    w += an
    if w > d:
        e += 1
        w = 0

print(e)