k = 0
for i in range (int(input())) :
    c, d = map(int, input().split())
    k += c > d; k -= c < d
if k > 0 :
    print ("Mishka")
elif k < 0 :
    print ("Chris")
else :
    print ("Friendship is magic!^^")