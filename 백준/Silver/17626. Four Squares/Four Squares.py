import math
n = int(input())

dp = [99 for i in range(n+1)]
dp[0] = 0
for i in range(1,n+1) :
    j = int(math.sqrt(i))
    while (dp[i] != 1) and (j != 0) :
        dp[i] = min(dp[i], dp[i-(j*j)]+1)
        j -= 1
print(dp[n])