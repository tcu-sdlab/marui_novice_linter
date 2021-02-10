s='0abcdefghijklmnopqrstuvwxyz'
n=input()
sm=0
u='a'
for i in range(len(n)):
    sm+=min(abs(s.index(u)-s.index(n[i])),26-abs(s.index(u)-s.index(n[i])))
    u=n[i]
print(sm)