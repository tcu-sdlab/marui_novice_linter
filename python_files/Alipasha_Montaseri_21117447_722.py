formats=int(input())
s=input()
if s=="00:30":
    print(s)
else:
    hour=int(s[0]+s[1])
    hours=s[0]+s[1]
    q=hours
    minute=int(s[3]+s[4])
    minutes=s[3]+s[4]
    if (hour>formats or hour==24) or hour==0:
        hour=int("0"+hours[1])
        hours="0"+hours[1]

    if hours[1]=="0" and hours[0]!="1" and hours[0]!="0":
        hour=9
    hours=str(hour)
    if len(hours)==1:
        hours="0"+hours
    if minute>59:
        minutes="0"+minutes[1]
    if hours=="00" and q[1]=="0":
        hours="10"
    elif hours=="00":
        hours="01"
    print(hours+":"+minutes)