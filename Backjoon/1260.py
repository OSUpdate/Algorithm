import sys
from collections import deque
def init(arr,n):
    tmp = [[] for i in range(n)]
    for i,v in enumerate(arr):
        tmp[v[0]-1].append(v[1]-1)
        tmp[v[1]-1].append(v[0]-1)
    for i in tmp:
        i.sort()
    return tmp

def bfs(v):
    global graph
    visit = []
    q = deque()
    q.append(v)
    visit.append(v)
    while q:
        tmp = q.popleft()
        for i,d in enumerate(graph[tmp-1]):
            if d+1 not in visit:
                visit.append(d+1)
                q.append(d+1)
    print(' '.join(map(str,visit)))
    return visit

def dfs(v):
    global graph
    visit = []
    stack = []
    stack.append(v)
    visit.append(v)
    while stack:
        tmp = stack.pop()
        if tmp not in visit:
            visit.append(tmp)
        for i,d in enumerate(reversed(graph[tmp-1])):
            if d+1 not in visit:
                stack.append(d+1)
                
    print(' '.join(map(str,visit)))
    return visit


n,m,v = map(int,sys.stdin.readline().split())
arr = []
graph =[]
for i in range(m):
    v1,v2 = map(int,sys.stdin.readline().split())
    arr.append((v1,v2))
graph = init(arr,n)
dfs(v)
bfs(v)
