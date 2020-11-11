N = int(input())
grade = []

for _ in range(N):
    grade.append(input().split())

grade = sorted(grade, key = lambda x: [-int(x[1]), int(x[2]), -int(x[3]), x[0]])

for i in grade:
  print(i[0])