# 삽입정렬 -> O(n2)
# 자신의 위치 이전까지 비교하며 작으면 자리를 바꾸는 것을 반복해 제일 앞쪽으로 가게 됨

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
    if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]
    else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break

print(array)