def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):

        while stack and prices[stack[-1]] > prices[i]:
            tmp = stack.pop()
            answer[tmp] = i - tmp
        stack.append(i)
    while stack:
        tmp = stack.pop()
        answer[tmp] = len(prices) - tmp -1
    print(answer)
    return answer

solution([1, 2, 3, 2, 3])