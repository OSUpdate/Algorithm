import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = []
answer = [[0]*n for _ in range(n)]
def bfs(cur):
    global arr,visit
    q= deque()
    q.append(cur)
    while q:
        tmp = q.popleft()
        for k,v in enumerate(arr[tmp]):
            if v== 1 and not visit[k]:
                visit[k] = True
                q.append(k)

def dfs(cur):
    global arr,visit
    for k,v in enumerate(arr[cur]):
        if v == 1 and not visit[k]:
            visit[k] = True
            dfs(k)
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    visit = [False] * n
    bfs(i)
    for j in range(n):
        if visit[j]:
            answer[i][j] = 1
for lst in answer:
    for a in lst:
        print("%d " % a)
    print()
