#!/usr/bin/env python3
n = int(input())
print("YES" if sum(map(int, input().split())) == n - (n != 1) else "NO")