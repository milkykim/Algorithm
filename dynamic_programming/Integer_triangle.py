# 왼쪽 위/ 바로 위
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])
n = int(input())

# dp테이블에 정보 넣어두기
dp = []

for _ in range(n):
  # [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]] 이런식으로 추가
  dp.append(list(map(int, input().split())))

# 0번째 줄부터 할 필요 x -> 그대로의 값을 사용할 것
# 두번째 줄부터 내려가면서 확인
for i in range(1,n):
  for j in range(i+1):
    # i가 0일때는 왼쪽 위가 없음!
    # 왼쪽 위에서 내려올 때
    if j==0:
      up_left = 0
    else:
    # i가 0이 아니라면, 왼쪽 위를 대입  
      up_left = dp[i-1][j-1]
      
    # 왼쪽 아래에서 오는 경우
    # i가 n-1 즉, 제일 하단에 있는 경우, 왼쪽 아래가 없음!
    if j == i:
      up = 0
    else:
      up = dp[i-1][j]

    # 왼쪽에서 오는 경우
    dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]));