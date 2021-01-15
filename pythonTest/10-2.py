from sys import stdin

input = stdin.readline

n,m = map(int,input().split())
arr = [i for i in range(n+1)]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
for _ in range(m):
    num,a,b = map(int,input().split())
    if num == 0:
        union(arr,a,b)
    if num == 1:
        print("NO" if find(arr,a) != find(arr,b) else "YES")