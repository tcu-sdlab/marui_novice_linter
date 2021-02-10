from sys import setrecursionlimit
import re
setrecursionlimit(1000000000)
from math import sqrt


def main():
    str=input()
    place=0;
    if(str[-1]=='a'):
        place=4;
    if(str[-1]=='b'):
        place=5;
    if(str[-1]=='c'):
        place=6;
    if(str[-1]=='d'):
        place=3;
    if(str[-1]=='e'):
        place=2;
    if(str[-1]=='f'):
        place=1;
    way = int(str[:-1])
    print(((way-1)//4)*16+(1-way%2)*7+place)


main()

#      ^R\d*C\d*$