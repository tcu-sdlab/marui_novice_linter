s=input();l=list(s);up=0;low=0
for i in range(len(s)):
                if s[i].isupper():up=up+1
                else: low=low+1;
print([s.upper(),s.lower()] [low>=up])