import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n) :
    arr.append(list(map(int, sys.stdin.readline().split())))

# 테트로미노 모양을 미리 정의
tetrominoes = [
    # 일자 모양
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # 정사각형 모양
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # ㄴ 모양
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, -1), (1, -2)],
    # ㄹ 모양
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    # ㅗ 모양
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (1, -1)],
    [(0, 0), (0, 1), (-1, 1), (1, 1)]
]

max_sum = 0

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(n):
    for j in range(m):
        for tetromino in tetrominoes:
            total = 0
            for dx, dy in tetromino:
                ni, nj = i + dx, j + dy
                if is_valid(ni, nj):
                    total += arr[ni][nj]
                else:
                    break
            else:
                max_sum = max(max_sum, total)

print(max_sum)
