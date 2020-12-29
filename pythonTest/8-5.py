from sys import stdin

input = stdin.readline

n,m = map(int,input().split())
arr = [int(input()) for i in range(n)]
dp = [10001]*(m+1)

dp[0] =0
for i in range(n):
    for j in range(arr[i],m+1):
        dp[j] = min(dp[j],dp[j-arr[i]]+1)
print(dp)
