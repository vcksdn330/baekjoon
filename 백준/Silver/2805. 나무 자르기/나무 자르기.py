import sys

n, m = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

last = max(arr) 
start = 0

while start <= last :
    trees = 0
    mid = (last + start) // 2
    for i in arr :
        if i > mid :
            trees += (i-mid)

    if trees > m :
        start = mid + 1
    else :
        last = mid - 1

start -= 1
trees = 0
for i in arr :
    if i > start :
        trees += (i-start)

while trees >= m :
    start += 1
    trees = 0
    for i in arr :
        if i > start :
            trees += (i-start)

print(start-1)
