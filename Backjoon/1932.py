from sys import stdin

input = stdin.readline

n = int(input())
pre = 0
dp = []
for i in range(n):
    tmp = list(map(int,input().split()))
    if len(tmp) == 1:
        pre = tmp[0]
    else:
        for v in tmp:
            pre = v