from sys import stdin
import copy

input = stdin.readline
n = int(input())

direct = ['L', 'D', 'R', 'U']
arr = [list(map(int, input().split())) for _ in range(n)]

def move(dir):
    global arr,n
    if dir == 'L':
        for i in range(n):
            idx = 0
            for j in range(1,n):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = tmp
                    elif arr[i][idx] == tmp:
                        arr[i][idx] *= 2
                        idx += 1
                    else:
                        idx += 1
                        arr[i][idx] = tmp

                
    elif dir == 'D':
        for i in range(n):
            idx = n-1
            for j in range(n-2, -1,-1):
                if arr[j][i]:
                    tmp = arr[j][i]
                    arr[j][i] = 0
                    if arr[idx][i] == 0:
                        arr[idx][i] = tmp
                    elif arr[idx][i] == tmp:
                        arr[idx][i] *= 2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[idx][i] = tmp
    elif dir == 'R':
        for i in range(n):
            idx = n-1
            for j in range(n-2, -1,-1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = tmp
                    elif arr[i][idx] == tmp:
                        arr[i][idx] *= 2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[i][idx] = tmp

    else:
        for i in range(n):
            idx = 0
            for j in range(1,n):
                if arr[j][i]:
                    tmp = arr[j][i]
                    arr[j][i] = 0
                    if arr[idx][i] == 0:
                        arr[idx][i] = tmp
                    elif arr[idx][i] == tmp:
                        arr[idx][i] *= 2
                        idx += 1
                    else:
                        idx += 1
                        arr[idx][i]
def dfs(cnt):
    global direct,n, answer,arr
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(arr[i][j],answer)
        return
    tmp = copy.deepcopy(arr)
    for dir in direct:
        move(dir)
        dfs(cnt+1)
        arr = copy.deepcopy(tmp)
answer = 0
dfs(0)
print(answer)
