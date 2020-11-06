import sys

m, n, k = map(int, input().split())

graph = [[0]*n for _ in range(m)]

for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1,y2):
    for j in range(x1,x2):
      graph[i][j]= 1


#print(graph)
count = 0

# dfs로 특정 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y, count):
  if x<=-1 or x>=m or y<=-1 or y>=n:
    return False
  
  if graph[x][y] == 0: #0인 것들의 넓이를 더하자
    # 여기 들어온 친구들은 방문처리해서 각각의 개수를 세는 용도
    # 해당 노드 방문 처리

    #count += 1
    graph[x][y] = 1

    # 해당 덩어리를 재귀호출 하는데, count에 +1을 넣어서 방문처리를 해줌.
    dfs(x-1, y, count+1)
    dfs(x, y-1, count+1)
    dfs(x+1, y, count+1)
    dfs(x, y+1, count+1)

    print(count)
    
    return count
  
  return count

result = []
for i in range(m):
  for j in range(n):
    count = dfs(i, j, count)  #여기서 각기 떨어져있는 것의 개수 3이 나옴
    result.append(count)

print(result)
