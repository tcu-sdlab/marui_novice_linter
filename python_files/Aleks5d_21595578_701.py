def key(a):
    return a[0]

def main():
    count = int(input())
    card=list()
    r=input().split()
    for i in range(count):
        card.append([int(r[i]), i+1])
    card.sort(key=key)
    for i in range(count//2):
        print(str(card[i][1])+' '+str(card[-1*i-1][1]))

main()