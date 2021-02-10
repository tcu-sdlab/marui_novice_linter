s=input()
s=s.replace(", " ,"")
s=s.replace("{" ,"")
s=s.replace("}" ,"")
print(len(set(s)))