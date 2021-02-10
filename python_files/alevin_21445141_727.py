def pereob(ch1, ch2, ar):
    if ch1 == ch2:
        global con
        con = 1
        global pop
        pop = ar + []
    elif ch1 < ch2:
        ar1 = ar + [2 * ch1]
        pereob(2 * ch1, ch2, ar1)
        ar2 = ar + [ch1 * 10 + 1]
        pereob(ch1 * 10 + 1, ch2, ar2)

a, b = map(int, input().strip().split())
pop = [a]
con = 0
pereob(a, b, pop)
if con == 1:
    print("YES")
    print(len(pop))
    for i in pop:
        print(i, end=' ')
else:
    print("NO")