d = {
 "monday":0,
 "tuesday":1,
 "wednesday":2,
 "thursday":3,
 "friday":4,
 "saturday":5,
 "sunday":6
}
d1 = d[input()] 
d2 = d[input()] 
if (28-d2+d1) % 7 == 0 or (30-d2+d1) % 7 == 0 or (31-d2+d1) % 7 == 0:
  print("YES")
else:
  print("NO")