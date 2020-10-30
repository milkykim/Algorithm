import sys
from collections import deque

n, m = map(int , sys.stdin.readline())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]

#1과 연결된 모든 노드 뽑기
def bfs(x,y):
  queue = deque()
  queue.append((x,y));

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue;

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  return graph[n-1][m-1]

#1을 제외한 감염된 노드 수 출력
print(bfs(0,0))
