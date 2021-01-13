# def solution(clothes):
#     answer = {}
#     for i in clothes:
#         if i[1] in answer: 
#             answer[i[1]] += 1
#         else: 
#             answer[i[1]] = 1

#     cnt = 1
    
#     for i in answer.values():
#         cnt *= (i+1)
        
#     return cnt - 1

from collections import Counter

def solution(clothes):
    counter_each_category = Counter([cat for _, cat in clothes])
    print(counter_each_category)
    all_possible = 1

    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)

    return all_possible - 1