from sys import stdout

primes = [2, 4, 3, 9, 5, 25, 7, 49, 11,13,17,19,23,29,31,37,41,43,47]
cnt = 0

for i in primes:
    print(i)
    stdout.flush()
    if input() == "yes":
        cnt += 1
        
if cnt < 2:
    print("prime")
else:
    print("composite")