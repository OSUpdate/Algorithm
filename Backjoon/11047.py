from sys import stdin

input = stdin.readline

n, k = map(int,input().split())
arr = []
cnt = 0
for i in range(n):
    tmp = int(input())
    if k >= tmp:
        arr.append(tmp)
arr.reverse()
for v in arr:
    cnt += k //v
    k = k % v
    print(k,v, cnt)