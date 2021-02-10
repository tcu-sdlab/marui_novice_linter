c=0
for i in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,4,9,25,49]:
    print(i)
    c += input()=="yes"
print("composite" if c > 1 else "prime")