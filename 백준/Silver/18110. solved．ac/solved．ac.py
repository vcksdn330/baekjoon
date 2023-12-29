import math
import sys

n = int(input())
arr = []
if n == 0 : print(0)
else :
    for _ in range(n) :
        arr.append(int(sys.stdin.readline()))

    arr.sort()
    p = round(n*15/100 + 0.000001)

    total = 0
    for i in range(p,n-p) :
        total += arr[i]
    result = total/(n-p-p)

    if result - int(result) >= 0.5 :
        result = int(result) + 1
    else :
        result = int(result)
    print(result)