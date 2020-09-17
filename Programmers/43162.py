from collections import deque

def solution(n, computers):
    answer = 0
    visit = [False] * n
    for i in range(n):
        if visit[i]:
            continue
        q = deque()
        q.append(i)
        visit[i] = True
        while q:
            cur = q.popleft()
            for j,conn in enumerate(computers[cur]):
                if conn == 1 and not visit[j]:
                    q.append(j)
                    visit[j] = True
        answer += 1


    
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))