def solution(numbers):
    s_numbers = [str(n) for n in numbers]
    answer = sorted(s_numbers, key=lambda x: x * 3, reverse=True)
    if set(answer) == {"0"}:
        answer = ["0"]
    return "".join(answer)
