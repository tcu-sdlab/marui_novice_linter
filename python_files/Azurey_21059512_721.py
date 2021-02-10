row = int(input())
encrypt = input()

consecutive = []
groups = 0
cons = 0
i = 0
while i < row:
    while encrypt[i] == 'B':
        i += 1
        cons += 1
        if i == row:
            break
    else:
        i += 1
    if cons > 0:
        groups += 1
    if cons != 0:
        consecutive.append(str(cons))
    cons = 0
    
print(groups)
if groups != 0:
    print(" ".join(consecutive))