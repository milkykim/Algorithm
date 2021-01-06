# 백준 펠린드롭
# https://www.acmicpc.net/problem/1254

s = input()
n = len(s)

for i in range(n):
  print(s[i:])

  # s[i:] s의 i부터 끝까지를 역순으로 뒤집다는 뜻
  print(s[i:][::-1])

  # i부터 끝까지, 역순으로 했을 때 동일한 문자가 나오면, 
  # 그 단어는 펠린드롭을 만들 수 있는 문자라는 뜻
  # 원래 있던 단어 길이에 해당 단어를 인덱스를 추가하기
  if s[i:] == s[i:][::-1] :
    print(n+i)
    break