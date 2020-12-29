from sys import stdin

input = stdin.readline
n = int(input())
arr = [0 for i in range(n+1)]
d = [0] * 30001
def dfs(num, cnt):
    global arr
    if arr[cnt] != 0:
        return
    if num == 1:
        arr[cnt] = cnt
        return
    if num % 5 == 0:
        dfs(num//5,cnt+1)
    if num % 3 == 0:
        dfs(num//3,cnt+1)
    if num % 2 == 0:
        dfs(num//2,cnt+1)
    dfs(num-1,cnt+1)
for i in range(2, n+1):
    d[i] = d[i-1] +1
    if d[i] % 5 == 0:
        d[i] = min(d[i],d[i//5]+1)
    if d[i] % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if d[i] % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
dfs(n,0)
print(arr)