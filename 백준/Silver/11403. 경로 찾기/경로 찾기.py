import sys
n = int(input())
arr = []
for i in range(n) :
    arr.append(list(map(int, sys.stdin.readline().split())))

for _ in range(2) :
    for i in range(n) :
        for j in range(n) :
            for q in range(n) :
                if (arr[i][q] + arr[q][j]) > 1 :
                    arr[i][j] = 1

for i in range(n) :
    for j in range(n) :
        sys.stdout.write("%d "%arr[i][j])
    sys.stdout.write("\n")