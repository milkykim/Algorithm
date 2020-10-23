import sys
N = int(sys.stdin.readline())

# P는 공백으로 구분해 입력받기
P = list(map(int, input().split()))
P.sort()

time = 0

for idx, item in enumerate(P):
  for j in range(0, idx+1): # 0~idx까지 돌면서 소요시간 합하기
    time += P[j]

print(time)