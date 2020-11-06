import sys
from collections import deque

n, m, v= map(int, input().split())

# 정점의 개수만큼 그래프 모양 잡기
graph = [[]*1 for _ in range(n+1)] #[[0],[0],[0],[0],[0]]
graph1 = [[0]*(n+1)] #[[0,0,0,0,0]]

# 간선의 개수 만큼
for i in range(m):
  x, y = list(map(int, input().split()))


print(graph)
print(graph1)

