color = ['C','M','Y']
n,m=[int(i) for i in input().split()]
for i in range(n):
    l=input()
    for c in color:
        if c in l:
            print('#Color')
            exit()
print('#Black&White')