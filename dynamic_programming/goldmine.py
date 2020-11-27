# 테스트 케이스 정보 받기
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][i-1], dp[i+1][j-1])
for t in range(int(input())):
  # 금광 정보
  n, m = map(int,input().split())
  array = list(map(int, input().split()))

  # dp테이블에 금광정보 넣어두기
  dp = []
  index = 0
  for i in range(n):
    # [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]] 이런식으로 추가
    dp.append(array[index: index+m])
    index+=m

  # 0번째 줄부터 할 필요 x -> 그대로의 값을 사용할 것
  for j in range(1,m):
    for i in range(n):
      # i가 0일때는 왼쪽 위가 없음!
      if i==0:
        left_up = 0
      else:
      # i가 0이 아니라면, 왼쪽 위를 대입  
        left_up = dp[i-1][j-1]
      
      # 왼쪽 아래에서 오는 경우
      # i가 n-1 즉, 제일 하단에 있는 경우, 왼쪽 아래가 없음!
      if i == n-1:
        left_down = 0
      else:
        left_down = dp[i+1][j-1]

      # 왼쪽에서 오는 경우
      left = dp[i][j-1]
      dp[i][j] = dp[i][j] + max(left_up, left, left_down)

  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1])
  
  print(result);