from sys import stdin
from copy import deepcopy

input = stdin.readline

n = int(input())
tmp = []
dp = []
for i in range(n):
    tmp.append(list(map(int,input().split())))
    dp.append([0 for _ in range(n)])
dp[0][0] = tmp[0][0]
for i in range(1,len(tmp)):
    for j in range(len(tmp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j]+tmp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j]+tmp[i][j],dp[i-1][j-1] + tmp[i][j])
print(max(dp[n-1]))