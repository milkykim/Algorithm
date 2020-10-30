import sys

n, m = map(int , sys.stdin.readline())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# dfs로 특정 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return false

    queue = deque([start])
    visited[start] = True
  
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    graph[x][y] = 1

    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  
  return false

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1



print(result)
