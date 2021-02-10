def main():
    str1=str(input())
    str2=str(input())
    str3=''.join(sorted(str1))
    for i in range(len(str3)):
        if (str3[i]!='0' and str3[0]=='0'):
            str3=swap(str3,i,0)
            break;
    if(str3==str2):
        print("OK")
    else:
        print("WRONG_ANSWER")
   # print(str3)   
def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c) 
main()