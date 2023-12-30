import sys
import math

def cal(N,a,b,c,d,e,f) :
    tmp = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
    t = abs(N-tmp) + len(str(tmp))
    return t

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
pad = [i for i in range(10)]
if M > 0 :
    arr = list(map(int, sys.stdin.readline().split()))
    for i in arr :
        pad.remove(i)

channel = 100
T = abs(N-channel) #+ or -로만 이동. 최대시간
line = len(str(N))
for a in pad :
    for b in pad :
        for c in pad :
            for d in pad :
                for e in pad :
                    for f in pad :
                        t = cal(N,a,b,c,d,e,f)
                        if T > t : T = t
                        t = cal(N,0,b,c,d,e,f)
                        if T > t : T = t
                        t = cal(N,0,0,c,d,e,f)
                        if T > t : T = t
                        t = cal(N,0,0,0,d,e,f)
                        if T > t : T = t
                        t = cal(N,0,0,0,0,e,f)
                        if T > t : T = t
                        t = cal(N,0,0,0,0,0,f)
                        if T > t : T = t

print(T)