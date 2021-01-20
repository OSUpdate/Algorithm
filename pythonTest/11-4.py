from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int,input().split()))
d = [0]*(sum(arr)+1)
visit = [False]*n

def dfs(num,cur,end):
    global arr,visit,d
    if cur == end:
        print(num)
        d[num] += 1
        return
    for i,v in enumerate(arr):
        if not visit[i]:
            visit[i] = True
            dfs(num+v,cur+1,end)
            visit[i] = False

for i in range(1,n+1):
    dfs(0,0,i)
for i in range(1,len(d)):
    if d[i] == 0:
        print(i)

    