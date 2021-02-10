a,b,c,d,e,f = map(int, input().split())
if a*e*c< f*d*b or (c == 0 and d) or (a == 0 and b and d):
    print("Ron")
else:
    print("Hermione")