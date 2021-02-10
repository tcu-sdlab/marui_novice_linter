# coding=utf-8
__author__ = 'Alexander'

# s = input()
#
# k = 0 #len(s)
# last = 0

# for i, c in enumerate(s):
#     if c in ['A', 'E', 'I', 'O', 'U', 'Y']:
#         #print(i, c, k)
#         if i-last > k:
#             k = i - last
#         last = i
#
# if last == 0:
#     k = len(s)
#
# print(k)

s = input()

k = 0 #len(s)
last = 0
p = [0]

for i, c in enumerate(s):
    if c in ['A', 'E', 'I', 'O', 'U', 'Y']:
        p.append(i+1)

p.append(len(s)+1)

i = 0
n = len(p)
while i < n-1:
    d = p[i+1] - p[i]
    if d > k:
        k = d
    i += 1

print(k)