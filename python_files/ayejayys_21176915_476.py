s1 = input().strip()
s2 = input().strip()
l1 = [0]*2
l2 = [0]*3
f = [1]*11
f[0] = 1
for x in range(1, 11):
    f[x] = f[x-1]*x

for x in s1:
    if x == '+':
        l1[0] += 1
    else:
        l1[1] +=1

for x in s2:
    if x == '+':
        l2[0] += 1
    elif x == '-':
        l2[1] +=1
    else:
        l2[2] +=1

reqp = l1[0] - l2[0]
reqn = l1[1] - l2[1]
if reqp > l2[2] or reqn > l2[2]:
    prob = 0
else:
    prob = (f[l2[2]]//f[reqp]//f[reqn])/pow(2, l2[2])
print("%.12f" % (prob))