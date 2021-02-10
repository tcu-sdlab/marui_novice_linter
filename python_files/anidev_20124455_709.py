#! /usr/bin/env python3

s = t = list(input())

total = 0
started = False
for i, c in enumerate(s):
    if c == 'a':
        if started:
            break
        else:
            continue
    else:
        started = True
        t[i] = chr(ord(c) - 1)
        total += 1

if total == 0:
    t[-1] = 'z'

print(''.join(t))