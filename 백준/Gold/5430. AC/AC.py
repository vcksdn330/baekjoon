import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T) :
    act = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()
    flag = 0
    bflag = 0

    arr = arr.strip("[""]")
    if len(arr) > 0 :
        arr = list(map(int,arr.split(",")))
    
    num = deque(arr)
    
    for i in act :
        if i == "R" :
            if flag == 0 :
                flag = 1
            else :
                flag = 0
    
        if i == "D" :
            if len(num) == 0 :
                bflag = 1 
                print("error")
                break

            if flag == 1 :
                num.pop()
            else :
                num.popleft()

    num = list(num)

    ans = "["
    cflag = 0
    if bflag == 0 :
        if flag == 1 :
             num.reverse()

        for i in num :
            cflag = 1
            ans += str(i)
            ans += ","

        ans = ans.rstrip(",")
        ans += "]"

        print(ans)