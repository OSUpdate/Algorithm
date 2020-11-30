from collections import deque

direct = [(1,0),(0,1),(-1,0),(0,-1)]

def check(x,y,n):
    return (x >= 0 and x < n) and ( y >= 0 and y < n)
def bfs(arr,visit, n, x, y):
    global direct
    q = deque()
    q.append((x,y))
    cur = arr[x][y]
    cnt = 0
    while q:
        x,y = q.popleft()
        visit[x][y] = True
        for dir in direct:
            nx = x + dir[0]
            ny = y + dir[1]
            if check(nx,ny,n) and arr[nx][ny] == cur and not visit[nx][ny]:
                q.append((nx,ny))
                visit[nx][ny] = True
    return cnt
def solution(v):
    answer = [0,0,0]
    n = len(v)
    visit=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                cnt = bfs(v,visit,n,i,j)
                print(cnt)
                answer[v[i][j]] += 1
    return answer
arr = [[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]
print(solution(arr))