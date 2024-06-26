import sys
n = int(input())
arr = [0]
arr.extend(list(map(int, sys.stdin.readline().split())))

dp = [1 for i in range(n+1)] # 각 자리가 끝자리 수열이라고 가정

for i in range(2,n+1) :
    for j in range(1,i) :
        if arr[i] > arr[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))