import sys
#sys.stdin = open("apples.in","r")
#sys.stdout = open("apples.out","w")

n, x = list(map(int, sys.stdin.readline().split()))
s = []
ice = x
sad = 0
for i in range(n):
    s = input().split()
    if (s[0] == "+"):
        ice += int(s[1])
    else:
        if (ice >= int(s[1])):
            ice -= int(s[1])
        else:
            sad += 1
print(ice, sad)

        
#sys.stdin.close()
#sys.stdout.close()