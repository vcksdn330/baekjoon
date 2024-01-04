import sys

x = int(sys.stdin.readline())
arr = [i-1 for i in range(10**6 + 1)]
for i in range(2, 10**6 + 1) :
    if i%2 == 0 and i%3 == 0 :
        arr[i] = min(arr[i-1], arr[i//2], arr[i//3]) + 1
    elif i%2 == 0 :
        arr[i] = min(arr[i-1], arr[i//2]) + 1
    elif i%3 == 0 :
        arr[i] = min(arr[i-1], arr[i//3]) + 1
    else :
        arr[i] = arr[i-1] + 1

print(arr[x])