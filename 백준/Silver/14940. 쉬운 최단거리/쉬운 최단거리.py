from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n)]
for i in range(n) :
    arr[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 2 :
            oy, ox = i, j
            break

ans = [[0 for i in range(m)] for i in range(n)]
q = deque()
q.append([oy, ox, 0])

while q :
    y, x, level = q.popleft()
    if 0<= y < n and 0<= x < m and ans[y][x] == 0 :
        if arr[y][x] == 0  :
            continue
        else :
            ans[y][x] = level
            q.append([y+1,x,level+1])
            q.append([y-1,x,level+1])
            q.append([y,x+1,level+1])
            q.append([y,x-1,level+1])
            
for i in range(n) :
    for j in range(m) :
        if ans[i][j] == 0 and arr[i][j] > 0 :
            ans[i][j] = -1

ans[oy][ox] = 0

for i in range(n) :
    for j in range(m) :
        sys.stdout.write("%d "%ans[i][j])
    print()