n,k = map(int,input().split())

arr=[0]*100001
queue=[n]
while queue:
    tmp = queue.pop(0)
 
    if tmp==k : break

    for i in[tmp-1, tmp+1, tmp*2]:
    
        if 0 <= i < 100001 and arr[i] < 1 :
            arr[i] = arr[tmp] + 1
            queue.append(i)

print(arr[k])