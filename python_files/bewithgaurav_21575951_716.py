# cook your dish here
s=list(input())
l=len(s)
if l<26:
	print(-1)
else:
	flag=0
	for i in range(l-26+1):
		hash=[0]*26
		st=[]
		c=0
		for j in range(i,i+26):
			if s[j]=='?':
				c+=1
			else:
				hash[ord(s[j])-65]+=1
				st.append(s[j])
		if len(set(st))==26-c:
			flag=1
			t=[]
			for j in range(26):
				if hash[j]==0:
					t.append(chr(65+j))
			for j in range(i,i+26):
				if s[j]=='?':
					s[j]=t.pop()
			break
	if flag==0:
		print(-1)
	else:
		for i in range(l):
			if s[i]=='?':
				s[i]='A'
		print(''.join(s))