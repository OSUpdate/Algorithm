from collections import deque

def solution(board, r, c):
    arrow = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(1,0,1),(0,1,1),(-1,0,1),(0,-1,1)]
    q = deque()
    answer = 0
    q.append((r,c,0))
    for i in board:
        print(i)
    visit = [[False for _ in range(4)] for _ in range(4)]
    arr = [[0 for _ in range(4)] for _ in range(4)]
    while q:
        x,y,cnt = q.popleft()
        answer = max(answer,cnt)
        print(x,y,cnt)
        for _,d in enumerate(arrow):
            tmp = 1
            nx,ny = x,y
            if d[2] == 1:
                while 0 <= nx+d[0] < 4 and 0<= ny+d[1] < 4:
                    nx += d[0]
                    ny += d[1]
                    if board[nx][ny] != 0:
                        break

                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    if board[nx][ny] != 0:
                        tmp += 1
                        board[nx][ny] = 0
                    q.append((nx,ny,cnt+tmp))
                    
                
            else:
                nx += d[0]
                ny += d[1]
                if 0<=nx<4 and 0<=ny<4 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    if board[nx][ny] != 0:
                        tmp += 1
                        board[nx][ny] = 0

                    q.append((nx,ny,cnt+tmp))
        
    for i in board:
        print(i)
    return answer

print(solution(	[[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))