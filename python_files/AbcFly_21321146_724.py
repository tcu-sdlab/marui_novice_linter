il=[4,7,7,3,5,1,3,6,2,4,7,2]
id = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
a,b = id.get(input()),id.get(input())
ans = False
for i in range(11):
    if il[i]-a == il[i+1]-b:
        ans = True
        break
print(["NO","YES"][ans])