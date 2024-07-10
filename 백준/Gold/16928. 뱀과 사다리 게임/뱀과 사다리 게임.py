import sys
from collections import deque
inf = 99999999
field = [inf for i in range(101)]
n, m = map(int, sys.stdin.readline().split())

ladder = [0 for i in range(101)] 
snake = [0 for i in range(101)]

for i in range(n) :
    a,b = map(int, sys.stdin.readline().split())
    ladder[a] = b

for i in range(m) :
    a,b = map(int, sys.stdin.readline().split())
    snake[a] = b

dq = deque([])
dq.append((1,0))
while dq :
    x, level = dq.popleft()

    if x <= 100 :
        if field[x] > level :
            field[x] = level
            if snake[x] > 0 :
                dq.append((snake[x], level))
            elif ladder[x] > 0 :
                dq.append((ladder[x], level))
            else :
                dq.append((x+1, level+1))
                dq.append((x+2, level+1))
                dq.append((x+3, level+1))
                dq.append((x+4, level+1))
                dq.append((x+5, level+1))
                dq.append((x+6, level+1))

print(field[100])