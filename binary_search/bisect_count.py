# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

# 데이터 개수 N, 찾고자하는 값 x 입력
n, x = map(int, input().split())

# 정렬되어있는 전체 데이터 입력받기
array = list(map(int, input().split()))

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
	right_index = bisect_right(a, right_value)
	left_index = bisect_left(a, left_value)
	return right_index - left_index

count = count_by_range(array, x, x)

if count == 0:
  print(-1)
else:
  print(count)