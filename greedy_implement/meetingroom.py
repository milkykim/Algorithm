# # N 입력받기
# n = int(input())

# count = 0

# for i in range(n):
#   mInfo = list(map(int, input().split()))

#   # 처음일때는 무조건 회의실 배정 가능
#   if i==0:
#     count += 1
#     beforeInfoStart = mInfo[0]
#     beforeInfoEnd = mInfo[1]

#   # 더 작은 end 시간이 있을 수 있음.
#   elif mInfo[1] <= beforeInfoStart:
#     count += 1
#     beforeInfoStart = mInfo[0]

#   else:
#     # 시작 시간이 이전의 끝나는 시간보다 크면!
#     if mInfo[0] >= beforeInfoEnd:
#       count += 1
#       beforeInfoStart = mInfo[0]
#       beforeInfoEnd = mInfo[1]

# print(count)

import sys

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, sys.stdin.readline().split())))

meeting = sorted(meeting, key = lambda x: [x[1], x[0]])


#빨리 끝나는 것 중 가장 빨리 시작하는 순서대로 더해준다.
max_meeting = 0
start = 0
for meet in meeting:
    if meet[0] >= start:
        start = meet[1]
        max_meeting += 1
        
print(max_meeting)