n = int(input())

count = 0

while True:
  # n을 5로 나누어 떨어지면
  if (n % 5) == 0:
    count += n//5
    print(count)
    break

  n = n-3
  count += 1
  if n < 0:
    print("-1")
    break