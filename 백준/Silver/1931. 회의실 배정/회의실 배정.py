import sys

T = int(sys.stdin.readline())
sched = list()

for i in range(T):
    S, E = map(int, sys.stdin.readline().split())
    sched.append((S, E))

sched = sorted(sched, key=lambda x: (-x[0], -x[1]))

count = 0
for i in sched:
    if count == 0 or i[1] <= startTime:
        count += 1
        startTime = i[0]

print(count)