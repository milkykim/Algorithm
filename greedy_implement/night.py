# N를 공백으로 구분하여 입력받기
n = int(input())

# x,y 좌표 선언 및 초기값 설정
x, y = 1, 1

# 2칸 위로, 1칸 오른쪽
# 1칸 위로, 2칸 오른쪽
# 1칸 아래로, 2칸 오른쪽
# 2칸 아래로, 1칸 오른쪽
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 여행자의 계획 배열로 받음
plans = input().split()
move_type = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            new_x = x + dx[i]
            new_y = y + dy[i]
        
    
    # 공간을 벗어나는 경우 무시
    if new_x < 1 or new_y < 1 or new_x > n or new_y > n:
        # 다음 순번의 loop를 돌도록 넘어감
        continue

    x, y = new_x, new_y

print(x, y)