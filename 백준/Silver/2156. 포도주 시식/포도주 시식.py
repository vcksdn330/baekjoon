import sys
n = int(input())
wine = [0 for i in range(n+1)]
for i in range(1,n+1) :
    wine[i] = int(sys.stdin.readline())
dp = [0 for i in range(n+1)]
dp[1] = wine[1] #dp[i] 에서 i는 i번째 와인을 마실때 최댓값. i가 마지막이라고 가정
if n > 1 :
    dp[2] = wine[1]+wine[2]
if n > 2 :
    dp[3] = max(dp[1]+wine[3], dp[2], wine[2]+wine[3])
    
for i in range(4, n+1) :
    dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1])
    
print(dp[n])