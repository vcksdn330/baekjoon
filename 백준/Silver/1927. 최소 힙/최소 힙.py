import heapq
import sys

heap =[]
n = int(sys.stdin.readline())

for _ in range(n) :
    x = int(sys.stdin.readline())
    if x == 0 and len(heap) > 0 :
        print(heapq.heappop(heap))
    elif x == 0 :
        print(0)
    else :
        heapq.heappush(heap, x)
