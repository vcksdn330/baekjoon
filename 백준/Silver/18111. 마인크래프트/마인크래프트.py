import sys

N,M,B = map(int, sys.stdin.readline().split())
arr = [0 for i in range(N)]
ery = 0
for i in range(N) :
    arr[i] = list(map(int, sys.stdin.readline().split()))
    ery += sum(arr[i])
minee = 2147483647
level = 0
for i in range(257) : #목표레벨 i
    t = 0
    if ery + B >= i*N*M :
        for q in range(N) : 
            for p in range(M) :
                dist = arr[q][p] - i
                if dist < 0 : t += dist*(-1)
                else : t += dist*2
        if minee >= t : 
            minee = t
            level = i

print("%d %d"%(minee, level))