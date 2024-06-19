import heapq
import sys

n = int(input())
heap = []
for i in range(n) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if heap :
            sys.stdout.write("%d\n"%(-heapq.heappop(heap)))
        else :
            sys.stdout.write("0\n")
    else :
        heapq.heappush(heap, -x)