from collections import deque

# 갈 수 있는 좌표의 수
dx = [-2,-2,0,0,+2,+2]
dy = [-1,+1,-2,+2,-1,+1]


def bfs(sx, sy, ex, ey):
  q = deque()
  # 시작점 세팅
  q.append((sx, sy))

  # 방문처리
  graph[sx][sy] = 1
  
  #큐가 빌때까지 반복
  while q:
    x, y = q.popleft()

    if x == ex and y == ey:
        print(graph[x][y]-1)
        return
    
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
        q.append((nx, ny))
        # 새로운 위치에 현재좌표까지 쌓인 횟수 + 1
        graph[nx][ny] = graph[x][y]+1

  print("-1")
  return


#체스판의 크기, 시작점과 이동점을 입력받음
l = int(input())
sx, sy, ex, ey = map(int, input().split())

# l만큼의 체스판 생성
graph = [[0]*l for _ in range(l)]
bfs(sx, sy, ex, ey)