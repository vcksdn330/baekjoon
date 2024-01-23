import sys

n, t = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sumarr = [0]
for i in range(n) :
    sumarr.append(sumarr[i] + arr[i])
for _ in range(t) :
    a, b = map(int, sys.stdin.readline().split())

    sys.stdout.write("%d\n"%(sumarr[b] - sumarr[a-1]))