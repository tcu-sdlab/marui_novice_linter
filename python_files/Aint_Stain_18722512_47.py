import math
a=int(input())
b=int(math.sqrt(1+(8*a)))
if b*b!=(1+(8*a)):
    print("NO")
else:
    print("YES")