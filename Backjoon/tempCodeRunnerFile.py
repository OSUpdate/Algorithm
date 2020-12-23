from sys import stdin
import copy

input = stdin.readline
n = int(input())
arr = []
direct = ['L', 'D', 'R', 'U']
for _ in range(n):
    arr.append(list(map(int, input().split())))

def move(dir):
    global arr,n
    if dir == 'L':
        for i in range(n):
            for j in range(n-1):
                if arr[i][j] == arr[i][j+1]:
                    arr[i][j] = arr[i][j]*2
                    arr[i][j+1] = 0
                if arr[i][j] == 0 and arr[i][j+1] != 0:
                    arr[i][j] = arr[i][j+1]
                    arr[i][j+1] = 0
    elif dir == 'D':
        for i in range(n):
            for j in range(n-1, 0,-1):
                if arr[j][i] == arr[j-1][i]:
                    arr[j][i] = arr[j][i]*2
                    arr[j-1][i] = 0
                if arr[j][i] == 0 and arr[j-1][i] != 0:
                    arr[j][i] = arr[j-1][i]
                    arr[j-1][i] = 0
    elif dir == 'R':
        for i in range(n-1, -1,-1):
            for j in range(n-1, 0,-1):
                if arr[i][j] == arr[i][j-1]:
                    arr[i][j] = arr[i][j-1]*2
                    arr[i][j-1] = 0
                if arr[i][j] == 0 and arr[i][j-1] != 0:
                    arr[i][j] = arr[i][j-1]
                    arr[i][j-1] = 0
    else:
        for i in range(n):
            for j in range(n-1):
                if arr[j][i] == arr[j+1][i]:
                    arr[j][i] = arr[j][i]*2
                    arr[j+1][i] = 0
                if arr[j][i] == 0 and arr[j+1][i] != 0:
                    arr[j][i] = arr[j+1][i]
                    arr[j+1][i] = 0
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
