# N를 공백으로 구분하여 입력받기
n = int(input())

# x,y 좌표 선언 및 초기값 설정
x, y = 1, 1

# 좌 우 업 다운
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
        continue

    x, y = new_x, new_y

print(x, y)



  
n = int(input())
command = input().split()
x, y = 1, 1
for c in command:
    if c == 'L' and y > 1:
        y -= 1
    elif c == 'R' and y < n:
        y += 1
    elif c == 'U' and x > 1:
        x -= 1
    elif c == 'D' and x < n:
        x += 1

print(x, y)