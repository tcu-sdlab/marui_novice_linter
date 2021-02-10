d,h,v,e = map(int, input().split())
s = 3.14159265354/4*d*d 
if s*e-v >= 0.0:
    print("NO")
else:
    print("YES")
    print(h/(v/s-e))