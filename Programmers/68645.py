
from itertools import chain

def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    maximum = sum([len(i) for i in answer])
    print(maximum)
    dir = [(1,0),(0,1),(-1,-1)]
    x,y = 0,0
    idx = 0
    for i in range(1,maximum+1):
        print(y,x,idx)
        answer[y][x] = i
        if y+ dir[idx][0] < 0 or y+ dir[idx][0] >= n or x+ dir[idx][1] > y+ dir[idx][0] or answer[y+dir[idx][0]][x+dir[idx][1]] != 0:
            idx += 1
            if idx > 2:
                idx = 0

        y = y + dir[idx][0]
        x = x + dir[idx][1]
    

    return list(chain(*answer))


print(solution(4))
print(solution(6))
