import sys

N, M = map(int,sys.stdin.readline().split())
graph = [[0 for i in range(N+1)] for i in range(N+1)]
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, N+1) :
    for j in range(1, N+1) :
         if i == j : graph[i][j] = 0
         elif graph[i][j] == 0 : graph[i][j] = 99999


for k in range(1,N+1) :
    for i in range(1,N+1) :
        for j in range(1,N+1) :
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

x = 999999
ans = 0

for i in range(1,N+1) :
    y = sum(graph[i][1:])
    if x > y :
        x = y
        ans = i
print(ans)