import heapq
import sys

sheap = []
lheap = []
nums = dict()

for _ in range(int(sys.stdin.readline())) :
    for _ in range(int(sys.stdin.readline())) :
        b,n = sys.stdin.readline().split()
        n = int(n)
        if b == 'I' :
            if n in nums :
                nums[n] += 1
                heapq.heappush(sheap, n)
                heapq.heappush(lheap, -n) 
            else :
                nums[n] = 1
                heapq.heappush(sheap, n)
                heapq.heappush(lheap, -n) 


        elif nums :
            if n == -1 :
                while True :
                    x = heapq.heappop(sheap)
                    if x in nums :
                        break

            else :
                while True :
                    x = -heapq.heappop(lheap)
                    if x in nums :
                        break
            
            nums[x] -= 1
            if nums[x] == 0 :
                del nums[x]

    if not nums :
        sys.stdout.write("EMPTY\n")
    else :
        while sheap[0] not in nums  :
            heapq.heappop(sheap)
            
        while -lheap[0] not in nums :
            heapq.heappop(lheap)
            
        sys.stdout.write("%d %d\n"%(-lheap[0], sheap[0]))
    
    sheap.clear()
    lheap.clear()
    nums.clear()