import sys
n = int(input())
arr = []
arr.extend(list(map(int, sys.stdin.readline().split())))
dp = []
dp.extend(arr)
for i in range(1,n) :
    dp[i] = max(arr[i]+dp[i-1], arr[i])
print(max(dp))