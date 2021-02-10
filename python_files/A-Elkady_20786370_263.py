for i in range(5):
          m=input().split()
          if m.count('1'):
                   j=m.index('1')
                   break
print (abs(i-2) + abs(j-2))