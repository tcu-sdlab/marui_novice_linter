n = int(input())
data = [input() for i in range(n)]
found = False
for i in range(n):
  if data[i][0:2] == "OO":
    data[i] = "++" + data[i][2:]
    found = True
    break
  if data[i][3:5] == "OO":
    data[i] = data[i][:3] + "++"
    found = True
    break

if found:
  print("YES")
  for s in data:
    print(s)
else:
  print("NO")