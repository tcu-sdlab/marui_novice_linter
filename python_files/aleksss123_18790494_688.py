import sys, string
#sys.stdin = open("apples.in","r")
#sys.stdout = open("apples.out","w")


n = sys.stdin.readline().strip()

sys.stdout.write(str(n + n[::-1]))


    
#sys.stdin.close()
#sys.stdout.close()