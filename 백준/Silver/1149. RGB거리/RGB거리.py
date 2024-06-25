import sys
n = int(sys.stdin.readline())
house = [[0,0,0]]
for _ in range(n) :
    house.append(list(map(int, sys.stdin.readline().split())))

dp = [[0,0,0] for i in range(n+1)]
dp[2] = [min(house[1][1]+house[2][0], house[1][2]+house[2][0]),
        min(house[1][0]+house[2][1], house[1][2]+house[2][1]),
        min(house[1][0]+house[2][2], house[1][1]+house[2][2])]

for i in range(3,n+1) :
    dp[i] = [min(dp[i-1][1] + house[i][0], dp[i-1][2] + house[i][0]),
            min(dp[i-1][0] + house[i][1], dp[i-1][2] + house[i][1]),
            min(dp[i-1][0] + house[i][2], dp[i-1][1] + house[i][2])]

print(min(dp[n]))