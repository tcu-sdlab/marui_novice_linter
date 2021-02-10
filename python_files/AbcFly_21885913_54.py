N,K = map(int, input().split());
dl, d, index, ans = list(map(int, input().split()))+[N+1], 0, 1, -1;

while(d<=N):
    ans+=1;
    if dl[index]<=d+K:
        d=dl[index];
        index+=1;
    else:
        d+=K;
print(ans)