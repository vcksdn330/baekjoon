import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n)]
for i in range(n) :
    arr[i] = list(sys.stdin.readline().rstrip())

mx,my = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 'I' :
            mx = i
            my = j
            break

def numCheck(x,y) :
    return (x<n and x>=0) and (y<m and y>=0)

queue = deque([])
queue.append([mx,my])

p = 0
while queue :
    x, y = queue.popleft()
    if numCheck(x,y):
        if arr[x][y] != 'X' :
            for i in range(4) :
                queue.append([x+dx[i],y+dy[i]])
            
            if arr[x][y] == 'P' :
                p += 1
            
            arr[x][y] = 'X'

if p == 0 :
    print("TT")
else :
    print(p)