from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int,input().split())

arr = [i for i in range(1,n+1)]
visit = [False] * n
ans = []
def dfs(cnt,prev):
    if cnt == m:
        print(' '.join(map(str,ans)), end='\n')
        return
    for i,v in enumerate(arr):
        if not visit[i] and prev < v:
            visit[i] = True
            ans.append(v)
            dfs(cnt+1,v)
            visit[i] = False
            ans.pop()
dfs(0,0)
            
