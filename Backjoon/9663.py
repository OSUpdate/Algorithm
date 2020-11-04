from sys import stdin

input = stdin.readline

n = int(input())
arr = [0]*n 
visit = [False]*n
ans = 0
def check(index):
    global arr
    for i in range(index):
        if arr[index] == arr[i] or abs(arr[index]-arr[i]) == index - i:
            return False
    return True
def dfs(index):
    global n,visit,arr
    if index == n:
        global ans
        ans += 1
        return
    for i in range(n):
        arr[index] = i
        if not visit[i] and check(index):
            visit[i] = True
            dfs(index+1)
            visit[i] = False


dfs(0)
print(ans)