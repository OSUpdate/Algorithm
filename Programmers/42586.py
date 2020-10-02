from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-p)/s) for p,s in zip(progresses,speeds)]
    cur = 0
    idx = 0
    for v in days:
        if cur < v:
            cur = v
            answer.append(1)
            idx += 1
        else:
            answer[idx-1] += 1
    print(days)


    print(answer)
    return answer
solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])