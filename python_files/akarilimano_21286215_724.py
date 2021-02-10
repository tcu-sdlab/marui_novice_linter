one = input()
two = input()

t = {"monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
 }

if (t[two] - t[one])%7 in [3,2,0]:
    print("YES")
else:
    print("NO")