n, m = map(int, input().split())

arr = list(map(int, input().split()))
trueman = set(arr[1:])

parties = [[] for i in range(m)]

for i in range(m) :
    parties[i] = list(map(int, input().split()))

for _ in range(m) :
    for party in parties :
        for i in range(1, party[0]+1) :
            if party[i] in trueman :
                trueman.update(party[1:])
                break

count = 0
for party in parties :
    for i in range(1, party[0]+1) :
        if party[i] in trueman :
            count += 1
            break

print(m - count)