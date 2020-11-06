import sys
from collections import deque

n, m, v= map(int, input().split())

# 정점의 개수만큼 그래프 모양 잡기
graph = [[] for _ in range(n+1)]

# 간선의 개수 만큼
for i in range(m):
  x, y = list(map(int, input().split()))
  # 해당 위치에 연결된 점의 값을 집어넣음
  graph[x].append(y)
  graph[x].sort()
  graph[y].append(x)
  graph[y].sort()


def dfs(graph, v, visited):
  # 현재 노드를 방문처리
  visited[v] = True
  print(v, end=' ')
  
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  # 큐 생성
  q = deque([start])
  # 현재 노드 방문처리
  visited[start] = True
  
  #큐가 빌때까지 반복
  while q:
    v = q.popleft()
    print(v, end=' ')
    #해당 원소와 연결되고, 아직 방문하지 않은 원소들 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

# 각 노드가 방문한 정보를 리스트로 표현
visited = [False]*(n+1)

# dfs함수 호출
dfs(graph, v, visited)


# 각 노드가 방문한 정보를 리스트로 표현
visited = [False]*(n+1)

print()

# bfs함수 호출
bfs(graph, v, visited)