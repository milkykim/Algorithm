# 퀵정렬 -> O(nlogn)
# 가운데 안테나를 설치하는 것이 무조건 최소가 된다는 점을 이용!

import sys
N = int(sys.stdin.readline())

array = list(map(int,input().split()))

def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  pivot = array[0] # 피벗은 첫 번째 원소
  tail = array[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분할된 오른 부분

  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)
  
quick = quick_sort(array)
print(quick[(N-1)//2])