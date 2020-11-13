import sys
from collections import Counter

N = int(sys.stdin.readline())

data = []
for _ in range(N):
  data.append(int(sys.stdin.readline()))

data.sort()

# 산술평균 구하기
average = round(sum(data)/N)
print(average)

# 중앙값 구하기
print(data[(N-1)//2])

# 최빈값
# cntTuple -> 가장 많이 나타나는 값 2개 출력
cntTuple = Counter(data).most_common(2)
#print('cnt->',cntTuple)

if len(data) == 1 or len(cntTuple) == 1 or cntTuple[0][1] > cntTuple[1][1]:
  print(cntTuple[0][0])
else:
  print(cntTuple[1][0])

# 범위
print(abs(data[-1] - data[0]))