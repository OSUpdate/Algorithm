from sys import stdin

input = stdin.readline

n,m = map(int,input().split())

arr = [i for i in range(1,n+1)]
visit = [False] * n
ans = []
def dfs(cnt):
    if cnt == m:
        print(' '.join(map(str,ans)), end='\n')
        return
    for i,v in enumerate(arr):
        ans.append(v)
        dfs(cnt+1)
        ans.pop()
dfs(0)
            
