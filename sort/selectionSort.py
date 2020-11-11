# 선택정렬 -> O(n2)
# 제일 작은 원소를 만나면 가장 앞으로 보내는 것을 반복


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# i는 가장 앞쪽으로 보내는 원소(제일 작은 원소)
for i in range(len(array)):
  min_index = i #가장 작은 원소의 인덱스
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j

  # 가장 앞쪽 원소와 현재 원소의 자리를 뒤바꿈
  array[i], array[min_index] = array[min_index], array[i] # 스와프: 두 원소의 자리를 바꿀 수 있음

print(array)