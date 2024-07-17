import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr_count = {}

max_num = 0
left = 0
right = 0

for i in range(n) :
    right = i
    if arr[right] not in arr_count :
        arr_count[arr[right]] = 1
    else :
        arr_count[arr[right]] += 1
    
    while len(arr_count) > 2 :
        arr_count[arr[left]] -= 1
        if arr_count[arr[left]] == 0 :
            del arr_count[arr[left]]
        left += 1
        
    max_num = max(max_num, right - left + 1)
    arr_num = 0
print(max_num)