n = int(input())
arr = list(map(int, input().split(' ')))
l = []
for i in range(n):
    l.append([i+1, arr[i]])  
l = sorted(l, key=lambda x:x[1])
for i in range(n//2):
    print(str(l[i][0]) + ' ' + str(l[n-i-1][0]))