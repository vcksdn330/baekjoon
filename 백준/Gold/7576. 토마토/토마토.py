from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
field = [[] for i in range(n)]

for i in range(n) :
    field[i] = list(map(int, sys.stdin.readline().split()))

def bfs(arr, point, m, n) :
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while point :    
        y,x,level = point.popleft()
        for i in range(4) :
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < m and 0<= ty < n :
                if arr[ty][tx] == 0 :
                    arr[ty][tx] = 1
                    point.append([ty,tx,level+1])

    for i in range(n) :
        if 0 in arr[i]:
            return -1
    return level

point = deque()
for y in range(n) :
    for x in range(m) :
        if field[y][x] == 1 :
            point.append([y,x,0])

if len(point) == 0 :
    print(-1)
else :
    print(bfs(field, point, m, n))