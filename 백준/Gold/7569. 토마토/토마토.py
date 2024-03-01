import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())
tomatos = [[[] for i in range(n)] for j in range(h)] ##제일 안쪽에 m개의 토마토 들어감

for i in range(h) :
     for j in range(n) :
         tomatos[i][j] = list(map(int, sys.stdin.readline().split()))

ripen = deque()
for i in range(h) :
     for j in range(n) :
          for p in range(m) :
               if tomatos[i][j][p] == 1 :
                    ripen.append([p,j,i,0])

check = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]

while ripen :
    x,y,z,level = ripen.popleft()
    
    if 0<= x < m and 0<= y < n and 0<= z < h and check[z][y][x] == 0:
        check[z][y][x] = 1
        if tomatos[z][y][x] != -1 :
            tomatos[z][y][x] = 1
            ripen.append([x+1,y,z,level+1])
            ripen.append([x-1,y,z,level+1])
            ripen.append([x,y+1,z,level+1])
            ripen.append([x,y-1,z,level+1])
            ripen.append([x,y,z+1,level+1])
            ripen.append([x,y,z-1,level+1])

for i in range(h) :
     for j in range(n) :
          for p in range(m) :
               if tomatos[i][j][p] == 0 :
                    level = 0
                    break
print(level-1)
        