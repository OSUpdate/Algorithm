from sys import stdin

input = stdin.readline

t = int(input())
dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(t):
    num = int(input())
    for i in range(4,num+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[num])