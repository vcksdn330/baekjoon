import sys

t = int(input())

for _ in range(t) :
    m,n,x,y = map(int,sys.stdin.readline().split())

    tx = x-m
    flag = 0
    while tx <= m*n :
        tx += m
        ty = tx%n
        if ty == 0 :
            ty += n
     
        if y == ty :
            flag = 1
            print(tx)
            break

    if flag == 0 :
        print(-1)
