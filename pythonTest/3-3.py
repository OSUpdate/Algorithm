from sys import stdin

input = stdin.readline

n,m = map(int,input().split())
arr = []
answer = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    maximum = min(tmp)
    answer = max(maximum,answer)
print(answer)