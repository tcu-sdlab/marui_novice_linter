n = int(input())
al = list(map(int, input().split()))+[0]
bl = []
# Bi = Ai + Ai+1
for i in range(n):
    bl+=[str(al[i]+al[i+1])]
print(" ".join(bl))