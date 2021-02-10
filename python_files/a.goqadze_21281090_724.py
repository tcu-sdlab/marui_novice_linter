days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day1 = input()
day2 = input()

d1 = days.index(day1)
d2 = days.index(day2)

diff = d2 - d1
if diff < 0:
    diff += 7

ans = "NO"
for month in months:
    if month % 7 == diff:
        ans = "YES"
        break

print(ans)