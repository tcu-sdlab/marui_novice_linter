def year(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        return 2
    
    return 1


now = int(input())
s = now
balance = 0


while balance % 7 != 0 or balance == 0 or year(now) != year(s):
    now += 1
    balance += year(now)
    
print(now)