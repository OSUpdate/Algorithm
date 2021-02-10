from sys import stdin
from collections import deque
input = stdin.readline
def bfs(arr,colors,visit,start):
    q = deque()
    q.append(start)
    colors[start] = 1
    while q:
        cur = q.popleft()
        for v in arr[cur]:
            if colors[v] == 0:
                if colors[cur] == 1:
                    colors[v] = 2
                elif colors[cur] == 2:
                    colors[v] = 1
                q.append(v)
            elif colors[cur] == colors[v]:
                return False
    return True
def dfs(arr,colors,visit,cur):
    if visit[cur]:
        return
    for v in arr[cur]:
        visit[v] = True
        if colors[cur] == 'R':
            colors[v] = 'B'
            
            dfs(arr,colors,visit,v)
        else:
            colors[v] = 'R'
            dfs(arr,colors,visit,v)
t = int(input())
for _ in range(t):
    v,e = map(int,input().split())
    arr = [[] for i in range(v+1)]
    colors = [0]*(v+1)
    visit = [False] * (v+1)
    check = False
    for _ in range(e):
        a, b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    
    for i in range(1,v+1):
        if colors[i] == 0:
            if not bfs(arr,colors,visit,i):
                check = True
                break
        '''
    for i in range(1,v+1):
        dfs(arr,colors,visit,i)
    for i in range(1,len(arr)):
        for j in arr[i]:
            if colors[i] == colors[j]:
                check = True
                '''
    print('NO' if check else 'YES')