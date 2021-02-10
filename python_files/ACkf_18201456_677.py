if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    n, h, k = map(int, input().split())
    A = list(map(int, input().split()))
    cnt, cur, ans = 0, 0, 0
    while True:
        while cnt < n and cur <= h:
            cur += A[cnt]
            cnt += 1
        if cur > h: 
            cur -= A[cnt - 1]
            cnt -= 1
        
        cur -= min(k, cur)
        ans += 1
        if cnt == n:
            ans += cur // k
            if cur % k != 0:
                ans += 1
            break
        if cnt < n and cur + A[cnt] >= h:
            ans += (cur + A[cnt] - h) // k
            cur -= ((cur + A[cnt] - h) // k) * k
                        
        if cur <= 0 and cnt == n: break

    print(ans)