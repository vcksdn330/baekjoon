import sys
def zflip(N, lt, x, y) :
    if N == 0 :
        return lt
    
    point = 2**(2*N-2)
    half = 2**(N-1) - 0.5
    rhalf = 2**(N-1)
    if x < half and y < half : #1사분면
        return zflip(N-1, lt, x, y)
    elif x > half and y < half : #2사분면
        return zflip(N-1, lt+point, x-rhalf, y)
    elif x < half and y > half : #3사분면
        return zflip(N-1, lt+(point*2), x, y-rhalf)
    elif x > half and y > half : #4사분면
        return zflip(N-1, lt+(point*3), x-rhalf, y-rhalf)
    else :
        return -1
     
N, r, c = map(int, sys.stdin.readline().split())

print(zflip(N, 0, c, r))