from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(lambda i: (i[0],int(i[1])) ,enumerate(input().split(),1)))
dp = [0] *(n)
arr.sort(key=lambda x: x[1])
dp[0] = arr[0][1]
for i in range(1,n):
    dp[i] = arr[i][1] + dp[i-1]
print(sum(dp))