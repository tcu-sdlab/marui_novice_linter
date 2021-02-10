import decimal
N=input()
s = str(N)
s = s.split('e')
pw = int(s[1])
fl = s[0]
fl = fl.split('.')
f1 = fl[0]
f2 = fl[1]
ans = f1+f2
pw = pw-len(f2)
if(pw>=0):
    ans = ans + '0'*pw
else:
    if(len(ans)>pw):
        ans = ans[:pw]+'.'+ans[pw:]
    else:
        ans = '0.'+'0'*(pw-len(ans))+ans
print(ans.rstrip('0').rstrip('.') if '.' in ans else ans)