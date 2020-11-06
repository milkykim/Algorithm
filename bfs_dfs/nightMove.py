from collections import deque

# 갈 수 있는 좌표의 수
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]


def bfs(sx, sy, ex, ey):
  queue = deque()
  # 시작점 세팅
  queue.append((sx, sy))
  # 방문처리
  graph[sx][sy] = 1

  while queue:
    # 좌표를 하나씩 빼면서
    x, y = queue.popleft()

    # 목표 좌표값과 동일하면 -> 현재 나의 좌표값에 횟수가 누적되어 있음
    if x==ex and y==ey:
      print(graph[x][y]-1)
      return

    # 좌표의 경우의 수 8개
    for i in range(8):
      # 현재 위치에서 이동
      nx = x + dx[i]
      ny = y + dy[i]
      
      # 방문하지 않았거나 범위 안에 있다면
      if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
        queue.append((nx, ny))
        # 새로운 위치에 현재좌표까지 쌓인 횟수 + 1
        graph[nx][ny] = graph[x][y]+1


#입력받은 개수 만큼 테스트케이스
n = int(input())

for i in range(n):
  #체스판의 크기, 시작점과 이동점을 입력받음
  l = int(input())
  sx, sy = map(int, input().split())
  ex, ey = map(int, input().split())

  # l만큼의 체스판 생성
  graph = [[0]*l for _ in range(l)]
  bfs(sx, sy, ex, ey)



