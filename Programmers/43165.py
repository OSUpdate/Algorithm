from collections import deque


def solution(numbers, target):
    opt = ['+','-']
    q = deque()
    q.append((numbers[0],1,len(numbers)))
    q.append((-numbers[0],1,len(numbers)))
    answer = 0
    while q:
        cur,index,end = q.popleft()
        if index == end:
            break
        for op in opt:
            if op == '+':
                n = cur + numbers[index]
            elif op == '-':
                n = cur - numbers[index]
            if n == target and index + 1 == end:
                answer += 1
            
            q.append((n,index+1,end))
            
    return answer

print(solution([1, 1, 1, 1, 1],3))