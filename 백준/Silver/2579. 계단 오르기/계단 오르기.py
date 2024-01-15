import sys
input = sys.stdin.readline
N = int(input())
stair = [0] #시작지점
for _ in range(N): stair.append(int(input()))  #1번부터 N번계단까지

D = [[0] * 3 for _ in range(N+1)] #[계단번호][계단스택] N번까지
for i in range(1,N+1):
    D[i][1] = D[i-1][0]+stair[i] #밟은 첫번째 계단
    D[i][2] = D[i-1][1]+stair[i] #밟은 두번째 계단
    D[i][0] = max(D[i-1][1:]) #건너뛰었을 경우
    
print(max(D[-1][1:]))

#메모이제이션으로 모든 경우의 수를 저장하고 실행.