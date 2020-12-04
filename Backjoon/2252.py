from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int,input().split())
answer = [0]*n
degree = [0]*n
arr = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a-1].append(b-1)
    degree[b-1] += 1
print(degree,arr)
def sort():
    global degree,arr,n,answer
    q = deque()
    for i in range(n):
        if degree[i] == 0:
            q.append(i)
    print(q)
    for i in range(n):
        if not q:
            return
        cur = q.popleft()
        answer[i] = cur + 1
        print(i,cur,answer)
        for nxt in arr[cur]:
            degree[nxt] -= 1
            print(nxt,degree)
            if degree[nxt] == 0:
                q.append(nxt)
                print(q)
sort()
print(' '.join(map(str,answer)))


