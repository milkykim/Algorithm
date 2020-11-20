# 고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
# 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하라

# 이진 탐색 소스코드 구현 (재귀+함수)
def binary_search(array, start, end):
  
  # 데이터가 존재하지 않는다면 None출력
  if start > end:
    return None
  
  mid = (start + end) // 2

  # 찾은 경우 중간점 인덱스 반환
  if array[mid] == mid:
    return mid

  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > mid:
    return binary_search(array, start, mid - 1)

  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, mid + 1, end)

# n(원소의 개수) 입력받기
n = int(input())

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, 0, n - 1)
if result == None:
  print("-1")
else:
  print(result)